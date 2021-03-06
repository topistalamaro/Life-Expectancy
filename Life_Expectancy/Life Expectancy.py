#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
# print(data.head())
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.50, 0.75])
print(life_expectancy_quartiles)
plt.hist(life_expectancy)
plt.show()



# 70 years of life expectancy lies in the second quartile
gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.50)

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25,0.50,0.75])
high_gdp_quartiles =  np.quantile(high_gdp["Life Expectancy"], [0.25,0.50,0.75])
print(low_gdp_quartiles)
print(high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.title('Impact of GDP on Life Expectancy')
plt.show()


# In[ ]:




