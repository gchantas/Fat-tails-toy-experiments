# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:17:38 2021

@author: gchantas
"""

from matplotlib import pyplot
import numpy as np

from scipy.stats import norm
from scipy.stats import kurtosis

#Number of followers of my Twitter followers in an array.
a=[14.4, 54.7, .58, 0.69, 0.01, 0, 0.2, 3.19, 0.19, 0.57, 0.19, 0.17, 0.1, 0.23, 0.5, 0.7, 0.2, 1.3, 0.04, 0.86, 796, 0.22, 2.5, 6, 2.2, 1.4, 8.1, 0.94, 0.47, 0.59, 1.6, 0.5, 0.001, 3, 3.2, 0.96]
#Sort the array
a1=np.sort(np.asarray(a))


#pyplot.hist(a1,100)
#pyplot.hist(np.log((np.log(a1+1)+1)),100)

###Gamma distribution fit
#alpha=np.mean(a1)**2/a1.size
#alpha=(np.mean(a1)/np.sqrt(np.var(a1)))**2
#beta=(np.var(a1)/np.mean(a1))


N = a1.size 
b=np.zeros((N+1,2));


for k in range(N):
    #pre-fix sums for cpf
    b[k+1,0]=b[k,0]+a1[k]
    #frequency ranks
    b[k+1,1]=k
    
    
pyplot.plot(  np.log(np.log(1- b[1:N,0]/sum(b[1:,0]) )+1),'bo')
pyplot.plot(  np.log(np.log(1- b[1:N,1]/sum(b[1:,1]) )+1)   )
pyplot.show()

