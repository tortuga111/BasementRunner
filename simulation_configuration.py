from simulation_runner.configurations.configuration_classes import (
    ExperimentParameterToVary,
    ExperimentParameterConfigurator,
)


def get_experiment_base_run_root_folder():
    return r"C:/Users/nina/Documents/04_Model_220321/04_Model/03_simulation_runs/07_calibration_runs_hw20_new_mesh/base_scenario"


def prepare_experiment_configurations():
    if use_discharge_file := True:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            name_in_json="discharge_file",
            values=[
                r"C:/Users/nina/Documents/04_Model_220321/04_Model/01_input_data/Hydrographs/Hydrograph_1_continue_HW2020.txt",
            ],
            json_file_name="model.json",
        )
    else:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge",
            name_in_json="discharge",
            values=[
                r"C:/Users/nina/Documents/04_Model_220321/04_Model/01_input_data/Hydrographs/SarineHydrograph_1_continue_HW2020_testshort.txt"
            ],
            json_file_name="model.json",
        )

    simulation_time = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SIMULATION/TIME/end",
        name_in_json="end",
        values=[120_000],
        json_file_name="simulation.json"
        )

    bed_load_inflow = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDLOAD/BOUNDARY/STANDARD",
        name_in_json="bed_load_inflow",
        values=[
            [
                {"boundary_factor": 1.0, "name": "input", "string_name": "input", "type": "transport_capacity"},
                {"boundary_factor": 1.0, "name": "output", "string_name": "output", "type": "transport_capacity"},
            ]
        ],
        json_file_name="model.json",
    )
    fixed_bed = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/FIXED_BED/regions",
        name_in_json="fixed_bed",
        json_file_name="model.json",
        values=[
            [
                {"region_name": "one", "z_rel": 0.0},
                {"region_name": "two", "z_rel": 0.0},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ]
        ],
    )
    return ExperimentParameterConfigurator([discharge, simulation_time, bed_load_inflow, fixed_bed])