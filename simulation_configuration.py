from simulation_runner.configurations.configuration_classes import (
    ExperimentParameterToVary,
    ExperimentParameterConfigurator,
)


def get_experiment_base_run_root_folder():
    return r"C:\Users\nina\Documents\04_Model_220427\04_Model\03_simulation_runs\01_calibration_run_with_new_mesh\base_scenario"


def prepare_experiment_configurations():
    if use_discharge_file := True:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="DISF",
            values=[
                r"C:/Users/nina/Documents/04_Model_220427/04_Model/01_input_data/Hydrographs/HW20_112max.txt",
            ],
            json_file_name="model.json",
        )
    else:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge",
            parameter_name="DIS",
            values=[
                r"C:/Users/nina/Documents/04_Model_220321/04_Model/01_input_data/Hydrographs/SarineHydrograph_1_continue_HW2020_testshort.txt",
            ],
            json_file_name="model.json",
        )


    sim_time = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SIMULATION/TIME/end",
        parameter_name="end",
        values=[111900],
        json_file_name="simulation.json",
    )

    critical_angle_dry = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/GRAVITATIONAL_TRANSPORT/critical_angle_dry",
        parameter_name="CAD",
        json_file_name="model.json",
        values=[60.0],
    )
    critical_angle_wet = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/GRAVITATIONAL_TRANSPORT/critical_angle_wet",
        parameter_name="CAW",
        json_file_name="model.json",
        values=[40],
    )
    repose_angle = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/INCIPIENT_MOTION/repose_angle",
        parameter_name="repose_angle",
        json_file_name="model.json",
        values=[40],
    )

    fixed_bed = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/FIXED_BED/regions",
        parameter_name="fixed_bed",
        json_file_name="model.json",
        values=[
            [
                {"region_name": "one", "z_rel": -0.2},
                {"region_name": "two", "z_rel": -0.5},
                {"region_name": "three", "z_rel": -0.2},
                {"region_name": "four", "z_rel": -0.5},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.0},
            ],
            [
                {"region_name": "one", "z_rel": -0.5},
                {"region_name": "two", "z_rel": -0.5},
                {"region_name": "three", "z_rel": -0.5},
                {"region_name": "four", "z_rel": -0.5},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.0},
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
        values=[[0.082]],
    )
    return ExperimentParameterConfigurator(
        [discharge, sim_time, critical_angle_wet, critical_angle_dry, repose_angle, fixed_bed, grain_size, friction]
    )
