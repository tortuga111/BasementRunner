import json
import os
import shutil
from typing import Iterable

from jsonpointer import set_pointer

from helpers.global_and_constant_values import GlobalConstants
from helpers.helpers import change_back_to_original_wd_afterwards
from simulation_runner.configurations.configuration_classes import SelectedParameterToChange


def create_experiment(
    experiment_base_run_root_folder: str, parameter_configuration: Iterable[SelectedParameterToChange]
):
    experiment_folder_name = "$".join(f"{p.name_in_json}@{p.key}" for p in parameter_configuration)
    directory_to_run_experiment = copy_base_experiment(experiment_base_run_root_folder, experiment_folder_name)
    replace_all_parameters_in_model_json_file(directory_to_run_experiment, parameter_configuration)
    return directory_to_run_experiment


def replace_all_parameters_in_model_json_file(
    path_to_files: str, parameters_to_replace: Iterable[SelectedParameterToChange]
) -> None:
    for parameter in parameters_to_replace:
        complete_file_path = os.path.join(path_to_files, parameter.json_file_name)
        with open(complete_file_path, "r") as json_file:
            loaded_json = json.load(json_file)
            set_pointer(loaded_json, parameter.pointer_to_location_in_json, parameter.value, inplace=True)
        with open(complete_file_path, "w") as json_file:
            json.dump(loaded_json, json_file, indent=4)


def load_paths_to_experiment_results(experiment_base_run_root_folder: str) -> tuple[str, ...]:
    experiment_results_root_directory = get_root_directory_for_experiment_results(experiment_base_run_root_folder)
    with change_back_to_original_wd_afterwards(experiment_results_root_directory):
        if os.path.exists(GlobalConstants.file_name_to_store_paths_to_results):
            with open(GlobalConstants.file_name_to_store_paths_to_results, "r") as json_file:
                return tuple(json.load(json_file))
        else:
            return tuple()


def store_paths_to_experiment_results(
    experiment_base_run_root_folder: str, root_paths_for_experiments_to_run: Iterable[str]
) -> None:
    experiment_results_root_directory = get_root_directory_for_experiment_results(experiment_base_run_root_folder)
    already_conducted_experiments = load_paths_to_experiment_results(experiment_base_run_root_folder)
    with change_back_to_original_wd_afterwards(experiment_results_root_directory):
        with open(GlobalConstants.file_name_to_store_paths_to_results, "w") as json_file:
            json.dump(tuple(root_paths_for_experiments_to_run) + already_conducted_experiments, json_file, indent=4)


def copy_base_experiment(experiment_base_run_root_folder: str, experiment_folder_name: str) -> str:
    with change_back_to_original_wd_afterwards(experiment_base_run_root_folder):
        experiment_results_root_directory = get_root_directory_for_experiment_results(experiment_base_run_root_folder)
        experiment_run_root_folder = os.path.join(experiment_results_root_directory, experiment_folder_name)
        shutil.copytree(experiment_base_run_root_folder, experiment_run_root_folder)
    return experiment_run_root_folder


def get_root_directory_for_experiment_results(experiment_base_run_root_folder: str) -> str:
    return os.path.join(os.path.dirname(experiment_base_run_root_folder), GlobalConstants.experiment_sub_folder_name)
