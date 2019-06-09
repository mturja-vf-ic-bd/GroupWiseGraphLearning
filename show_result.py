from utils.readFile import *
from utils.helper import *
from plot_functions import plot_matrix_all
from args import Args
import json
from matplotlib import pyplot as plt
from Evaluation.variation_of_information import sort_connectomes_by_modularity


def show_result(connectome_list, smoothed_connectomes, plot_all=False):
    if plot_all:
        plot_matrix_all(connectome_list, fname="raw")
        plot_matrix_all(smoothed_connectomes, fname="intrinsic")


if __name__ == '__main__':
    sub = 'sub_1'
    data_dir = os.path.join(os.getcwd(), 'data')
    connectomes, smoothed_connectomes = readSubjectFiles(sub, method="row")
    N = connectomes[0].shape[0]

    c_i = None
    s_i = None

    for t in range(0, len(connectomes)):
        connectomes[t], c_i = sort_connectomes_by_modularity(connectomes[t], c_i)
        smoothed_connectomes[t], s_i = sort_connectomes_by_modularity(smoothed_connectomes[t], s_i)
        smoothed_connectomes[t] = rescale_sm_mat_to_raw(connectomes[t], smoothed_connectomes[t])

    show_result(connectomes, smoothed_connectomes, plot_all=True)
