from animate import  AnimateGradiendDescent 
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


poly=PolynomialFeatures(degree=3)

class Model:
    def __init__(self,X,Y,learning_rate=0.001):
        self.X=X
        self.Y=Y
        self.m=np.zeros((1,len(X[0]))) #slope
        print('m',self.m)
        self.c=0   #constant term
        self.N=len(self.X)
        self.learning_rate=learning_rate

    def error(self):
        return np.sum((self.predict(self.X)-self.Y)**2)/self.N
        
    def descent(self):
        pass
       
    def predict(self,X):
      
        prediction= (self.m@X.T)+self.c


        return prediction[0]
    






X=np.arange(1,20).reshape(-1,1)
print(X.T)


x_poly=poly.fit_transform(X)[:,1:]
print('x_poly',x_poly)
Y=(X**3-3*X+10).reshape(1,-1)[0]
print('y',Y)


model=Model(x_poly,Y,learning_rate=0.000000003)
AnimateGradiendDescent([x_poly,Y],model).animate()


