import csv
import os.path

import h5py
import numpy as np

from helpers.helpers import change_back_to_original_wd_afterwards

__node_string_folder_name = "node_string_data"


def extract_node_string_information(path_to_h5: str, path_to_write_results_in: str) -> str:
    raise NotImplementedError("this does not work")
    h5_file = h5py.File(path_to_h5, "r")
    node_string_0 = h5_file["/RESULTS/NodeStrg/StateVar/"]
    data0 = list(node_string_0)
    print(data0)
    row_name = zip(data0)
    # initialize the array for final output 1
    node_strings = np.zeros(shape=(0, 10))
    # find the number of stringdef in the domain
    b3 = node_string_0.get(data0[0])
    df = len(b3)
    # initialize the array for discharge output
    column = np.empty(shape=(0, df))
    # loop to gather the outputs
    for x in range(len(node_string_0)):
        # for the discharge at each stringdef
        column0 = [i[1] for i in node_string_0.get(data0[x])]
        column = np.append(column, [column0], axis=0)
        # the timestamps
        # all the outputs of the stringdef
        node_strings = np.append(node_strings, node_string_0.get(data0[x]), axis=0)
    # write the csv documents
    with change_back_to_original_wd_afterwards(path_to_write_results_in):
        if not os.path.exists(__node_string_folder_name):
            os.mkdir(__node_string_folder_name)
        write_results_csv(node_strings)
        write_discharge_csv(column)
        write_timestamps_csv(row_name)
    return path_to_write_results_in


def write_results_csv(node_strings: np.array) -> None:
    # csv with all the available output, without specification on the output time and
    # the stringdef name (to be added in a further development)
    with open(os.path.join(__node_string_folder_name, "results.csv"), "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "Mean wse",
                "Discharge",
                "Wetted area",
                "Mean bottom elevation",
                "Reference elevation",
                "Wetted geometric length",
                "Total water volume stored in cells",
                "Total cells conveyance",
                "Morphological flux",
                "Bedload transport",
            ]
        )
        writer.writerows(node_strings)


def write_discharge_csv(column) -> None:
    with open(os.path.join(__node_string_folder_name, "Discharge.csv"), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(column)


def write_timestamps_csv(row_names) -> None:
    with open(os.path.join(__node_string_folder_name, "Timestamps.csv"), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in row_names:
            writer.writerow(row)
