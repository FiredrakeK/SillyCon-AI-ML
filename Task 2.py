"""TASK2*
Use Google Colab.
Import any public Kaggle dataset of your choice.

Perform EDA using:
➤ pandas, numpy, matplotlib, seaborn, and scikit-learn

Summarize the dataset and determine:
Whether it is supervised or unsupervised learning
Which type of algorithm (e.g., classification, regression, clustering) is best suited and why"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
da= pd.read_csv("wearable_health_devices_performance_upto_26june2025.csv")
print("some initial values:-")
#print(data.head())
#print("Dataset shapes")
#print(data.shape())
print("Dataset column types:- ")
#print(data.dtypes)
print("dataset Summary Information")
#print(data.info())
print("descriptive statistics:- ")
#print(data.describe()) #every column ka specific data ka details like mmm, deviation min max etc. 
print("Missing values in each column. ")
#print(data.isnull().sum()) # checking for null values  # tells how many missing values each column has. 
print("Duplicate values in column :-")
#print(data.duplicated().sum())
'''
#univariate analysis #shows histogram
data['Performance_Score'].value_counts()
sns.histplot(data['Performance_Score'])
plt.show()'''

# bivariate data analysis
sns.scatterplot(x='Heart_Rate_Accuracy_Percent', y='Performance_Score', data=da)
sns.boxplot(x='Model', y='Price_USD', data=da)

plt.show()




