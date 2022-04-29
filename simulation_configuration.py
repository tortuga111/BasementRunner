from simulation_runner.configurations.configuration_classes import (
    ExperimentParameterToVary,
    ExperimentParameterConfigurator,
)


def get_experiment_base_run_root_folder():
    return r"D:/Nina/04_Model_220411/04_Model/03_simulation_runs/08_calibration_runs_hw20_beyonce/base_scenario"


def prepare_experiment_configurations():
    if use_discharge_file := True:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="discharge_file",
            values=[
                r"D:/Nina/04_Model_220411/04_Model/01_input_data/Hydrographs/Hydrograph_HW2020_115000.txt",
            ],
            json_file_name="model.json",
        )
    else:
        discharge = ExperimentParameterToVary(
            pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/BOUNDARY/STANDARD/0/discharge_file",
            parameter_name="discharge_file",
            values=[
                r"D:/Nina/04_Model_220411/04_Model/01_input_data/Hydrographs/SarineHydrograph_testshort2.txt"
            ],
            json_file_name="model.json",
        )

    simulation_time = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SIMULATION/TIME/end",
        parameter_name="end",
        values=[115_000],
        json_file_name="simulation.json"
    )

    grain_diameter = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/GRAIN_CLASS/diameters",
        parameter_name="grain_diameter",
        values=[[0.082]],
        json_file_name="model.json",
    )

    kst_regions = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/HYDRAULICS/FRICTION/regions",
        parameter_name="kst_regions",
        json_file_name="model.json",
        values=[
            [
                {
                    "friction": 7.0,
                    "region_name": "three"
                },
                {
                    "friction": 10.0,
                    "region_name": "four"
                },
                {
                    "friction": 35.0,
                    "region_name": "one"
                },
                {
                    "friction": 35.0,
                    "region_name": "two"
                },
                {
                    "friction": 10.0,
                    "region_name": "seven"
                },
                {
                    "friction": 50.0,
                    "region_name": "eight"
                },
                {
                    "friction": 35.0,
                    "region_name": "five"
                },
                {
                    "friction": 35.0,
                    "region_name": "six"
                },
            ],
            [
                {
                    "friction": 7.0,
                    "region_name": "three"
                },
                {
                    "friction": 10.0,
                    "region_name": "four"
                },
                {
                    "friction": 30.0,
                    "region_name": "one"
                },
                {
                    "friction": 30.0,
                    "region_name": "two"
                },
                {
                    "friction": 10.0,
                    "region_name": "seven"
                },
                {
                    "friction": 50.0,
                    "region_name": "eight"
                },
                {
                    "friction": 30.0,
                    "region_name": "five"
                },
                {
                    "friction": 30.0,
                    "region_name": "six"
                },
            ],
        ]
    )

    fixed_bed = ExperimentParameterToVary(
        pointer_to_location_in_json=r"/SETUP/DOMAIN/BASEPLANE_2D/MORPHOLOGY/BEDMATERIAL/FIXED_BED/regions",
        parameter_name="fixed_bed",
        json_file_name="model.json",
        values=[
            [
                {"region_name": "one", "z_rel": -2.0},
                {"region_name": "two", "z_rel": -2.0},
                {"region_name": "three", "z_rel": -2.0},
                {"region_name": "four", "z_rel": -2.0},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.05},
            ],
            [
                {"region_name": "one", "z_rel": -1.5},
                {"region_name": "two", "z_rel": -1.5},
                {"region_name": "three", "z_rel": -1.5},
                {"region_name": "four", "z_rel": -1.5},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.05},
            ],
            [
                {"region_name": "one", "z_rel": -1.0},
                {"region_name": "two", "z_rel": -1.0},
                {"region_name": "three", "z_rel": -1.0},
                {"region_name": "four", "z_rel": -1.0},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.05},
            ],
            [
                {"region_name": "one", "z_rel": -0.5},
                {"region_name": "two", "z_rel": -0.5},
                {"region_name": "three", "z_rel": -0.5},
                {"region_name": "four", "z_rel": -0.5},
                {"region_name": "five", "z_rel": -0.1},
                {"region_name": "six", "z_rel": 0.0},
                {"region_name": "seven", "z_rel": -0.5},
                {"region_name": "eight", "z_rel": -0.05},
            ],

        ],
    )
    return ExperimentParameterConfigurator([discharge, simulation_time, fixed_bed, grain_diameter, kst_regions])
