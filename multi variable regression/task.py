from animate import  AnimateGradiendDescent 
import numpy as np

class Model:
    def __init__(self,X,Y,learning_rate=0.001):
        self.X=X
        self.Y=Y
        self.m=np.zeros((1,len(X[0]))) #slope
        self.c=0   #constant term
        self.N=len(self.X)
        self.learning_rate=learning_rate

    def error(self):
        return np.sum((self.predict(self.X)-self.Y)**2)/self.N
        
    def descent(self):
        pass

    def predict(self,X):
      
        prediction= (self.m@X.T)+self.c
        print('prediction ',prediction[0])


        return prediction[0]
    






X=np.array([[1,1]
            ,[2,2]
            ,[3,3],
            [4,4],
            [5,5],
            [6,6],
            [7,7],
            [8,8],
            [9,9],
            [10,10]])
print(X.T)
Y=(X[:,0]*5+X[:,1]*2+10)
print('y',Y)


model=Model(X,Y,learning_rate=0.005)
AnimateGradiendDescent([X,Y],model).animate()


