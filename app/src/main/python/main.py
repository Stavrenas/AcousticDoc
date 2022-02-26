# -*- coding: utf-8 -*-
import librosa
import tempfile
import numpy as np
from scipy import stats
from com.chaquo.python import Python
from numpy.random import randn
from scipy.io.wavfile import write

def extract2(content):

    mean = [
        3.81824020e-01,  2.95271863e-01,  2.03439715e+03,
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

def extract(content):

    with tempfile.NamedTemporaryFile() as temp_file:

        mean = [ 3.81824020e-01,2.95271863e-01,8.95628637e-02,7.38009762e-01,
                -3.58242096e-01,2.03439715e+03,7.39622100e+02,7.21601127e+05,
                3.90443993e-01,3.44967554e-01,1.69879041e+03,4.49268124e+02,
                2.64331584e+05,1.04771578e-01,1.11513550e-01,3.78944990e+03,
                1.35336624e+03,2.31204466e+06,3.17416870e-02,6.83318707e-02,
                1.43959306e-01,6.77000706e-02,6.35715342e-03,3.32542521e-01,
                5.29211755e-02,9.78050864e-02,8.76225435e-02,3.00470833e-02,
                2.00087882e+00,6.24510789e+00,1.91114794e+01,8.35261585e+00,
                7.27726758e+01,1.21178327e+00,1.42115469e+00,-4.09200408e+02,
                1.41061379e+02,2.44167538e+04,1.25364925e-03,-6.96187646e-01,
                9.18562226e+01,4.51107273e+01,2.50284081e+03,-9.90902380e-02,
                -5.17102649e-01,-2.83898654e+01,3.34076968e+01,1.36374079e+03,
                -1.00348072e-02,-4.70331975e-01,1.90976140e+01,2.26401450e+01,
                6.25403200e+02,1.66829830e-01,-1.89324083e-01,-1.93199281e+01,
                2.22092267e+01,6.00688626e+02,-9.13490452e-02,-3.44091686e-01,
                8.42101018e+00,1.65659652e+01,3.34787526e+02,1.45899557e-02,
                -1.80552900e-01,-1.77248147e+01,1.63961620e+01,3.24513764e+02,
                -9.49819412e-02,-3.62054466e-01,-5.92881093e+00,1.26304769e+01,
                1.90999476e+02,-1.27468683e-01,-1.07528939e-01,-1.21204746e+01,
                1.24304585e+01,1.83793840e+02,-1.22588207e-01,-2.95767723e-01,
                -4.75891560e+00,1.06411759e+01,1.34933872e+02,-5.58600734e-02,
                -5.75782335e-02,-2.99432168e+00,9.82503031e+00,1.14243570e+02,
                5.27635785e-03,8.44075899e-03,-9.08017945e+00,1.01212797e+01,
                1.19584978e+02,-1.10672200e-01,-2.10788545e-01,-6.46301626e-01,
                8.99376583e+00,9.52393559e+01,2.23006988e-02,1.07848652e-02,
                -7.29094437e+00,9.15163474e+00,9.66083817e+01,-6.97325432e-02,
                -1.85108212e-01,-1.48173250e+00,7.97624013e+00,7.37370748e+01,
                1.96541707e-02,2.49612568e-02,-5.86998658e+00,8.34069706e+00,
                8.11141089e+01,-1.02519952e-01,-1.70718566e-01,-3.76675911e+00,
                7.41933331e+00,6.34519084e+01,-7.70704626e-02,1.10944907e-02,
                -4.36890131e+00,7.55580744e+00,6.62063729e+01,-7.57737443e-02,
                -7.87250252e-02,-3.46954534e+00,7.04111226e+00,5.74873351e+01,
                -4.75868081e-02,3.84784198e-02,-2.60242401e+00,7.13172788e+00,
                5.93592343e+01,-5.66760651e-02,2.35572966e-02,2.41889537e-04,
                5.02667035e-02,2.66576210e-03,-1.61446444e-02,1.81275190e-01,
                -1.67808248e+00,1.36468759e+02,2.51653913e+04,-3.04775469e-02,
                -3.52094111e-01,3.38052807e+00,8.18505752e+01,8.88628017e+03,
                -2.53784615e-03,-2.75802397e-01,2.27502778e-02,2.49989768e+02,
                8.23242770e+04,-2.53422142e-02,-3.37828023e-01,-2.31743893e-04,
                1.30959895e-02,2.41019896e-04,-2.39845019e-02,-3.37799305e-01,
                -2.79397467e-04,1.36381371e-02,7.21293962e-04,4.59754122e-02,
                8.42823311e-01,-4.93283194e-02,8.81596303e-01,8.43667312e-01,
                -1.59721631e-01,2.40920875e+00,-2.06200893e+00,2.54289016e+01,
                8.31260974e+02,4.52229428e-01,-1.88292533e-01,-4.02871738e-01,
                8.32840298e+00,8.76945772e+01,1.26473088e-01,-3.78801176e-01,
                4.31696943e-01,6.34831387e+00,5.09698033e+01,-9.34551066e-02,
                -4.61262635e-01,-5.24370298e-02,4.38960900e+00,2.42811551e+01,
                1.05495361e-01,-3.53450441e-01,2.69090756e-01,4.23550330e+00,
                2.26176917e+01,-1.14221771e-01,-3.86275196e-01,-1.14252425e-01,
                3.21759355e+00,1.31188358e+01,7.51916152e-02,-3.63279061e-01,
                1.42693418e-01,3.05687112e+00,1.16865484e+01,-9.23723346e-02,
                -3.76007205e-01,2.78274915e-02,2.49942351e+00,7.85687982e+00,
                3.09439748e-02,-4.33717270e-01,7.86736523e-02,2.35707185e+00,
                6.87226195e+00,-6.02876969e-02,-4.10593710e-01,2.06951422e-02,
                2.05981144e+00,5.29114566e+00,9.79679785e-03,-4.15257635e-01,
                -1.51342985e-02,1.90194910e+00,4.46977895e+00,-1.14982989e-02,
                -3.90218567e-01,6.17738790e-02,1.91439558e+00,4.47314331e+00,
                -1.23453928e-02,-4.22456651e-01,-5.81575382e-02,1.74975591e+00,
                3.76589759e+00,-7.09779598e-03,-4.06920122e-01,2.83012634e-02,
                1.71680714e+00,3.54305952e+00,-3.19890941e-02,-4.05391157e-01,
                -3.82124507e-02,1.52045943e+00,2.80705197e+00,-1.69214565e-02,
                -3.89279144e-01,2.34638970e-02,1.57631825e+00,3.02571398e+00,
                -3.99328101e-02,-3.76308883e-01,-2.09218435e-02,1.41257331e+00,
                2.41863775e+00,-2.97321488e-03,-3.82623649e-01,2.39350028e-02,
                1.41597673e+00,2.43083250e+00,-6.09033918e-02,-3.60743984e-01,
                1.46135302e-03,1.34070061e+00,2.19641367e+00,-4.37404340e-02,
                -3.68727048e-01,1.35657197e-02,1.35555744e+00,2.25603038e+00,
                -2.46997156e-02,-3.59059857e-01]


        std = [3.81824020e-01,2.95271863e-01,8.95628637e-02,7.38009762e-01,
                -3.58242096e-01,2.03439715e+03,7.39622100e+02,7.21601127e+05,
                3.90443993e-01,3.44967554e-01,1.69879041e+03,4.49268124e+02,
                2.64331584e+05,1.04771578e-01,1.11513550e-01,3.78944990e+03,
                1.35336624e+03,2.31204466e+06,3.17416870e-02,6.83318707e-02,
                1.43959306e-01,6.77000706e-02,6.35715342e-03,3.32542521e-01,
                5.29211755e-02,9.78050864e-02,8.76225435e-02,3.00470833e-02,
                2.00087882e+00,6.24510789e+00,1.91114794e+01,8.35261585e+00,
                7.27726758e+01,1.21178327e+00,1.42115469e+00,-4.09200408e+02,
                1.41061379e+02,2.44167538e+04,1.25364925e-03,-6.96187646e-01,
                9.18562226e+01,4.51107273e+01,2.50284081e+03,-9.90902380e-02,
                -5.17102649e-01,-2.83898654e+01,3.34076968e+01,1.36374079e+03,
                -1.00348072e-02,-4.70331975e-01,1.90976140e+01,2.26401450e+01,
                6.25403200e+02,1.66829830e-01,-1.89324083e-01,-1.93199281e+01,
                2.22092267e+01,6.00688626e+02,-9.13490452e-02,-3.44091686e-01,
                8.42101018e+00,1.65659652e+01,3.34787526e+02,1.45899557e-02,
                -1.80552900e-01,-1.77248147e+01,1.63961620e+01,3.24513764e+02,
                -9.49819412e-02,-3.62054466e-01,-5.92881093e+00,1.26304769e+01,
                1.90999476e+02,-1.27468683e-01,-1.07528939e-01,-1.21204746e+01,
                1.24304585e+01,1.83793840e+02,-1.22588207e-01,-2.95767723e-01,
                -4.75891560e+00,1.06411759e+01,1.34933872e+02,-5.58600734e-02,
                -5.75782335e-02,-2.99432168e+00,9.82503031e+00,1.14243570e+02,
                5.27635785e-03,8.44075899e-03,-9.08017945e+00,1.01212797e+01,
                1.19584978e+02,-1.10672200e-01,-2.10788545e-01,-6.46301626e-01,
                8.99376583e+00,9.52393559e+01,2.23006988e-02,1.07848652e-02,
                -7.29094437e+00,9.15163474e+00,9.66083817e+01,-6.97325432e-02,
                -1.85108212e-01,-1.48173250e+00,7.97624013e+00,7.37370748e+01,
                1.96541707e-02,2.49612568e-02,-5.86998658e+00,8.34069706e+00,
                8.11141089e+01,-1.02519952e-01,-1.70718566e-01,-3.76675911e+00,
                7.41933331e+00,6.34519084e+01,-7.70704626e-02,1.10944907e-02,
                -4.36890131e+00,7.55580744e+00,6.62063729e+01,-7.57737443e-02,
                -7.87250252e-02,-3.46954534e+00,7.04111226e+00,5.74873351e+01,
                -4.75868081e-02,3.84784198e-02,-2.60242401e+00,7.13172788e+00,
                5.93592343e+01,-5.66760651e-02,2.35572966e-02,2.41889537e-04,
                5.02667035e-02,2.66576210e-03,-1.61446444e-02,1.81275190e-01,
                -1.67808248e+00,1.36468759e+02,2.51653913e+04,-3.04775469e-02,
                -3.52094111e-01,3.38052807e+00,8.18505752e+01,8.88628017e+03,
                -2.53784615e-03,-2.75802397e-01,2.27502778e-02,2.49989768e+02,
                8.23242770e+04,-2.53422142e-02,-3.37828023e-01,-2.31743893e-04,
                1.30959895e-02,2.41019896e-04,-2.39845019e-02,-3.37799305e-01,
                -2.79397467e-04,1.36381371e-02,7.21293962e-04,4.59754122e-02,
                8.42823311e-01,-4.93283194e-02,8.81596303e-01,8.43667312e-01,
                -1.59721631e-01,2.40920875e+00,-2.06200893e+00,2.54289016e+01,
                8.31260974e+02,4.52229428e-01,-1.88292533e-01,-4.02871738e-01,
                8.32840298e+00,8.76945772e+01,1.26473088e-01,-3.78801176e-01,
                4.31696943e-01,6.34831387e+00,5.09698033e+01,-9.34551066e-02,
                -4.61262635e-01,-5.24370298e-02,4.38960900e+00,2.42811551e+01,
                1.05495361e-01,-3.53450441e-01,2.69090756e-01,4.23550330e+00,
                2.26176917e+01,-1.14221771e-01,-3.86275196e-01,-1.14252425e-01,
                3.21759355e+00,1.31188358e+01,7.51916152e-02,-3.63279061e-01,
                1.42693418e-01,3.05687112e+00,1.16865484e+01,-9.23723346e-02,
                -3.76007205e-01,2.78274915e-02,2.49942351e+00,7.85687982e+00,
                3.09439748e-02,-4.33717270e-01,7.86736523e-02,2.35707185e+00,
                6.87226195e+00,-6.02876969e-02,-4.10593710e-01,2.06951422e-02,
                2.05981144e+00,5.29114566e+00,9.79679785e-03,-4.15257635e-01,
                -1.51342985e-02,1.90194910e+00,4.46977895e+00,-1.14982989e-02,
                -3.90218567e-01,6.17738790e-02,1.91439558e+00,4.47314331e+00,
                -1.23453928e-02,-4.22456651e-01,-5.81575382e-02,1.74975591e+00,
                3.76589759e+00,-7.09779598e-03,-4.06920122e-01,2.83012634e-02,
                1.71680714e+00,3.54305952e+00,-3.19890941e-02,-4.05391157e-01,
                -3.82124507e-02,1.52045943e+00,2.80705197e+00,-1.69214565e-02,
                -3.89279144e-01,2.34638970e-02,1.57631825e+00,3.02571398e+00,
                -3.99328101e-02,-3.76308883e-01,-2.09218435e-02,1.41257331e+00,
                2.41863775e+00,-2.97321488e-03,-3.82623649e-01,2.39350028e-02,
                1.41597673e+00,2.43083250e+00,-6.09033918e-02,-3.60743984e-01,
                1.46135302e-03,1.34070061e+00,2.19641367e+00,-4.37404340e-02,
                -3.68727048e-01,1.35657197e-02,1.35555744e+00,2.25603038e+00,
                -2.46997156e-02,-3.59059857e-01]

        temp_file.write(content)
        filename = temp_file.name
        y, sr = librosa.load(filename, mono=True, duration=30)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_delta = librosa.feature.delta(chroma_stft)

        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        cent_delta = librosa.feature.delta(spec_cent)

        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        bw_delta = librosa.feature.delta(spec_bw)

        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        rolloff_delta = librosa.feature.delta(rolloff)

        zcr = librosa.feature.zero_crossing_rate(y)
        zcr_delta = librosa.feature.delta(zcr)

        spec_flat = librosa.feature.spectral_flatness(y=y)
        flat_delta = librosa.feature.delta(spec_flat)

        spec_contr = librosa.feature.spectral_contrast(y=y, sr=sr)
        contr_delta = librosa.feature.delta(spec_contr)

        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        mfcc_delta = librosa.feature.delta(mfcc)
        features = []
        features.extend([np.mean(chroma_stft), np.std(chroma_stft), np.var(chroma_stft), stats.skew(chroma_stft,axis=None), stats.kurtosis(chroma_stft,axis=None),
               np.mean(spec_cent), np.std(spec_cent), np.var(spec_cent), stats.skew(spec_cent,axis=None), stats.kurtosis(spec_cent,axis=None), 
               np.mean(spec_bw), np.std(spec_bw), np.var(spec_bw), stats.skew(spec_bw,axis=None), stats.kurtosis(spec_bw,axis=None), 
               np.mean(rolloff), np.std(rolloff), np.var(rolloff), stats.skew(rolloff,axis=None), stats.kurtosis(rolloff,axis=None), 
               np.mean(zcr), np.std(zcr), np.var(zcr), stats.skew(zcr,axis=None), stats.kurtosis(zcr,axis=None), 
               np.mean(spec_flat), np.std(spec_flat), np.var(spec_flat), stats.skew(spec_flat,axis=None), stats.kurtosis(spec_flat,axis=None), 
               np.mean(spec_contr), np.std(spec_contr), np.var(spec_contr), stats.skew(spec_contr,axis=None), stats.kurtosis(spec_contr,axis=None)])
        for e in mfcc:
            features.extend( [np.mean(e), np.std(e), np.var(e), stats.skew(e,axis=None), stats.kurtosis(e,axis=None)])

        features.extend([ np.mean(chroma_delta), np.std(chroma_delta), np.var(chroma_delta), stats.skew(chroma_delta,axis=None), stats.kurtosis(chroma_delta,axis=None),
               np.mean(cent_delta), np.std(cent_delta), np.var(cent_delta), stats.skew(cent_delta,axis=None), stats.kurtosis(cent_delta,axis=None), 
               np.mean(bw_delta), np.std(bw_delta), np.var(bw_delta), stats.skew(bw_delta,axis=None), stats.kurtosis(bw_delta,axis=None), 
               np.mean(rolloff_delta), np.std(rolloff_delta), np.var(rolloff_delta), stats.skew(rolloff_delta,axis=None), stats.kurtosis(rolloff_delta,axis=None), 
               np.mean(zcr_delta), np.std(zcr_delta), np.var(zcr_delta), stats.skew(zcr_delta,axis=None), stats.kurtosis(zcr_delta,axis=None), 
               np.mean(flat_delta), np.std(flat_delta), np.var(flat_delta), stats.skew(flat_delta,axis=None), stats.kurtosis(flat_delta,axis=None), 
               np.mean(contr_delta), np.std(contr_delta), np.var(contr_delta), stats.skew(contr_delta,axis=None), stats.kurtosis(contr_delta,axis=None)])

        for e in mfcc_delta:
            features.extend( [np.mean(e), np.std(e), np.var(e), stats.skew(e,axis=None), stats.kurtosis(e,axis=None)])
        for i in range(len(features)):
            features[i] = (features[i]-mean[i])/std[i]
        return features


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

def features_extractor_cough_check(content):
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(content)
        file = temp_file.name
        audio, sample_rate = librosa.load(file, res_type='kaiser_fast')
        mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)

    return mfccs_scaled_features



def cough_save(content,name):

    with tempfile.NamedTemporaryFile() as temp_file:
        directory = str(Python.getPlatform().getApplication().getExternalFilesDir(None))
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
            title = name+"_"+str(i)+".wav"
            newFilename = directory+"/"+title
            write(newFilename, Fs, distinct_cough.astype(np.float32))
            files = i

    return files