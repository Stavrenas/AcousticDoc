# -*- coding: utf-8 -*-
import librosa
import tempfile
import numpy as np
from scipy import stats
from numpy.random import randn
from com.chaquo.python import Python
from scipy.io.wavfile import write

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


def features_extractor_cough_check(content):

    with tempfile.NamedTemporaryFile() as temp_file:

        mean = [3.98488395e-01,3.11825427e-01,9.91868190e-02,5.67493482e-01
            ,-6.50797862e-01,1.80675779e+03,9.24492246e+02,1.00287867e+06
            ,1.17187203e+00,2.29458496e+00,1.76004117e+03,5.19789975e+02
            ,3.12269474e+05,2.50249915e-01,-5.01709423e-03,3.43543911e+03
            ,1.70212163e+03,3.28568749e+06,4.61927576e-01,1.86442260e-01
            ,1.05042094e-01,7.62678579e-02,7.77752639e-03,1.34434878e+00
            ,2.74643407e+00,7.53232372e-02,7.91555211e-02,2.41729363e-02
            ,3.36436336e+00,2.12846290e+01,1.96662543e+01,8.59410055e+00
            ,8.52105526e+01,9.98157140e-01,9.06881246e-01,-3.77536081e+02
            ,1.19650553e+02,1.68302067e+04,6.33380670e-03,-3.59597607e-01
            ,9.28489299e+01,4.89842589e+01,2.72855787e+03,-1.23762315e-01
            ,-1.56896674e-01,-1.19085170e+01,3.24400821e+01,1.19715718e+03
            ,-2.62893758e-01,1.57567637e-02,2.77226183e+01,2.42019390e+01
            ,6.73164289e+02,3.72023399e-01,2.42651651e-01,-3.64210574e+00
            ,2.15543909e+01,5.29160890e+02,-4.44853283e-01,3.74563592e-01
            ,5.44228861e+00,1.78228757e+01,3.62802525e+02,-4.38210018e-02
            ,3.91586734e-01,-9.24488952e+00,1.59402809e+01,2.89490331e+02
            ,-2.87284643e-01,4.51522608e-02,-6.56718137e+00,1.44633457e+01
            ,2.36158468e+02,-3.02432161e-01,1.42882312e-01,-7.15617492e+00
            ,1.26659304e+01,1.77952000e+02,-3.30405405e-01,1.19640965e-01
            ,-2.43201340e+00,1.13501873e+01,1.44026163e+02,-2.49912725e-01
            ,2.53895522e-01,-2.45999383e+00,1.06020515e+01,1.25424443e+02
            ,-2.11417388e-01,3.15171022e-01,-3.49349029e+00,9.62165842e+00
            ,1.02639763e+02,-1.59464445e-01,1.93140783e-01,4.21725627e-02
            ,9.15236896e+00,9.29546779e+01,-8.37754855e-02,3.51275802e-01
            ,-1.79281986e+00,8.78987872e+00,8.59683949e+01,-1.46852672e-01
            ,2.49718577e-01,3.38154798e-01,8.10966659e+00,7.25302153e+01
            ,-8.87665881e-02,3.94178658e-01,-3.45511518e+00,8.26459318e+00
            ,7.59795704e+01,-2.08383429e-01,1.96286073e-01,-2.83277707e+00
            ,7.89709742e+00,6.96210073e+01,-1.96231023e-01,3.15762633e-01
            ,-2.08937445e+00,7.44278197e+00,6.21634231e+01,-2.10373212e-01
            ,2.87324823e-01,-3.12912557e+00,7.34100530e+00,6.05521082e+01
            ,-1.54608831e-01,2.96764464e-01,-7.53831815e-01,7.09690912e+00
            ,5.71684669e+01,-8.17619548e-02,4.31953992e-01,-3.05932084e-05
            ,5.26602844e-02,2.85944043e-03,-1.29884832e-02,1.86564773e-01
            ,-6.62068874e-01,1.73306246e+02,3.59757057e+04,-6.31231786e-02
            ,1.02640501e+00,1.19372676e+00,9.36561817e+01,1.01684395e+04
            ,-6.97365825e-02,3.94718078e-01,1.28691695e+00,3.14679287e+02
            ,1.14818163e+05,-4.10628488e-02,3.12676751e-01,-2.49171883e-05
            ,1.45309632e-02,2.76888325e-04,-3.50319235e-02,1.54606813e+00
            ,-5.31215458e-05,1.17125389e-02,5.04822803e-04,-4.15100043e-01
            ,7.15576387e+00,-2.31051046e-02,8.78913337e-01,8.30125926e-01
            ,2.60870951e-02,2.32047212e+00,-6.24549816e-01,1.89370624e+01
            ,4.50940845e+02,4.94046007e-01,8.36291086e-01,-1.25122025e-01
            ,8.89011347e+00,9.16985977e+01,1.18557575e-01,5.30836145e-01
            ,1.20227743e-01,6.09224253e+00,4.33548156e+01,-4.43002697e-02
            ,2.39104905e-01,-2.67522795e-02,4.56096991e+00,2.42502776e+01
            ,5.26788192e-02,3.38411469e-01,8.23606656e-02,4.02910512e+00
            ,1.87775646e+01,-3.22196606e-02,3.99937388e-01,-2.68042936e-02
            ,3.40309730e+00,1.35266151e+01,-1.76153859e-03,3.85780491e-01
            ,3.53161092e-02,2.85546636e+00,9.51398612e+00,-5.67311226e-02
            ,2.68265222e-01,1.03832333e-02,2.57760986e+00,7.56174656e+00
            ,-4.00804706e-02,2.62808143e-01,2.49147200e-02,2.28191777e+00
            ,5.91355125e+00,-4.55354332e-02,2.51213887e-01,4.82402077e-03
            ,2.10469971e+00,5.06451105e+00,-1.94022962e-02,2.19113110e-01
            ,-8.30115719e-03,1.94537809e+00,4.30075175e+00,-3.74772618e-02
            ,2.75809280e-01,1.50080754e-02,1.76217544e+00,3.51372200e+00
            ,-9.67656349e-03,2.29362989e-01,-2.12713912e-02,1.70942194e+00
            ,3.33622843e+00,-4.40924634e-02,2.15954278e-01,9.41574518e-03
            ,1.60725044e+00,2.94371649e+00,-1.15089445e-02,2.03721820e-01
            ,-1.06753905e-02,1.49007966e+00,2.50751105e+00,-2.58168631e-02
            ,2.68395665e-01,7.43918211e-03,1.49636461e+00,2.56342873e+00
            ,-3.32380704e-02,2.16967389e-01,-4.00845847e-03,1.44676191e+00
            ,2.39917016e+00,-1.51995379e-05,2.14218102e-01,7.22263375e-03
            ,1.35526437e+00,2.12771069e+00,-1.96174767e-02,1.99765619e-01
            ,3.57392658e-04,1.32155513e+00,2.02328514e+00,-3.40233952e-02
            ,2.33558160e-01,8.32782488e-03,1.30769765e+00,1.98687941e+00
            ,-1.58464314e-02,2.22833724e-01]


        std = [1.27512344e-02, 1.95172204e-03, 3.92770731e-04, 3.08797778e-01
            , 6.66135692e+00, 4.70387392e+05, 1.48192760e+05, 5.88421649e+11
            , 9.83253408e-01, 2.33217622e+01, 2.73809918e+05, 4.20878559e+04
            , 5.38018071e+10, 5.38643997e-01, 6.11255969e+00, 1.64055191e+06
            , 3.88469436e+05, 4.11124779e+12, 6.99795547e-01, 7.37506876e+00
            , 6.21215844e-03, 1.96074025e-03, 9.51917125e-05, 1.26807153e+00
            , 1.98784591e+01, 3.21424385e-02, 1.79073397e-02, 3.52025351e-03
            , 9.12316144e+00, 2.86310191e+03, 1.19664205e+01, 1.13519883e+01
            , 5.75646381e+03, 4.93743720e-01, 2.30242857e+01, 3.02803356e+04
            , 2.51395188e+03, 1.54200644e+08, 7.29815264e-01, 1.20627379e+01
            , 1.15966939e+03, 3.29100247e+02, 2.96431481e+06, 5.79625610e-01
            , 7.01948082e+00, 7.29932937e+02, 1.44798249e+02, 6.62234786e+05
            , 4.82346269e-01, 6.28686819e+00, 3.18718625e+02, 8.74304382e+01
            , 2.55935380e+05, 4.82737768e-01, 1.46053916e+01, 4.20800665e+02
            , 6.45691230e+01, 1.34111371e+05, 5.23596067e-01, 1.17669755e+01
            , 1.79891697e+02, 4.51476273e+01, 6.73514691e+04, 6.22453666e-01
            , 1.02113503e+01, 1.99622259e+02, 3.53977751e+01, 4.75037926e+04
            , 4.40304391e-01, 6.66547187e+00, 8.71347875e+01, 2.69700992e+01
            , 2.41430146e+04, 4.52397625e-01, 9.03309385e+00, 8.95737010e+01
            , 1.75262077e+01, 1.26263837e+04, 4.35871747e-01, 6.07609259e+00
            , 9.33825080e+01, 1.51994108e+01, 8.84652580e+03, 4.47295360e-01
            , 8.81400692e+00, 5.32019017e+01, 1.30209480e+01, 6.49708651e+03
            , 4.89852925e-01, 1.13871804e+01, 8.15248982e+01, 1.00634526e+01
            , 4.51339943e+03, 4.80154027e-01, 9.37174533e+00, 3.77013263e+01
            , 9.18882050e+00, 3.57527174e+03, 4.58427084e-01, 1.09367474e+01
            , 9.08639962e+01, 8.70642692e+00, 3.14938076e+03, 4.54809539e-01
            , 9.79210978e+00, 3.58967785e+01, 6.76352326e+00, 1.99860229e+03
            , 4.63118920e-01, 9.95629596e+00, 4.25021208e+01, 7.67606983e+00
            , 2.64661610e+03, 4.47015678e-01, 9.96721041e+00, 2.33744995e+01
            , 7.25685964e+00, 2.74197154e+03, 4.64989546e-01, 1.06749685e+01
            , 2.49717474e+01, 6.76841961e+00, 2.51459528e+03, 4.66698857e-01
            , 9.71850326e+00, 1.80935523e+01, 6.66174932e+00, 2.37787786e+03
            , 4.36944003e-01, 1.08200459e+01, 2.63344937e+01, 6.80234792e+00
            , 2.44110552e+03, 4.79141204e-01, 1.19925662e+01, 1.96519325e-05
            , 8.63348709e-05, 6.42316239e-07, 5.85385752e-02, 2.08910907e+00
            , 6.72727205e+02, 5.94065087e+03, 8.71668883e+08, 2.92017549e-01
            , 4.79257787e+00, 2.50917320e+02, 1.39695918e+03, 6.48448626e+07
            , 3.66623820e-01, 5.02361283e+00, 2.19952316e+03, 1.57951094e+04
            , 6.51560547e+09, 2.72086200e-01, 3.77009672e+00, 4.93519622e-06
            , 6.57394324e-05, 9.51515067e-08, 2.98479172e-01, 7.24552238e+00
            , 3.23090562e-05, 3.67639238e-04, 1.98701588e-06, 4.43449235e+00
            , 2.42830243e+02, 4.72692671e-03, 5.76372721e-02, 1.81720304e-01
            , 3.38913526e-01, 1.36661536e+01, 2.33351831e+01, 9.23285134e+01
            , 2.17258711e+05, 6.97215669e-01, 8.59326159e+00, 2.31165967e+00
            , 1.26644802e+01, 4.35172133e+03, 3.43240531e-01, 4.74543518e+00
            , 1.13821713e+00, 6.23939650e+00, 1.14990323e+03, 2.49575464e-01
            , 3.37808249e+00, 4.93789744e-01, 3.44783102e+00, 3.75086180e+02
            , 3.00769865e-01, 1.20090721e+01, 4.36759670e-01, 2.54387659e+00
            , 2.04216514e+02, 2.68783214e-01, 7.46066963e+00, 2.63472301e-01
            , 1.94554385e+00, 1.15446031e+02, 2.68355560e-01, 3.53376927e+00
            , 2.33453224e-01, 1.36029799e+00, 7.14444363e+01, 2.69604514e-01
            , 3.57631855e+00, 1.51648925e-01, 9.17673983e-01, 2.79857990e+01
            , 2.39860778e-01, 3.22418644e+00, 1.29101489e-01, 7.06402532e-01
            , 1.91323169e+01, 2.40703072e-01, 2.99417617e+00, 1.11335472e-01
            , 6.34750200e-01, 1.50827333e+01, 2.20300750e-01, 2.88039142e+00
            , 8.56779437e-02, 5.16255833e-01, 9.87484325e+00, 2.38350832e-01
            , 3.24298934e+00, 8.83240887e-02, 4.08459724e-01, 7.14238534e+00
            , 2.39916744e-01, 2.94946414e+00, 7.41187843e-02, 4.14105063e-01
            , 6.50482105e+00, 2.13978148e-01, 3.11888447e+00, 6.91240391e-02
            , 3.60462520e-01, 4.92546939e+00, 2.47463250e-01, 3.09338186e+00
            , 5.29524093e-02, 2.87173667e-01, 3.24236634e+00, 2.34389462e-01
            , 3.25824743e+00, 6.16806393e-02, 3.24321678e-01, 4.28548635e+00
            , 2.49081304e-01, 3.01535526e+00, 4.46014203e-02, 3.06050132e-01
            , 4.05882250e+00, 2.36357544e-01, 3.42939983e+00, 4.65432948e-02
            , 2.90969176e-01, 3.97690060e+00, 2.25342945e-01, 3.00115412e+00
            , 4.13538087e-02, 2.76777189e-01, 3.47179090e+00, 2.30088369e-01
            , 3.53529895e+00, 3.69561660e-02, 2.76806279e-01, 3.33182020e+00
            , 2.22269036e-01, 3.24599418e+00]

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
                start_cough = below_sec[break_points[i]+1]


    return t_coughs[1:, :]


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