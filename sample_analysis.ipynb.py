# Sample Data Analysis Notebook

#This notebook demonstrates a simple data analysis workflow using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create dummy dataset
df = pd.DataFrame({
    "Category": np.random.choice(['A', 'B', 'C'], 50),
    "Value": np.random.randint(10, 100, 50)
})
df.head()

df.describe()
sns.barplot(x='Category', y='Value', data=df, estimator=np.mean, errorbar=None)
plt.title('Average Value by Category')
plt.show()
