# 3D Room Visualization

This repository contains two Python scripts that generate 3D visualizations of a room. One script uses the `mayavi` library and the other uses the `trimesh` library.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The script requires the following Python libraries:

- numpy
- mayavi
- trimesh

You can install these libraries using pip:

```bash
pip install numpy
```

```bash
pip install mayavi
```
```bash
pip install trimesh
```

##Usage

#Mayavi Script
The Mayavi script defines a function room_vertices(length, breadth, height) that calculates the vertices for the floor, ceiling, and walls of a room given its dimensions.

The length, breadth, and height variables define the dimensions of the room. You can modify these variables to visualize a room of different dimensions.

The script then uses mayavi to generate a 3D triangular mesh for each component of the room and displays the 3D visualization.

#Trimesh Script
The Trimesh script first creates a box with noise to represent the room. It then subdivides the mesh to ensure no edge is longer than a fraction of the overall mesh size.

The center of each subdivided face is offset inwards, and the thickness of the mesh at these points is calculated using the original mesh.

RGBA colors are then created for each subdivided face based on the thickness, and the room is visualized with this thickness information.

## Authors

- Gitansh Mittal
