from dataclasses import dataclass
from enum import unique, Enum


@unique
class BasementSimulationBackendConfiguration(Enum):
    single_threaded = "BMv3_BASEplane_seq.exe"
    multi_threaded_with_20_threads = "BMv3_BASEplane_omp.exe -n 20"
    single_threaded_with_gpu = "BMv3_BASEplane_cudaC.exe"
    multi_threaded_with_20_threads_and_gpu = "BMv3_BASEplane_cudaO.exe -n 20"


@dataclass(frozen=True)
class BasementScenarioConfiguration:
    experiment_run_root_folder: str
    simulation_configuration_file_name: str
    model_configuration_file_name: str
    results_configuration_file_name: str
    basement_configuration: BasementSimulationBackendConfiguration
    __setup_h5_name = "setup.h5"
    __results_file_name = "results.h5"
    __output_name = "output.h5"

    def to_shell_string_for_setup(self) -> str:
        return f"-f {self.model_configuration_file_name} -o {self.__setup_h5_name}"

    def to_shell_string_for_simulation(self) -> str:
        return f"-r {self.__setup_h5_name} -f {self.simulation_configuration_file_name} -o {self.__output_name}"

    def to_shell_string_for_result(self) -> str:
        return f"-f {self.results_configuration_file_name} -r {self.__output_name} -o {self.__results_file_name}"
