import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import IPython.display as ipd

# De-noise a chromagram by non-local median filtering.
# By default this would use euclidean distance to select neighbors,
# but this can be overridden directly by setting the `metric` parameter.

y, sr = librosa.load("audio_wav/subway_with_noise.wav",
                     offset=30, duration=10)

chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

chroma_med = librosa.decompose.nn_filter(chroma,
                                         aggregate=np.median,
                                         metric='cosine')

print(chroma_med)
# To use non-local means, provide an affinity matrix and `aggregate=np.average`.

rec = librosa.segment.recurrence_matrix(chroma, mode='affinity',
                                        metric='cosine', sparse=True)
chroma_nlm = librosa.decompose.nn_filter(chroma, rec=rec,
                                         aggregate=np.average)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.subplot(5, 1, 1)
librosa.display.specshow(chroma, y_axis='chroma')
librosa.output(chroma) # load a local WAV file

plt.colorbar()
plt.title('Unfiltered')
plt.subplot(5, 1, 2)
librosa.display.specshow(chroma_med, y_axis='chroma')
librosa.output(chroma_med) # load a local WAV file

plt.colorbar()
plt.title('Median-filtered')
plt.subplot(5, 1, 3)
librosa.display.specshow(chroma_nlm, y_axis='chroma')
librosa.output(chroma_nlm) # load a local WAV file

plt.colorbar()
plt.title('Non-local means')
plt.subplot(5, 1, 4)
librosa.display.specshow(chroma - chroma_med,
                         y_axis='chroma')
librosa.output(chroma - chroma_med) # load a local WAV file

plt.colorbar()
plt.title('Original - median')
plt.subplot(5, 1, 5)
librosa.display.specshow(chroma - chroma_nlm,
                         y_axis='chroma', x_axis='time')
librosa.output(chroma - chroma_nlm)

plt.colorbar()
plt.title('Original - NLM')
plt.tight_layout()
plt.show()
