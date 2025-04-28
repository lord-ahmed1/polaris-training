from animate import  AnimateGradiendDescent 
import numpy as np
from population import Population
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
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
    def metric(self):
        return r2_score(self.Y,self.predict(self.X))
        
    def descent(self):
        pass

    def predict(self,X):
      
        prediction= (self.m@X.T)+self.c


        return prediction[0]

    def normal_distribution(self,avg,std,x):
        return (1/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-avg)/std)**2)   
    def get_liklihood(self):
        error=self.predict(self.X)-self.Y
        liklihood=1
        avg,std=np.average(error),np.std(error)
        for i in error:
            v=self.normal_distribution(avg,std,i)   
            liklihood*=v
        return liklihood
    
    




# p=Population("PHL")

# X=p.years[:-1]
# Y=p.population_rate_of_change()


# # Y=Y/np.max(Y)
# # X=X/np.max(X)


# Y=(Y-np.average(Y))/np.std(Y)
# X=(X-np.average(X))/np.std(X)

# poly=PolynomialFeatures(degree=2)
# X=poly.fit_transform(X)[:,1:]
# Y=Y.reshape(1,-1)[0]


# model=Model(X,Y,learning_rate=0.03)
# AnimateGradiendDescent([X,Y],model).animate()






p=Population("RUS")

X=p.years[:-1]
Y=p.population_rate_of_change()


# Y=Y/np.max(Y)
# X=X/np.max(X)


Y=(Y-np.average(Y))/np.std(Y)
X=(X-np.average(X))/np.std(X)

poly=PolynomialFeatures(degree=5)
X=poly.fit_transform(X)[:,1:]
Y=Y.reshape(1,-1)[0]


model=Model(X,Y,learning_rate=0.03)
AnimateGradiendDescent([X,Y],model).animate()
