from simulation_runner.configurations.configuration_classes import (
    ExperimentParameterToVary,
    ExperimentParameterConfigurator,
)


def get_experiment_base_run_root_folder():
    return r"C:/Users/nina/Documents/04_Model_220620/04_Model/03_simulation_runs/02_scenarios/base_scenario_hydraulic"


def prepare_experiment_configurations():
    if use_discharge_file := True:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="DISF",
            values=[
                r"C:\Users\nina\Documents\04_Model_220511\04_Model\01_input_data\Hydrographs\SarineHydrograph_1_continue_initial_filling.txt",
            ],
            json_file_name="model.json",
        )
    else:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="DISF",
            values=[
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax60_short_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax60_middle_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax60_long_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax120_short_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax120_middle_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax120_long_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax240_short_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax240_middle_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax240_long_complete.txt",
                r"C:/Users/nina/Documents/04_Model_220511/04_Model/01_input_data/hydrographs_scenarios/qmax480_short_complete.txt",
            ],
            json_file_name="model.json",
        )

    sim_time = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SIMULATION/TIME/end",
        parameter_name="end",
        values=[126_000],
        json_file_name="simulation.json",
    )

    friction = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/FRICTION/default_friction",
        parameter_name="k",
        values=[35],
        json_file_name="model.json",
    )

    return ExperimentParameterConfigurator(
        [discharge, sim_time, friction]
    )
