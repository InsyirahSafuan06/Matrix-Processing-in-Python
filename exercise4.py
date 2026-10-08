import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Pandas:reada and organize the data
df =pd.read_csv("sales.csv")

#Numpy: perform calculations on the data
average_sales = np.mean(df["Sales"])
print("Average:", average_sales)

#Matplotlib: visualize the data
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()