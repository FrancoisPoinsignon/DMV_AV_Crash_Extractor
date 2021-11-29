from PIL import Image
import numpy as np

from src.box_locations import *


def analyse_image(info_dict, image_name):

    image = Image.open('images/' + image_name)
    image_array = np.asarray(image)
    info_type = list(info_dict.keys())

    info_dict['crash'].append(image_name.split('.')[0])
    info_dict['car'].append(1)

    for k in range(len(car1_col1)):
        info_dict[info_type[k+2]].append(is_checked(image_array, car1_col1[k]))
    for k in range(len(car1_col2)):
        info_dict[info_type[k+26]].append(is_checked(image_array, car1_col2[k]))

    info_dict['crash'].append(image_name.split('.')[0])
    info_dict['car'].append(2)

    for k in range(len(car2_col1)):
        info_dict[info_type[k + 2]].append(is_checked(image_array, car2_col1[k]))
    for k in range(len(car2_col2)):
        info_dict[info_type[k + 26]].append(is_checked(image_array, car2_col2[k]))


def is_checked(image, box):
    color = np.mean(image[box[2]:box[3], box[0]:box[1], 0])
    if color < 230:
        return True
    return False
