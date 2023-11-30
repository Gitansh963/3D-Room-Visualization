# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:37:48 2023

@author: gitan
"""


# ---(Wed Feb  1 21:43:57 2023)---

import numpy as np
from mayavi import mlab


def room_vertices(length, breadth, height):
    floor_vertices = np.array(
        [[0, 0, 0], [0, breadth, 0], [length, breadth, 0], [length, 0, 0]])
    ceiling_vertices = floor_vertices + [0, 0, height]
    wall1_vertices = np.array(
        [[0, 0, 0], [0, 0, height], [0, breadth, height], [0, breadth, 0]])
    wall2_vertices = wall1_vertices + [length, 0, 0]
    wall3_vertices = np.array([[0, breadth, 0], [0, breadth, height], [
                              length, breadth, height], [length, breadth, 0]])
    wall4_vertices = wall3_vertices + [0, 0, height]

    return floor_vertices, ceiling_vertices, wall1_vertices, wall2_vertices, wall3_vertices, wall4_vertices


length = 10
breadth = 20
height = 30

floor_vertices, ceiling_vertices, wall1_vertices, wall2_vertices, wall3_vertices, wall4_vertices = room_vertices(
    length, breadth, height)

mlab.figure()
mlab.triangular_mesh(floor_vertices[:, 0], floor_vertices[:, 1], floor_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.triangular_mesh(ceiling_vertices[:, 0], ceiling_vertices[:, 1], ceiling_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.triangular_mesh(wall1_vertices[:, 0], wall1_vertices[:, 1], wall1_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.triangular_mesh(wall2_vertices[:, 0], wall2_vertices[:, 1], wall2_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.triangular_mesh(wall3_vertices[:, 0], wall3_vertices[:, 1], wall3_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.triangular_mesh(wall4_vertices[:, 0], wall4_vertices[:, 1], wall4_vertices[:, 2],
                     [(0, 1, 2), (0, 2, 3)], color=(0.5, 0.5, 0.5))
mlab.show()
