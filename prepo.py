# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/dc_tts
'''

from __future__ import print_function
i = 0
i=+1
print("prepo start loading",i)
from utils_bidon import load_spectrograms
i=+1
print("prepo start loading",i)
import os
i=+1
print("prepo start loading",i)
from data_load import load_data
print("prepo start loading")
import numpy as np
i=+1
print("prepo start loading",i)
import tqdm

print("prepo start loading")
# Load data
fpaths, _, _ = load_data() # list


for fpath in tqdm.tqdm(fpaths):
    fname, mel, mag = load_spectrograms(fpath)
    if not os.path.exists("mels"): os.mkdir("mels")
    if not os.path.exists("mags"): os.mkdir("mags")

    np.save("mels/{}".format(fname.replace("wav", "npy")), mel)
    np.save("mags/{}".format(fname.replace("wav", "npy")), mag)

print("prepo start loaded")