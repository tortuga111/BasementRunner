import os
from pathlib import Path

from helpers.global_and_constant_values import GlobalConstants
from helpers.helpers import change_back_to_original_wd_afterwards
from simulation_runner.run_basement.basement_scenario_configuration import (
    BasementSimulationBackendConfiguration,
    BasementScenarioConfiguration,
)


def _get_path_to_basement_simulation_executable(
    basement_simulation_backend_configuration: BasementSimulationBackendConfiguration,
) -> str:
    root_path_to_basement_executables = GlobalConstants.root_path_to_basement_executables
    return handle_white_spaces_in_path(
        Path(root_path_to_basement_executables, basement_simulation_backend_configuration.value)
    )


def handle_white_spaces_in_path(path: Path) -> str:
    return rf'"{path.parent}\{path.parts[-1].split(" ")[0]}" {" ".join(path.parts[-1].split(" ")[1:])}'


def simulate(basement_simulation_configuration: BasementScenarioConfiguration) -> None:
    executable_path = _get_path_to_basement_simulation_executable(
        basement_simulation_configuration.basement_configuration
    )
    shell_string_for_simulation = basement_simulation_configuration.to_shell_string_for_simulation()
    with change_back_to_original_wd_afterwards(basement_simulation_configuration.experiment_run_root_folder):
        return_code = os.system(f"{executable_path} {shell_string_for_simulation} -p")
        if not return_code == 0:
            raise TypeError(f"{return_code=}")
