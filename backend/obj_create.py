import os
import meshio
import pygalmesh

g = os.walk('/home/du/iwaitPro/SketchPC/frontend/static/delete')

for path, dir_list, file_list in g:
    for file_name in file_list:
        if os.path.splitext(file_name)[1] == '.off':
            print(os.path.splitext(file_name)[0])
            print(file_name)
            offPath = path+'/'+file_name
            print(offPath)
            goalPath = path+'/'+os.path.splitext(file_name)[0]+'.obj'
            print(goalPath)
            mesh = pygalmesh.remesh_surface(
                offPath,
                max_edge_size_at_feature_edges=0.025,
                min_facet_angle=25,
                max_radius_surface_delaunay_ball=0.1,
                max_facet_distance=0.001,
                verbose=False)
            meshio.write(goalPath, mesh)
