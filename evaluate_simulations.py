import os.path
from typing import Iterable

import h5py
import py2dm
from geopandas import GeoDataFrame
from shapely.geometry import Polygon

from helpers.global_and_constant_values import GlobalConstants
from helpers.helpers import change_back_to_original_wd_afterwards
from simulation_configuration import get_experiment_base_run_root_folder
from simulation_runner.prepare_basement.preparation import (
    get_root_directory_for_experiment_results,
    load_paths_to_experiment_results,
)


def load_paths_to_results() -> tuple[str, ...]:
    experiment_base_run_root_folder = get_experiment_base_run_root_folder()
    experiment_results_root_directory = get_root_directory_for_experiment_results(experiment_base_run_root_folder)
    return load_paths_to_experiment_results(experiment_results_root_directory)


def extract_data_for_evaluation(path_to_root_directory: str) -> str:
    return path_to_root_directory


def process_and_evaluate_data(path_to_root_directory: str) -> str:
    path_to_results = os.path.join(path_to_root_directory, "evaluation")
    if not os.path.exists(path_to_results):
        os.mkdir(path_to_results)
    path_to_mesh = r"C:\Users\nina\Documents\04_Model_220321\04_Model\01_input_data\BF2020_Mesh\mesh_all_inputs\Project1_computational-mesh.2dm"
    triangle_polygons = []
    with py2dm.Reader(path_to_mesh) as mesh:
        nodes = {node.id: node for i, node in enumerate(mesh.nodes)}
        for element in mesh.elements:
            point_indices = element.nodes
            triangle_polygons.append(Polygon([nodes[point_index].pos for point_index in point_indices]))
    base_data_frame = GeoDataFrame(geometry=triangle_polygons)
    with change_back_to_original_wd_afterwards(path_to_results):
        h5_path = os.path.join(path_to_root_directory, GlobalConstants.results_h5_file_name)
        h5_results_data = h5py.File(h5_path, "r")
        append_time_series_data_to_geo_data_frame(
            base_data_frame, h5_results_data["RESULTS/CellsAll/BottomEl"], "bottom_elevation", ["BottomEl"]
        )
        append_time_series_data_to_geo_data_frame(
            base_data_frame, h5_results_data["RESULTS/CellsAll/HydState"], "hydraulic_state", ["Value", "DX", "DY"]
        )
        h5_path = os.path.join(path_to_root_directory, "results_aux.h5")
        h5_auxiliary_data = h5py.File(h5_path, "r")
        append_time_series_data_to_geo_data_frame(
            base_data_frame, h5_auxiliary_data["flow_velocity"], "flow_velocity", ["DX", "DY"]
        )
        append_time_series_data_to_geo_data_frame(
            base_data_frame, h5_auxiliary_data["flow_velocity_abs"], "flow_velocity_abs", ["Value"]
        )
    return path_to_results


def append_time_series_data_to_geo_data_frame(
    base_data_frame: GeoDataFrame, file_with_1d_data_per_step: h5py.File, file_name: str, column_names: Iterable[str]
) -> None:
    data_frame_to_fill = base_data_frame.copy(deep=True)
    for key in sorted(file_with_1d_data_per_step.keys(), key=lambda x: int(x)):
        for column_index, column_name in enumerate(column_names):
            column_key = f"{key}-{column_name}"
            data_frame_to_fill[column_key] = file_with_1d_data_per_step[key][:, column_index]
    data_frame_to_fill.to_file(f"{file_name}.shp" if not file_name.endswith(".shp") else file_name)


def main():
    paths_to_results = load_paths_to_results()

    paths_to_extracted_data = []
    for path in paths_to_results:
        paths_to_extracted_data.append(extract_data_for_evaluation(path))
    for path in paths_to_extracted_data:
        process_and_evaluate_data(path)


if __name__ == "__main__":
    main()
