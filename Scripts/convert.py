import pymeshlab as ml
ms = ml.MeshSet()
ms.load_new_mesh('C:/Users/suleman/Documents/Face1.obj')
target = ms.current_mesh()

ms.load_new_mesh('C:/Users/suleman/Documents/Face2.obj')
source = ms.current_mesh()

ms.apply_filter('compute_coord_linear_morphing',targetmesh=0, percentmorph=40) 
ms.save_current_mesh('C:/Users/suleman/Documents/NewFace.obj')
