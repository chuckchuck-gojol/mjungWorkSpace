import noisereduce as nr
import scipy.io.wavfile as wavfile

# load data
rate, data = wavfile.read("audio_wav/subway_with_noise.wav")
# select section of data that is noise
noisy_part = data[10000:15000]
# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)

# n_grad_freq (int): how many frequency channels to smooth over with the mask.
print(reduced_noise.n_grad_freq)

# n_grad_time (int): how many time channels to smooth over with the mask.
print(reduced_noise.n_grad_time)

# n_fft (int): number audio of frames between STFT columns.
print(reduced_noise.n_fft)

# win_length (int): Each frame of audio is windowed by `window()`. The window will be of length `win_length` and then padded with zeros to match `n_fft`..
print(reduced_noise.win_length)

# hop_length (int):number audio of frames between STFT columns.
print(reduced_noise.hop_length)

# n_std_thresh (int): how many standard deviations louder than the mean dB of the noise (at each frequency level) to be considered signal
print(reduced_noise.n_std_thresh)

# prop_decrease (float): To what extent should you decrease noise (1 = all, 0 = none)
print(reduced_noise.prop_decrease)

# pad_clipping (bool): Pad the signals with zeros to ensure that the reconstructed data is equal length to the data
print(reduced_noise.pad_clipping)

# use_tensorflow (bool): Use tensorflow as a backend for convolution and fft to speed up computation
print(reduced_noise.use_tensorflow)

# verbose (bool): Whether to plot the steps of the algorithm
print(reduced_noise.verbose)