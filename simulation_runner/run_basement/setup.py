import os
from pathlib import Path

from helpers.global_and_constant_values import GlobalConstants
from helpers.helpers import change_back_to_original_wd_afterwards
from simulation_runner.run_basement.basement_scenario_configuration import BasementScenarioConfiguration


def _get_path_to_basement_setup_executable() -> Path:
    executable_path = os.path.join(GlobalConstants.root_path_to_basement_executables, "BMv3_BASEplane_setup.exe")
    return Path(f'"{executable_path}"')


def setup(basement_simulation_configuration: BasementScenarioConfiguration) -> None:
    executable_path = _get_path_to_basement_setup_executable()
    with change_back_to_original_wd_afterwards(basement_simulation_configuration.experiment_run_root_folder):
        return_code = os.system(f"{executable_path} {basement_simulation_configuration.to_shell_string_for_setup()}")
        if not return_code == 0:
            raise TypeError(f"{return_code=}")
