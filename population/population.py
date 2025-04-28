import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Population:
    def __init__(self, country_code):
        data = pd.read_csv('countries.csv')
        self.population = data[data["Country Code"] == country_code].iloc[0, 4:].values.reshape(-1,1)
        self.years = np.array(list(map(int, data.columns[4:].tolist()))).reshape(-1,1)

    def population_rate_of_change(self):
        self.rate=self.population[1:]-self.population[:-1]
        return self.rate



# plt.scatter(c.years[:-1],c.population_rate_of_change())
# plt.xlabel('Year')
# plt.ylabel('Population Rate of Change')
# plt.show()