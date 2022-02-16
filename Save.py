import os
import Calibration
from ast import literal_eval as make_tuple


def load_saves(x):
    if x == 1:
        file_exist = os.path.exists('save_reloading.txt')
        if file_exist == True:
            with open('save_reloading.txt', 'r', encoding='utf-8') as f:
                coordinates = f.readline()
                return make_tuple(coordinates)
        else:
            print('Saves not found. Starting calibration...')
            coordinates = Calibration.calibration()
            return coordinates
    elif x == 2:
        file_exist = os.path.exists('save_tailoring.txt')
        if file_exist == True:
            with open('save_tailoring.txt', 'r', encoding='utf-8') as f:
                coordinates = f.readline()
                return make_tuple(coordinates)
        else:
            print('Saves not found. Starting calibration...')
            coordinates = Calibration.calibration()
            return coordinates


def save_saves(name, coordinates):
    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        f.write(coordinates)
    print('Saved')
