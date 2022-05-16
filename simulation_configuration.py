from simulation_runner.configurations.configuration_classes import (
    ExperimentParameterToVary,
    ExperimentParameterConfigurator,
)


def get_experiment_base_run_root_folder():
    return r"D:\Nina\04_Model_220511\04_Model\03_simulation_runs\01_calibration_run_with_new_mesh\base_scenario"


def prepare_experiment_configurations():
    if use_discharge_file := True:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="DISF",
            values=[
                r"D:\Nina\04_Model_220511/04_Model/01_input_data/Hydrographs/hydrograph_hw20_corr.txt",
            ],
            json_file_name="model.json",
        )
    else:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge",
            parameter_name="DIS",
            values=[
                r"D:\Nina\04_Model_220321/04_Model/01_input_data/Hydrographs/SarineHydrograph_1_continue_HW2020_testshort.txt",
            ],
            json_file_name="model.json",
        )


    sim_time = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SIMULATION/TIME/end",
        parameter_name="end",
        values=[90000],
        json_file_name="simulation.json",
    )

    boundary_factor = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDLOAD/BOUNDARY/STANDARD/0/boundary_factor",
        parameter_name="boundary",
        json_file_name="model.json",
        values=[0],
    )

    fixed_bed = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/FIXED_BED/regions",
        parameter_name="FB",
        json_file_name="model.json",
        values=[
            [
                {"region_name": "one", "z_rel": -0.0},
                {"region_name": "two", "z_rel": -0.0},
                {"region_name": "three", "z_rel": -0.0},
                {"region_name": "four", "z_rel": -0.0},
                {"region_name": "five", "z_rel": -0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.0},
                {"region_name": "eight", "z_rel": -0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.2},
                {"region_name": "two", "z_rel": 0.0},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.1},
                {"region_name": "two", "z_rel": 0.0},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.1},
                {"region_name": "two", "z_rel": -0.1},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.2},
                {"region_name": "two", "z_rel": -0.2},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.5},
                {"region_name": "two", "z_rel": -0.5},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
            [
                {"region_name": "two", "z_rel": 0.0},
                {"region_name": "three", "z_rel": 0.0},
                {"region_name": "four", "z_rel": 0.0},
                {"region_name": "five", "z_rel": 0.0},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": 0.0},
                {"region_name": "eight", "z_rel": 0.0},
            ],
        ],
    )

    friction = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/FRICTION/default_friction",
        parameter_name="k",
        values=[30.4],
        json_file_name="model.json",
    )

    grain_size = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/GRAIN_CLASS/diameters",
        parameter_name="grain_size",
        json_file_name="model.json",
        values=[[0.035], [0.057]],
    )
    return ExperimentParameterConfigurator(
        [discharge, sim_time, boundary_factor, fixed_bed, grain_size, friction]
    )
