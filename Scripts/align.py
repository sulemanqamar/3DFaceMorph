import pymeshlab as ml
ms = ml.MeshSet()
ms.load_new_mesh('C:/Users/suleman/Documents/Face1.obj')
target = ms.current_mesh()

ms.load_new_mesh('C:/Users/suleman/Documents/Face1.obj')
source = ms.current_mesh()

ms.apply_filter('compute_matrix_by_mesh_global_alignment',basemesh =1,ogsize=500000,arcthreshold = 0.3,recalcthreshold=0.1,samplenum=2000,mindistabs=10,trgdistabs=0.005,maxiternum=750,samplemode=True,reducefactorperc=0.8,passhifilter=0.75,matchmode=False) 
ms.save_current_mesh('C:/Users/suleman/Documents/AlignedFace.obj')
