
import numpy as np


def eucledian_distance(point_1=np.array([0, 0]), point_2=np.array([1, 1])):
    # if len(point_1) == len(point_2):
    return np.linalg.norm(point_1 - point_2)
    # print('sizes of point_1 and point_2 arrays do not match')


def calculate_coordinate(x1, y1, x2, y2):
    return np.array([(x1 + x2) / 2, (y1 + y2) / 2])


def create_lower_matrix(size):
    lower = np.ones((size, size))
    lower[np.tril_indices(size, 0)] = 0
    return lower


def get_avg_eucledian_dist(doc_word_coords, tagged_vals_coords):
    return np.average([eucledian_distance(doc_word_coords, tagged_val) for tagged_val in tagged_vals_coords])


c = create_lower_matrix(5)
print(c)
