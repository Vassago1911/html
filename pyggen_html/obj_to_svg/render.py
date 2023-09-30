#todo: n 3d kd system in 2d projizieren, mit n paar standardwahlen geht da was
# obj to svg waere halt schon standardig :D
import imageio.v3 as iio
import numpy as np

xtra_d = 32

A = np.zeros((xtra_d,256,256,3),dtype=int)