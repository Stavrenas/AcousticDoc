# -*- coding: utf-8 -*-
import librosa
import tempfile
import numpy as np
import os
from numpy.random import randn
from scipy.io.wavfile import write

def extract(content):

    mean = [3.81824020e-01,  2.95271863e-01,  2.03439715e+03,
            7.39622100e+02,  1.69879041e+03,  4.49268124e+02,
            3.78944990e+03,  1.35336624e+03,  1.43959306e-01,
            6.77000706e-02,  9.78050864e-02,  8.76225435e-02,
            1.91114794e+01,  8.35261585e+00, -4.09200408e+02,
            1.41061379e+02,  9.18562226e+01,  4.51107273e+01,
            -2.83898654e+01,  3.34076968e+01,  1.90976140e+01,
            2.26401450e+01, -1.93199281e+01,  2.22092267e+01,
            8.42101018e+00,  1.65659652e+01, -1.77248147e+01,
            1.63961620e+01, -5.92881093e+00,  1.26304769e+01,
            -1.21204746e+01,  1.24304585e+01, -4.75891560e+00,
            1.06411759e+01, -2.99432168e+00,  9.82503031e+00,
            -9.08017945e+00,  1.01212797e+01, -6.46301626e-01,
            8.99376583e+00, -7.29094437e+00,  9.15163474e+00,
            -1.48173250e+00,  7.97624013e+00, -5.86998658e+00,
            8.34069706e+00, -3.76675911e+00,  7.41933331e+00,
            -4.36890131e+00,  7.55580744e+00, -3.46954534e+00,
            7.04111226e+00, -2.60242401e+00,  7.13172788e+00,
            2.41889537e-04,  5.02667035e-02, -1.67808248e+00,
            1.36468759e+02,  3.38052807e+00,  8.18505752e+01,
            2.27502778e-02,  2.49989768e+02, -2.31743893e-04,
            1.30959895e-02, -2.79397467e-04,  1.36381371e-02,
            -4.93283194e-02,  8.81596303e-01, -2.06200893e+00,
            2.54289016e+01, -4.02871738e-01,  8.32840298e+00,
            4.31696943e-01,  6.34831387e+00, -5.24370298e-02,
            4.38960900e+00,  2.69090756e-01,  4.23550330e+00,
            -1.14252425e-01,  3.21759355e+00,  1.42693418e-01,
            3.05687112e+00,  2.78274915e-02,  2.49942351e+00,
            7.86736523e-02,  2.35707185e+00,  2.06951422e-02,
            2.05981144e+00, -1.51342985e-02,  1.90194910e+00,
            6.17738790e-02,  1.91439558e+00, -5.81575382e-02,
            1.74975591e+00,  2.83012634e-02,  1.71680714e+00,
            -3.82124507e-02,  1.52045943e+00,  2.34638970e-02,
            1.57631825e+00, -2.09218435e-02,  1.41257331e+00,
            2.39350028e-02,  1.41597673e+00,  1.46135302e-03,
            1.34070061e+00,  1.35657197e-02,  1.35555744e+00]
    std = [1.26867540e-01, 4.87584901e-02, 9.02882804e+02, 4.17804113e+02,
           5.75509887e+02, 2.49979473e+02, 1.64695732e+03, 6.93141029e+02,
           1.10482501e-01, 4.21171445e-02, 1.97755681e-01, 1.49563943e-01,
           3.34167822e+00, 1.73392165e+00, 2.19582288e+02, 6.72193509e+01,
           4.02642363e+01, 2.16301433e+01, 2.95277626e+01, 1.57374265e+01,
           2.01104277e+01, 1.06220071e+01, 2.03906932e+01, 1.03652724e+01,
           1.64191511e+01, 7.76893325e+00, 1.53854116e+01, 7.46187893e+00,
           1.16487746e+01, 5.60986014e+00, 1.05772245e+01, 5.41087249e+00,
           1.01575500e+01, 4.65824512e+00, 8.22259989e+00, 4.20860419e+00,
           8.05968061e+00, 4.14061295e+00, 6.99141584e+00, 3.78834162e+00,
           7.66080339e+00, 3.58552133e+00, 6.21242980e+00, 3.18067103e+00,
           6.66412362e+00, 3.39807024e+00, 5.80403991e+00, 2.89920708e+00,
           5.93806260e+00, 3.01929576e+00, 5.25552877e+00, 2.81248524e+00,
           5.38294998e+00, 2.91508006e+00, 7.26823885e-03, 1.17907006e-02,
           4.50848673e+01, 8.08805849e+01, 2.66625518e+01, 4.67628432e+01,
           8.08305048e+01, 1.40816877e+02, 3.96380451e-03, 8.33756299e-03,
           9.05654507e-03, 2.31364470e-02, 1.14799109e-01, 2.57789199e-01,
           8.80882132e+00, 1.35879336e+01, 2.74284796e+00, 4.28162130e+00,
           1.88262433e+00, 3.26629978e+00, 1.24062882e+00, 2.23885860e+00,
           1.19443648e+00, 2.16291549e+00, 8.89590970e-01, 1.66310780e+00,
           8.64419339e-01, 1.53038796e+00, 6.90237308e-01, 1.26876394e+00,
           6.47119166e-01, 1.14737712e+00, 5.82955649e-01, 1.02387621e+00,
           5.22384284e-01, 9.23238085e-01, 5.38432335e-01, 8.99017721e-01,
           4.83420038e-01, 8.39197143e-01, 4.74773431e-01, 7.71772483e-01,
           4.09447725e-01, 7.03743633e-01, 4.41815870e-01, 7.35482665e-01,
           3.84183882e-01, 6.50595422e-01, 3.83883164e-01, 6.52566018e-01,
           3.64259535e-01, 6.31613433e-01, 3.54388644e-01, 6.46911433e-01]
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

        # for i in range(len(feat)):
        #     feat[i] = (feat[i] - mean[i]) / std[i]
        # feat = np.array(feat, ndmin=2)

    return feat


def zcr(window):
	window2 = np.zeros(len(window))
	window2[1:] = window[0:-1]
	Z = (1/(2*len(window))) * np.sum(np.abs(np.sign(window)-np.sign(window2)))
	return Z

def minimaxscaling(x):
	min_x = np.min(x)
	max_x = np.max(x)
	y = (x-min_x)/(max_x-min_x)
	return y


def zcr_signal(x,Fs,window_length,noverlap):
# zcr_seq = zcr_signal(x,Fs,window_length,noverlap)
# Inputs:
# x: input signal
# Fs: sample rate
# window_length: length of the window
# noverlap: percentage of overlap on windows
#
# Output:
# zcr_seq: zero-crossing sequence
# t_zcr: x-axis of zero-crossing sequence
	N = len(x)
	t = np.linspace(0,(N-1)/Fs,N)
	t = np.array([1000*i for i in t])
	y = (x-np.mean(x))
	y = np.array([i+0.05*randn() for i  in y])

	zcr_seq = []
	for i in range(0, int(N-window_length), int(np.round(window_length - noverlap*window_length))):
		if N - i >= np.round(window_length - noverlap*window_length):
			window = y[i:int(i+window_length-1)]
		else:
			window = y[i:]
	    
		zcr_seq.append(zcr(window))

	zcr_seq = minimaxscaling(zcr_seq)
	t_zcr = np.arange(0,N-window_length,np.round(window_length - noverlap*window_length))
	t_zcr = np.array([1000/Fs*i for i in t_zcr])

	if len(zcr_seq) != len(t_zcr):
		m = np.min([len(zcr_seq),len(t_zcr)])
		t_zcr = t_zcr[:m]
		zcr_seq = zcr_seq[:m]

	return t_zcr, zcr_seq


def cough_detection(zcr_seq, time_step):

	thres = 0.6
	below = np.array([i for i,val in enumerate(zcr_seq) if val<thres])
	below_sec = [(b-1)*time_step for b in below]
	

	diff_below = np.diff(below)
	break_points = [i for i,val in enumerate(diff_below) if val>1]
	break_points.append(int(len(diff_below)))
	break_points = [int(i) for i in break_points]

	break_sec = [(b-1)*time_step for b in below[break_points]]


	t_coughs = np.array([0,0])
	start_cough = below_sec[0]
	for i in range(len(break_sec)):
		if (break_sec[i] + time_step) - start_cough > 250:
			margin = 2
			if start_cough - margin*time_step >= 0:
				t_coughs = np.vstack((t_coughs, np.array([start_cough - margin*time_step, break_sec[i] + margin*time_step]) ))
			else:
				t_coughs = np.vstack((t_coughs, np.array([start_cough - time_step, break_sec[i]+margin*time_step]) ))

			if i != len(break_sec)-1:
				start_cough = below_sec[break_points[i]+1];


	return t_coughs[1:, :]



def cough_save(content,name):

    with tempfile.NamedTemporaryFile() as temp_file:
        directory = os.environ["HOME"]
        temp_file.write(content)
        filename = temp_file.name

        x, Fs = librosa.load(filename)
        noverlap = 0.3
        nsec = 0.1
        window_length = np.round(nsec*Fs)
        time_step = np.round(window_length - noverlap*window_length)/Fs*1000

        _, zcr_seq = zcr_signal(x,Fs,window_length,noverlap)
        t_coughs = cough_detection(zcr_seq, time_step)
        newFilename = "None"
        for i in range(t_coughs.shape[0]):
            start_cough = int(np.round(t_coughs[i,0]*Fs/1000))
            end_cough = int(np.round(t_coughs[i,1]*Fs/1000))

            if end_cough > len(x)-1:
                end_cough = len(x)-1


            samples_cough = range(start_cough,end_cough+1)

            distinct_cough = x[samples_cough]

            newFilename = directory +"/" name+"_"+str(i)+".wav"
            write(newFilename, Fs, distinct_cough.astype(np.float32))
            files = i

    return newFilename