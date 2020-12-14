from numpy import * 
import matplotlib.pyplot as plt

from data import data_

for i in range (0, len(data_)): 

    plt.plot([data_[i][2], data_[i][5]], label = f'{data_[i][0]}, {data_[i][1]}')

plt.legend()
plt.grid(True)

def showPlot():
    plt.show()

#for i in range (0, 4):
    #plt.plot([data_[i][2], data_[i][5]], label = f'{data_[i][0]}, {data_[i][1]}')
    #plt.plot([data_[i+4][2], data_[i+4][5]], label = f'{data_[i+4][0]}, {data_[i+4][1]}')

    #plt.legend()
    #plt.grid(True)
    #plt.show()