import matplotlib.pyplot as plt
import numpy as np

import random
from matplotlib.animation import FuncAnimation


class AnimateGradiendDescent:
    def __init__(self,data,model):
        self.fig, self.ax = plt.subplots()
        self.error_fig,self.error_ax=plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.error_line,=self.error_ax.plot([],[],lw=2)
        self.model=model
        self.X=data[0]
        self.Y=data[1]
        self.recorded_errors=[]

    def update(self,frame):
        self.model.descent()
        error=self.model.metric()
        liklihood=self.model.get_liklihood()

        
        self.ax.set_title(f'r2score {error}  liklihood {liklihood}')

        self.line.set_data(self.X[:,0], self.model.predict(self.X))
        
        return self.line,

    def update_error(self,frame):
        error=self.model.error()
        self.recorded_errors.append(error)
        self.error_ax.set_title(f'error {error} ')
        self.error_line.set_data(range(len(self.recorded_errors)),self.recorded_errors)
        self.error_ax.set_xlim(0, len(self.recorded_errors))
        self.error_ax.set_ylim(0, max(self.recorded_errors)+1)
        return self.error_line,

    def animate(self):
        self.ax.plot(self.X[:,0], self.Y, 'bo', label='Initial Data')  # Plot X and Y as blue dots
        self.ax.legend(['model prediction'])  # Add a legend to the plot

        self.error_ax.legend(['model error'])  # Add a legend to the plot


        error_ani=FuncAnimation(self.error_fig, self.update_error, frames=5, interval=50)

        ani = FuncAnimation(self.fig, self.update, frames=5, interval=50)

        plt.show()





    




    



