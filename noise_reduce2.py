import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io
# %matplotlib inline

url = "audio_wav/subway_with_nosie.wav"
# response = urllib.request.urlopen(url)
data, rate = sf.read(url)
data = data

noise_reduced = nr.reduce_noise(audio_clip=audio_clip_band_limited, noise_clip=noise_clip, verbose=True)

