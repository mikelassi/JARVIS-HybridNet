"""
visualization_utils.py
=================
"""

import numpy as np
import cv2


def draw_line(img, line, points2D, img_size, color):
    array_sum = np.sum(np.array(points2D))
    array_has_nan = np.isnan(array_sum)
    if ((not array_has_nan) and int(points2D[line[0]][0]) < img_size[0]-1
            and int(points2D[line[0]][0]) > 0
            and int(points2D[line[1]][0]) < img_size[0]-1
            and int(points2D[line[1]][0]) > 0
            and int(points2D[line[0]][1]) < img_size[1]-1
            and int(points2D[line[0]][1]) > 0
            and int(points2D[line[1]][1]) < img_size[1]-1
            and int(points2D[line[1]][1]) > 0):
        cv2.line(img,
                (int(points2D[line[0]][0]), int(points2D[line[0]][1])),
                (int(points2D[line[1]][0]), int(points2D[line[1]][1])),
                color, 1)


def draw_point(img, point, img_size, color, confidence):
    array_sum = np.sum(np.array(point))
    array_has_nan = np.isnan(array_sum)
    if ((not array_has_nan) and (point[0] < img_size[0]-1
            and point[0] > 0 and point[1] < img_size[1]-1
            and point[1] > 0)):
        thickness = 3
        if confidence < 0.6:
            thickness = 1
        cv2.circle(img, (int(point[0]), int(point[1])),
                3, color, thickness=thickness)
