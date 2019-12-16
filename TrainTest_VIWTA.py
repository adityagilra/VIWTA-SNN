import numpy as np
import scipy.io
import shelve, sys, os.path

import VIWTA_SNN
VIWTA_SNN.pyInit()

np.random.seed(100)

#__________________________________________________________________________
# Description: Performs training and testing of the VI-WTA SNN.
#              This is simply a Python wrapper that calls the Boost-ed
#              function VIWTA_SNN (written in C++).
#__________________________________________________________________________

# -- Specify Hyper-Parameter Values: --
dataset  = 'daily'
m        = 10         #number of readout neurons in VIWTA circuit (i.e. # of latent modes)
eta_b    = 0.001      #Learning rate hyperparameter 
eta_W    = 0.0004     #Learning rate hyperparameter
save     = True

if dataset == 'minutely':
   savename = 'VIWTA_minutely_etab' + str(eta_b) + '_etaW' + str(eta_W)
elif dataset == 'daily':
   savename = 'VIWTA_daily_etab' + str(eta_b) + '_etaW' + str(eta_W)

mixing_weights = (1./m)*np.ones(m)

# -- Train & Test via VI (Variational Inference) WTA Circuit: --

## Earlier the datafile was hard-coded into the C++ code,
##  below uses the old signature to call the clustering code, as in the TrainTest_VIWTA.m file
##  assuming hard coded data filename in C++ code:
#W_star, b_star, Converg_avgW, readout_train, readout_test = \
#      VIWTA_SNN.pyWTAcluster(m, eta_b, eta_W, mixing_weights)

# I modified the C++ code to take in a list of lists of neuron spike times
# The new call signature is used below:
# first load in the population spike time data from the sample .txt file
datafile = "ST_VIM_GBPUSD_Daily.txt"; # simulated or actual (data) spike times
print("Loading in spike time data...")
fileobj = open(datafile, "r") 
nrnSpikeTimes = [[]]
nrnnow = 0
for line in fileobj:
    st,nidx = line.split()
    st = float(st)
    nidx = int(nidx)
    if nidx != nrnnow:
        nrnnow = nidx
        nrnSpikeTimes.append([])
    nrnSpikeTimes[-1].append( st )
fileobj.close()
binsize = 200
trainiter = 1
# now, call the python clustering function with the new signature
W_star, b_star, Converg_avgW, readout_train, readout_test = \
  VIWTA_SNN.pyWTAcluster(nrnSpikeTimes, float(binsize), m, eta_b, eta_W, trainiter, mixing_weights)


print("W_star, b_star, Converg_avgW, readout_train, readout_test")
print(W_star, b_star, Converg_avgW, readout_train, readout_test)
 
if save:
    dataBase = shelve.open(savename+'.shelve')
    dataBase['W_star'] = W_star
    dataBase['b_star'] = b_star
    dataBase['Converg_avgW'] = Converg_avgW
    dataBase['readout_train'] = readout_train
    dataBase['readout_test'] = readout_test
    dataBase.close()
