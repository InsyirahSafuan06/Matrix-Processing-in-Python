import numpy as np
# 1. Create ndarray
sales = np.array([
    [120,150,180,200,220,250], #product a
    [80,100,120,140,160,180], #product b
    [200,220,240,260,280,300]  #product c
])

# 2a. Type and shape
print("Type:", type(sales))
print("Shape:", sales.shape)

# 2b. Array creation routine already used (np.array)

# 2c. Indexing (Product B)
print("Product B:",sales[1])

# 2d. Slicing (Month 3 to 5)
print("Month 3-5:",sales[:, 2:5])   

# 2e. Calculations
total_sales = np.sum(sales, axis=1)
average_sales = np.mean(sales, axis=1)

print("Total Sales per Product:", total_sales)
print("Average Monthly Sales:", average_sales)

# 2f. Increase by 10%
updated_sales = sales * 1.10
print("Updated Sales:", updated_sales)