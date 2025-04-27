from animate import  AnimateGradiendDescent 
import numpy as np

class Model:
    def __init__(self,data,learning_rate=0.001):
        self.data=data
        self.X=np.array(data[0])
        self.Y=np.array(data[1])
        self.m=0  #slope
        self.c=0   #constant term
        self.N=len(self.X)
        self.learning_rate=learning_rate

    def error(self):
        return np.sum((self.predict(self.X)-self.Y)**2)/self.N
        
    def descent(self):
        pass

    def predict(self,X):
        X=np.array(X)
        return (self.m*X)+self.c
    






X=np.array([1,2,3,4,5,6,7,8,9,10])

Y=(X*5+10)



model=Model([X,Y],learning_rate=0.05)
AnimateGradiendDescent([X,Y],model).animate()


