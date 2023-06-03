import pymeshlab as ml
ms = ml.MeshSet()
#ms.load_new_mesh('C:/Users/sulem/Documents/T3.obj')
ms.load_new_mesh('C:/Users/sulem/Documents/Pi.obj')

m = ms.current_mesh()
print('input mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')

#Target number of vertex
#TARGET=23686
TARGET=1384
#Estimate number of faces to have 100+10000 vertex using Euler
numFaces = 100 + 2*TARGET

#Simplify the mesh. Only first simplification will be agressive
while (ms.current_mesh().vertex_number() > TARGET):
    ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=numFaces, preservenormal=True)
    print("Decimated to", numFaces, "faces mesh has", ms.current_mesh().vertex_number(), "vertex")
    #Refine our estimation to slowly converge to TARGET vertex number
    numFaces = numFaces - (ms.current_mesh().vertex_number() - TARGET)

m = ms.current_mesh()
print('output mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')
ms.save_current_mesh('C:/Users/sulem/Downloads/output.ply')