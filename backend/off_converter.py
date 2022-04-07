import os
from glob import glob
import random
import json
from tqdm import tqdm
import numpy as np


class Vertex(object):
    """
    Vertex class
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)

    def __repr__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)


class Face(object):
    """
    Face class
    """

    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def __eq__(self, other):
        return self.v1 == other.v1 and self.v2 == other.v2 and self.v3 == other.v3

    def __str__(self):
        return str(self.v1) + ' ' + str(self.v2) + ' ' + str(self.v3)

    def __repr__(self):
        return str(self.v1) + ' ' + str(self.v2) + ' ' + str(self.v3)


def get_offs(path):
    """
    Get all .off files in a directory
    """
    return glob(os.path.join(path, '*.off'))


def read_off(filename):
    """
    Read a .off file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def off_process(off_obj):
    """
    Process a .off file
    """
    off_obj = [line.replace('\n', '') for line in off_obj]
    nums = off_obj[1].split(' ')
    num_vertices = int(nums[0])
    num_faces = int(nums[1])
    num_edges = int(nums[2])
    off_obj_p = off_obj[2:]
    # get vertices
    vertices_raw = off_obj_p[:num_vertices]
    vertices = [x.split(' ') for x in vertices_raw]
    vertices = [x for x in vertices if x != ['']]
    vertices = [x for x in vertices if x != []]
    vertices = [[float(x) for x in y] for y in vertices]
    vertices_instances = [Vertex(x[0], x[1], x[2]) for x in vertices]
    # get faces
    faces_raw = off_obj_p[num_vertices:num_vertices+num_faces]
    faces = [x.split(' ') for x in faces_raw]
    faces = [x for x in faces if x != ['']]
    faces = [x for x in faces if x != []]
    faces = [[int(x) for x in y] for y in faces]
    faces = [x[1:4] for x in faces]
    faces_instances = [Face(x[0], x[1], x[2]) for x in faces]
    result = {
        "num_vertices": num_vertices,
        "num_faces": num_faces,
        "point_set": vertices,
        "face_set": faces,
        "point_set_instances": vertices_instances,
        "faces_instances": faces_instances
    }
    return result


def off_sparse_process(off_obj_raw, max_lack_part=90, min_distance=0.19, random_param=0.88):
    """
    Random sparse process a .off object
    """
    off_obj = off_obj_raw["point_set_instances"].copy()
    num_part_lack = random.randint(70, max_lack_part)
    center_points = []
    for i in range(num_part_lack):
        vertex_idx = random.randint(0, len(off_obj)-1)
        center_points.append(off_obj[vertex_idx])

    for p_c in center_points:
        for i, p in enumerate(off_obj):
            if distance_cal(p, p_c) < min_distance and random.random() < random_param:
                del off_obj[i]

    off_obj_raw["sparsed_point_set_instances"] = off_obj
    return off_obj_raw


def distance_cal(point1, point2):
    """
    Calculate the distance between two points
    """
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)**0.5


def save_as_json(off_obj, save_name):
    """
    Save a .off file as a json file
    """
    with open(save_name, 'w') as f:
        f.write(json.dumps({"point_set": off_obj["point_set"]}))


def save_sparse_as_json(off_obj, save_name):
    """
    Save a sparse .off file as a json file
    """
    vertices = []
    for p in off_obj["sparsed_point_set_instances"]:
        vertices.append([p.x, p.y, p.z])
    with open(save_name, 'w') as f:
        f.write(json.dumps(
            {"point_set": vertices}))


def save_as_obj(off_obj, filename):
    """
    Save a .obj file
    """
    # write to .obj file
    with open(filename, 'w') as f:
        # f.write('# File type: ASCII OBJ\n')
        for x in off_obj["point_set"]:
            f.write('v ' + str(x[0]) + ' ' +
                    str(x[1]) + ' ' + str(x[2]) + '\n')
        for x in off_obj["face_set"]:
            f.write('f ' + str(x[0]+1) + ' ' +
                    str(x[1]+1) + ' ' + str(x[2]+1) + '\n')
        # for idx in range(int(off_obj["num_vertices"])):
        #     f.write('p ' + str(idx+1) + '\n')


def save_sparse_as_obj(off_obj, filename):
    """
    Save a .obj file
    """
    # write to .obj file
    with open(filename, 'w') as f:
        for p in off_obj["sparsed_point_set_instances"]:
            f.write('v ' + str(p.x) + ' ' +
                    str(p.y) + ' ' + str(p.z) + '\n')
        # for x in off_obj["point_set"]:
        #     f.write('v ' + str(x[0]) + ' ' +
        #             str(x[1]) + ' ' + str(x[2]) + '\n')
        # for x in off_obj["face_set"]:
        #     f.write('f ' + str(x[0]+1) + ' ' +
        #             str(x[1]+1) + ' ' + str(x[2]+1) + '\n')


if __name__ == '__main__':
    off_files = get_offs('/home/du/iwaitPro/SketchPC/frontend/static/threeDs')
    # off_files = get_offs('/home/du/iwaitPro/SketchPC/frontend/static/test')
    for off_file in tqdm(off_files, desc='Converting...'):
        # for off_file in off_files:
        off_obj = read_off(off_file)
        # save off as json
        off_obj_processed = off_process(off_obj)
        # save off as sparsed json
        off_obj_processed_sparse = off_sparse_process(off_obj_processed)
        save_name = off_file.replace('.off', '.json')
        save_name_obj = off_file.replace('.off', '.obj')
        save_name_sparse = off_file.replace('.off', '_sparse.json')
        save_name_sparse_obj = off_file.replace('.off', '_sparse.obj')
        save_as_json(off_obj_processed, save_name)
        # print('{} saved'.format(save_name))
        save_sparse_as_json(off_obj_processed_sparse, save_name_sparse)
        # print('{} saved'.format(save_name_sparse))
        save_as_obj(off_obj_processed, save_name_obj)
        save_sparse_as_obj(off_obj_processed_sparse, save_name_sparse_obj)
        # print('Converted ' + off_file + ' to ' +
        #       off_file.replace('.off', '.obj'))
    print('Done')
