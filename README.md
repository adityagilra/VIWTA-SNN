This is a fork of the repo: [https://github.com/adriannaloback/VIWTA-SNN](https://github.com/adriannaloback/VIWTA-SNN):
# Variational Inference Winner-take-all (VIWTA) Neural Circuit Model for Unsupervised On-line Clustering  
  
Implementation in C++ (mexed for local callable use in Matlab) of the variational inference winner-take-all neural circuit model.  
Author: Adrianna Loback  
  
## Paper link:  

* https://www.biorxiv.org/content/10.1101/389155v1.article-info

## Python bindings have been added in this repo  
Author: Aditya Gilra  
The python bindings require boostpython and boost installed. Set version numbers and paths in Makefile and run `make` on the commandline. A .so file will be generated if all compiles successfully.  
An example file for usage `TrainTest_VIWTA.py`, based on the original .m file, is provided.  
You can also import this module from outside this directory as long as its parent directory is in the PYTHONPATH (since `__init__.py` file is present).  
See the companion repo: [https://github.com/adityagilra/UnsupervisedLearningNeuralData](https://github.com/adityagilra/UnsupervisedLearningNeuralData) for more usage examples.  
Three major changes were made to VIWTA_SNN.cpp:  
0. User can comment/uncomment one of `#define MATLAB` or `#define PYTHON` at the start of `VIWTA_SNN.cpp`, to later mex in Matlab or `make` for Python. However, currently the `#define MATLAB` and mexing in Matlab won't work due to the changes below. Use the code in the [original repo](https://github.com/adriannaloback/VIWTA-SNN) to use in Matlab, or modify the WTACircuitModel::WTACircuitModel() call to use the new signature in the mex function in the `VIWTA_SNN.cpp` file in this repo.  
1. The data file was earlier hard coded in the constructor WTACircuitModel::WTACircuitModel() in the VIWTA_SNN.cpp file, now the neuronal spike times must be loaded as a list of lists by the calling python program. The Matlab .m script is now obsolete, and the Matlab binding's mex function in VIWTA_SNN.cpp must be modified to read in neuronal spike times and pass them on to WTACircuitModel::WTACircuitModel(...). Binsize must also be passed in.  
2. An extra loop of training iterations is added to the WTA training procedure and the number of training iterations have to be passed in.  
