import hashlib
from abc import ABC
from dataclasses import dataclass
from itertools import product
from typing import List, Union, Dict, Iterable


@dataclass(frozen=True)
class ParameterToVaryABC(ABC):
    pointer_to_location_in_json: str
    parameter_name: str
    json_file_name: str


@dataclass(frozen=True)
class ExperimentParameterToVary(ParameterToVaryABC):
    values: List[Union[str, float, list]]


@dataclass(frozen=True)
class SelectedParameterToChange(ParameterToVaryABC):
    key: str
    value: Union[str, int, float, bool]


def key_creator(value: any) -> str:
    if isinstance(value, float)  or isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return value.split("/")[-1]
    if isinstance(value, dict) or isinstance(value, list):
        return str(int(hashlib.md5(str(value).encode()).hexdigest()[:7], 16))
    raise NotImplementedError("Can not handle this case")


@dataclass(frozen=False, init=False)
class ExperimentParameterConfigurator:
    _parameters_to_vary: Dict[str, ExperimentParameterToVary]

    def __init__(self, parameters_to_vary: Iterable[ExperimentParameterToVary]):
        self._parameters_to_vary = {
            parameter_to_vary.parameter_name: parameter_to_vary for parameter_to_vary in parameters_to_vary
        }

    def iterator_for_all_parameter_combinations(self) -> Iterable[List[SelectedParameterToChange]]:
        for parameter_values in product(*[value.values for value in self._parameters_to_vary.values()]):
            parameters_with_names = [
                SelectedParameterToChange(
                    pointer_to_location_in_json=self._parameters_to_vary[parameter_name].pointer_to_location_in_json,
                    name_in_json=self._parameters_to_vary[parameter_name].parameter_name,
                    key=key_creator(parameter_value),
                    value=parameter_value,
                    json_file_name=self._parameters_to_vary[parameter_name].json_file_name,
                )
                for parameter_name, parameter_value in zip(self._parameters_to_vary.keys(), parameter_values)
            ]
            yield parameters_with_names
