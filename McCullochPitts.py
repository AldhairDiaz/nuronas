import numpy as np

class MPNeuron:
    def __init__(self):
        self.threshold = None

    def modelo(self,x):
        #input=[1,0,1,0][x1,x2,x3,xn]
        z=sum(x)
        return (z >= self.threshold)
    
    def prediccion(self,X):
        #input:[[1,0,1,0][1,0,0,0][...]]
        Y = []
        for x in X:
            resultado= self.modelo(x)
            Y.append(resultado)
        return np.array(Y)

mp_neurona= MPNeuron()
mp_neurona.threshold=3
print(mp_neurona.prediccion([[1,0,1,1]]))