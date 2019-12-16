# Variational Inference Winner-take-all (VIWTA) Neural Circuit Model for Unsupervised On-line Clustering

Implementation in C++ (mexed for local callable use in Matlab) of the variational inference winner-take-all neural circuit model.
Author: Adrianna Loback

## Paper link:

* https://www.biorxiv.org/content/10.1101/389155v1.article-info

## Python bindings added  
Author: Aditya Gilra  
The python bindings require boostpython and boost installed. Set version numbers and paths in Makefile and run `make` on the commandline. A .so file will be generated if all compiles successfully. An example file for usage is provided: TrainTest_VIWTA.py based on the original .m file. You can also import this module from outside this directory as long as it's parent directory is in the PYTHONPATH (due to __init__.py file).  
Three major changes were made:  
0. There is an #define ... switch at the start of VIWTA_SNN.cpp to choose between mexing in Matlab or `make` for Python. However, currently the #define Matlab and mexing in Matlab won't work due to the changes below.
1. The data file was earlier hard coded in the constructor WTACircuitModel::WTACircuitModel() in the VIWTA_SNN.cpp file, now the neuronal spike times must be loaded as a list of lists by the calling python program. The Matlab .m script is now obsolete, and the Matlab binding's mex function in VIWTA_SNN.cpp must be modified to read in neuronal spike times and pass them on to WTACircuitModel::WTACircuitModel(...). Binsize must also be passed in.  
2. An extra loop of training iterations is added to the WTA training procedure and the number of training iterations have to be passed in.  
