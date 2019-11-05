import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa

wav_loc = "audio_wav/subway_with_noise"
src_rate, src_data = wavfile.read(wav_loc)
# src_data = np.concatenate((src_data, np.zeros(src_rate*3)))
src_data = src_data / 32768
wav_loc = "cafe.wav"
noise_rate, noise_data = wavfile.read(wav_loc)
# get some noise to add to the signal
noise_to_add = noise_data[len(src_data) : len(src_data) * 2]
# get a different part of the noise clip for calculating statistics
noise_clip = noise_data[: len(src_data)]
noise_clip = noise_clip / max(noise_to_add)
noise_to_add = noise_to_add / max(noise_to_add)
# apply noise
snr = 1  # signal to noise ratio
audio_clip_cafe = src_data + noise_to_add / snr
noise_clip = noise_clip / snr

print("noise + sound")
fig, ax = plt.subplots(figsize=(20,4))
ax.plot(audio_clip_cafe)
IPython.display.Audio(data=audio_clip_cafe, rate=src_rate)

output = removeNoise(
    audio_clip=audio_clip_cafe,
    noise_clip=noise_clip,
    n_std_thresh=2,
    prop_decrease=0.95,
    visual=True,
)

print("sound")
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 4))
plt.plot(output, color="black")
ax.set_xlim((0, len(output)))
plt.show()
# play back a sample of the song
IPython.display.Audio(data=output, rate=44100)