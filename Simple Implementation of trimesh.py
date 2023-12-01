import trimesh

# Create a box with noise
room_mesh = trimesh.creation.box([10, 2, 1]).permutate.noise(0.4)

# Subdivide the mesh to ensure no edge is longer than a fraction of the overall mesh size
subdivided_mesh = trimesh.Trimesh(*trimesh.remesh.subdivide_to_size(
    vertices=room_mesh.vertices,
    faces=room_mesh.faces,
    max_edge=room_mesh.scale / 5
))

# Center of each subdivided face offset inwards
points = subdivided_mesh.triangles_center + (subdivided_mesh.face_normals * -1e-4)

# Use the original mesh for thickness calculation as it is well-constructed
thickness = trimesh.proximity.thickness(mesh=room_mesh, points=points)

# Create RGBA colors for each subdivided face based on thickness
subdivided_mesh.visual.face_colors = trimesh.visual.interpolate(thickness)

# Visualize the room with thickness information
subdivided_mesh.show()


# # # import trimesh

# # # # Define the vertices of the room
# # # vertices = [    [0, 0, 0], [0, 5, 0], [5, 5, 0], [5, 0, 0],
# # #     [0, 0, 3], [0, 5, 3], [5, 5, 3], [5, 0, 3],
# # # ]

# # # # Define the faces of the room
# # # faces = [    [0, 1, 2], [0, 2, 3],
# # #     [4, 5, 6], [4, 6, 7],
# # #     [0, 4, 1], [1, 4, 5],
# # #     [2, 6, 3], [3, 6, 7],
# # #     [0, 4, 3], [3, 4, 7],
# # #     [1, 5, 2], [2, 5, 6],
# # # ]

# # # # Create a mesh from the vertices and faces
# # # mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# # # # Plot the mesh
# # # mesh.show()

# # import trimesh
# # import numpy as np

# # # Define vertices for each face
# # floor_vertices = np.array([[0,0,0],[0,5,0],[5,5,0],[5,0,0]])
# # ceiling_vertices = floor_vertices + [0,0,5]
# # wall1_vertices = np.array([[0,0,0],[0,0,5],[0,5,5],[0,5,0]])
# # wall2_vertices = wall1_vertices + [5,0,0]
# # wall3_vertices = np.array([[0,5,0],[0,5,5],[5,5,5],[5,5,0]])
# # wall4_vertices = wall3_vertices + [0,0,5]

# # # Create mesh objects for each face
# # floor = trimesh.Trimesh(vertices=floor_vertices, faces=[[0,1,2],[2,3,0]])
# # ceiling = trimesh.Trimesh(vertices=ceiling_vertices, faces=[[0,2,1],[2,0,3]])
# # wall1 = trimesh.Trimesh(vertices=wall1_vertices, faces=[[0,1,2],[2,3,0]])
# # wall2 = trimesh.Trimesh(vertices=wall2_vertices, faces=[[0,2,1],[2,0,3]])
# # wall3 = trimesh.Trimesh(vertices=wall3_vertices, faces=[[0,1,2],[2,3,0]])
# # wall4 = trimesh.Trimesh(vertices=wall4_vertices, faces=[[0,2,1],[2,0,3]])

# # # Combine all faces into one mesh
# # room = ceiling + wall1 + wall2 + wall3 + wall4

# # # Plot the mesh

# # room.show()

# import trimesh
# import numpy as np

# # Define the vertices for the floor and ceiling
# floor_vertices = np.array([[0,0,0],[0,5,0],[5,5,0],[5,0,0]])
# ceiling_vertices = floor_vertices + [0,0,5]

# # Define the vertices for the three walls
# wall1_vertices = np.array([[0,0,0],[0,0,5],[0,5,5],[0,5,0]])
# wall2_vertices = wall1_vertices + [5,0,0]
# wall3_vertices = np.array([[0,5,0],[0,5,5],[5,5,5],[5,5,0]])

# # Create mesh objects for each face
# floor = trimesh.Trimesh(vertices=floor_vertices, faces=[[0,1,2],[2,3,0]])
# ceiling = trimesh.Trimesh(vertices=ceiling_vertices, faces=[[0,2,1],[2,0,3]])
# wall1 = trimesh.Trimesh(vertices=wall1_vertices, faces=[[0,1,2],[2,3,0]])
# wall2 = trimesh.Trimesh(vertices=wall2_vertices, faces=[[0,2,1],[2,0,3]])
# wall3 = trimesh.Trimesh(vertices=wall3_vertices, faces=[[0,1,2],[2,3,0]])

# # Combine all faces into one mesh
# room = ceiling + wall1 + wall2 + wall3 + floor

# # Visualize the room
# room.show()



# import numpy as np
# length = np.random.randint(10,30,1000)
# breadth = np.random.randint(10,30,1000)
# height = np.random.randint(10,30,1000)
# def room_vertices(length, breadth, height):
#     floor_vertices = np.array([[0,0,0],[0,breadth,0],[length,breadth,0],[length,0,0]])
#     ceiling_vertices = floor_vertices + [0,0,height]
#     wall1_vertices = np.array([[0,0,0],[0,0,height],[0,breadth,height],[0,breadth,0]])
#     wall2_vertices = wall1_vertices + [length,0,0]
#     wall3_vertices = np.array([[0,breadth,0],[0,breadth,height],[length,breadth,height],[length,breadth,0]])
#     wall4_vertices = wall3_vertices + [0,0,height]
#     return floor_vertices, ceiling_vertices, wall1_vertices, wall2_vertices, wall3_vertices, wall4_vertices

# call the function for all the values of length,breadth and height.
# for i in range(1000):
#     floor_vertices, ceiling_vertices, wall1_vertices, wall2_vertices, wall3_vertices, wall4_vertices = room_vertices(length[i], breadth[i], height[i])
