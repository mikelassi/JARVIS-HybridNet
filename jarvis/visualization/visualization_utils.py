"""
visualization_utils.py
=================
"""

import numpy as np
import cv2


def get_colors_and_lines(skeletonPreset):
    colors = []
    line_idxs = []
    if skeletonPreset == "Hand":
        colors = ['b', 'b','b','b', 'r', 'r', 'r', 'r', 'g', 'g','g','g', 'y', 'y', 'y','y', 'purple', 'purple','purple', 'purple', 'grey', 'orange', 'orange']
        line_idxs = [[0,1], [1,2], [2,3], [4,5], [5,6], [6,7],
                     [8,9], [9,10], [10,11], [12,13], [13,14],
                     [14,15], [16,17], [17,18], [18,19],
                     [15,18], [15,19], [15,11], [11,7], [7,3],
                     [3,21], [21,22], [19,22]]
    elif skeletonPreset == "HumanBody":
        colors = ['b', 'b','b','b', 'gray', 'r', 'r', 'r', 'r', 'g', 'g','g','g', 'gray', 'y', 'y', 'y','y', 'purple', 'purple','purple', 'purple']
        line_idxs = [[4,5], [5,6], [6,7], [7,8], [4,9], [9,10],
                     [10,11], [11,12], [4,13], [13,14], [14,15],
                     [15,16], [16,17], [13,18], [18,19],
                     [19,20], [20,21]]
    elif skeletonPreset == "MonkeyBody":
        colors = ['b', 'b', 'gray','gray', 'r', 'r', 'r','g','g','g','y', 'y','y', 'purple', 'purple','purple']
        line_idxs = [[2,4], [2,10], [4,5], [5,6], [3,7], [7,8], [8,9],
                      [3,2], [10,11], [11,12], [13,14],
                      [14,15], [3,13]]
    elif skeletonPreset == "RodentBody":
        colors = ['r', 'r','r', 'gray', 'b', 'b', 'b', 'b', 'g', 'g','g','g', 'gray', 'y', 'y','y', 'purple', 'purple','purple', 'orange', 'orange', 'orange']
        line_idxs = [[0,1], [0,2], [1,2],[1,3], [2,3], [3,7],
                     [7,6], [6,5], [5,4], [3,11], [11,10],
                     [10,9], [9,8], [3,12], [12,15], [15,14],
                     [14,13], [12,18], [18,17], [17,16], [12,19]]

    return colors, line_idxs
