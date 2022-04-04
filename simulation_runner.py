from concurrent.futures import ProcessPoolExecutor

from helpers.global_and_constant_values import GlobalConstants
from simulation_configuration import prepare_experiment_configurations, get_experiment_base_run_root_folder
from simulation_runner.prepare_basement.preparation import create_experiment, store_paths_to_experiment_results
from simulation_runner.run_basement.basement_scenario_configuration import (
    BasementScenarioConfiguration,
    BasementSimulationBackendConfiguration,
)
from simulation_runner.run_basement.results import export_results
from simulation_runner.run_basement.setup import setup
from simulation_runner.run_basement.simulation import simulate


def run_basement(root_path_to_experiment: str, basement_configuration: BasementSimulationBackendConfiguration) -> None:
    config = BasementScenarioConfiguration(
        experiment_run_root_folder=root_path_to_experiment,
        results_configuration_file_name=GlobalConstants.results_configuration_file_name,  # do not change
        simulation_configuration_file_name=GlobalConstants.simulation_configuration_file_name,  # do not change
        model_configuration_file_name=GlobalConstants.model_configuration_file_name,  # do not change
        basement_configuration=basement_configuration,
    )
    setup(config)
    simulate(config)
    export_results(config)


def main() -> None:
    experiment_base_run_root_folder = get_experiment_base_run_root_folder()
    configurator = prepare_experiment_configurations()
    root_paths_for_experiments_to_run = []
    for parameter_configuration in configurator.iterator_for_all_parameter_combinations():
        root_paths_for_experiments_to_run.append(
            create_experiment(experiment_base_run_root_folder, parameter_configuration)
        )

    if do_single_threaded := False:
        for path in root_paths_for_experiments_to_run:
            run_basement(path, BasementSimulationBackendConfiguration.single_threaded_with_gpu)
    else:
        index_to_split_on = round(1 / 3 * len(root_paths_for_experiments_to_run))
        cpu_paths = root_paths_for_experiments_to_run[:index_to_split_on]
        gpu_paths = root_paths_for_experiments_to_run[index_to_split_on:]
        with ProcessPoolExecutor(1) as cpu:
            cpu_jobs = [
                cpu.submit(run_basement, path, BasementSimulationBackendConfiguration.multi_threaded_with_20_threads)
                for path in cpu_paths
            ]
            with ProcessPoolExecutor(1) as gpu:
                gpu_jobs = [
                    gpu.submit(run_basement, path, BasementSimulationBackendConfiguration.single_threaded_with_gpu)
                    for path in gpu_paths
                ]
        print("all jobs scheduled")
        [job.result() for job in gpu_jobs + cpu_jobs]

    store_paths_to_experiment_results(experiment_base_run_root_folder, root_paths_for_experiments_to_run)


if __name__ == "__main__":
    main()
