from numpy import * 
import matplotlib.pyplot as plt

from data import data_

#for i in range (0, len(data_)): 

    #plt.plot([data_[i][2], data_[i][4]], label = f'{data_[i][0]}, {data_[i][1]}')

#plt.legend()
#plt.grid(True)

#plt.show()

for i in range (0, 4):
    plt.plot([data_[i][0], data_[i][0]], label = f'{data_[i][0]}, {data_[i][0]}')
    plt.plot([data_[i+4][1], data_[i+4][1]], label = f'{data_[i][2]}, {data_[i][1]}')

    plt.legend()
    plt.grid(True)
    plt.show()