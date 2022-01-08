# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 23:29:15 2022

@author: user
"""
import librosa
import tempfile
import numpy as np


def extract(content):
    feat = []

    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(content)
        filename = temp_file.name

        y, sr = librosa.load(filename, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        feat.append(np.mean(chroma_stft))
        feat.append(np.std(chroma_stft))
        chroma_delta = librosa.feature.delta(chroma_stft)
        feat.append(np.mean(chroma_delta))
        feat.append(np.std(chroma_delta))

        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        feat.append(np.mean(spec_cent))
        feat.append(np.std(spec_cent))
        cent_delta = librosa.feature.delta(spec_cent)
        feat.append(np.mean(cent_delta))
        feat.append(np.std(cent_delta))

        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        feat.append(np.mean(spec_bw))
        feat.append(np.std(spec_bw))
        bw_delta = librosa.feature.delta(spec_bw)
        feat.append(np.mean(bw_delta))
        feat.append(np.std(bw_delta))

        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        feat.append(np.mean(rolloff))
        feat.append(np.std(rolloff))
        rolloff_delta = librosa.feature.delta(rolloff)
        feat.append(np.mean(rolloff_delta))
        feat.append(np.std(rolloff_delta))

        zcr = librosa.feature.zero_crossing_rate(y)
        feat.append(np.mean(zcr))
        feat.append(np.std(zcr))
        zcr_delta = librosa.feature.delta(zcr)
        feat.append(np.mean(zcr_delta))
        feat.append(np.std(zcr_delta))

        spec_flat = librosa.feature.spectral_flatness(y=y)
        feat.append(np.mean(spec_flat))
        feat.append(np.std(spec_flat))
        flat_delta = librosa.feature.delta(spec_flat)
        feat.append(np.mean(flat_delta))
        feat.append(np.std(flat_delta))

        spec_contr = librosa.feature.spectral_contrast(y=y, sr=sr)
        feat.append(np.mean(spec_contr))
        feat.append(np.std(spec_contr))
        contr_delta = librosa.feature.delta(spec_contr)
        feat.append(np.mean(contr_delta))
        feat.append(np.std(contr_delta))

        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        mfcc_delta = librosa.feature.delta(mfcc)

        for e in mfcc:
            feat.append(np.mean(e))
            feat.append(np.std(e))

        for e in mfcc_delta:
            feat.append(np.mean(e))
            feat.append(np.std(e))
        # feat = np.array(feat, ndmin=2)

    return feat
