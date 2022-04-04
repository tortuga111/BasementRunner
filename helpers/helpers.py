import contextlib
import os


@contextlib.contextmanager
def change_back_to_original_wd_afterwards(path_to_switch_to: str) -> None:
    current_wd = os.getcwd()
    try:
        os.chdir(path_to_switch_to)
        yield
    finally:
        os.chdir(current_wd)
