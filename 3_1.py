# 3_1 How to construct a bar graph with overlay in python
import matplotlib.pyplot as plt
import numpy as np

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values1 = [100, 150, 200, 300]
values2 = [5, 12, 18, 70]

plt.bar(categories, values1, label='Set 1', color='blue')
plt.bar(categories, values2, label='Set 2', color='orange', alpha=0.5)  # alpha controls transparency

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph with Overlay')

plt.legend()
plt.show()
