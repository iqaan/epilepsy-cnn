import numpy as np
from os import listdir
from os.path import isfile, join

def read_raw_dataset():
    
    """
    Returns a dictionary `raw_dataset` which contains following keys pairs.
    A, B, C, D, and F with values as 2D numpy array of shape (m, n).
    
    m = no. of training examples in each set
    n - no. of data points in time series
    """
    
    # Directory names are saved as F, O, N, etc.
    # And set names are processed as A, B, C, etc.
    mapping_set_to_dir = {
        'A': (0,'Z'),
        'B': (1,'O'),
        'C': (2,'N'),
        'D': (3,'F'),
        'E': (4,'S')
    }

    file_lists = []
    
    # get the list of files for each set
    # 1 file corresponds to 1 training example
    for s,d in mapping_set_to_dir.items():
        file_lists.insert(d[0], [f for f in listdir(d[1]) if isfile(join(d[1], f))])
    
    raw_dataset = { }

    # loop over all sets
    for s,d in mapping_set_to_dir.items():

        # loop over every file (training example) in each set
        for f in file_lists[d[0]]:
            
            # read the time series data
            curr_example = np.loadtxt(join(d[1], f))

            # create a key in the raw_database dict in case it doesn't exist already
            # otherwise just append the new example in the 2D array
            if (s in raw_dataset):
                raw_dataset[s] = np.append(raw_dataset[s], [curr_example], axis=0)
            else:
                raw_dataset[s] = np.array([curr_example])
    
    return raw_dataset