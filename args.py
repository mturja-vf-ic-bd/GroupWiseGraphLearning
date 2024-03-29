import numpy as np
import os

class Args:
    n_eig = 0.005  # percent of eigen values to be zero
    eps = 1e-12
    th = 0.01  # Threshold of connectome
    dfw = 1
    sw = 1
    lmw = 1
    lmd = 1
    k = 50
    threshold = 0.0002 # threshold for raw connectomes
    debug = False
    n_iter = 10
    c_dim = (148, 148)  # matrix dimension

    rbf_sigma = 0.01  # spread of rbf kernel
    lambda_m = 1
    beta = np.ones(c_dim) / 3
    mu = 0.5
    r = 2
    intra_r = 0.7
    pro = 1
    base_dir = "/home/turja"
    root_directory = os.path.join(base_dir, "GroupWiseGraphLearning")
    data_directory = os.path.join(root_directory, 'data')
    raw_data_directory = os.path.join(base_dir, "AD-Data")
    data_file = os.path.join(base_dir, "DXData.csv")
    other_file = os.path.join(base_dir, "AD_files")


