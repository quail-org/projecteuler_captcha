from PIL import Image
import os
import numpy as np

dir = "../data_gathering/captchas/"

fnames = np.sort([dir + f for f in os.listdir(dir)])


