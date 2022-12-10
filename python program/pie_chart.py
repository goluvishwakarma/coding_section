# Date: 23-01-2021
#       Pie Chart

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["apples", "bananas", "cherries", "dates"]
my_explode = [0.2, 0, 0, 0]

plt.pie(y, labels=my_labels, explode=my_explode, shadow=True)
plt.show()
