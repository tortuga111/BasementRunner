import os.path
from dataclasses import dataclass


@dataclass(frozen=True)
class GlobalConstants:
    root_path_to_basement_executables = os.path.normpath("C:\\Program Files\\BASEMENT 3.1.1\\bin")
    experiment_sub_folder_name = "experiments"
    file_name_to_store_paths_to_results = "paths_to_experiments.json"
    results_configuration_file_name = "results.json"  # do not change
    results_h5_file_name = "output.h5"  # do not change
    simulation_configuration_file_name = "simulation.json"  # do not change
    model_configuration_file_name = "model.json"  # do not change
