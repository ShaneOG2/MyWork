# 
# 

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

possibleCounties = ["Kildare", "Monaghan", "Dublin", "Cork", "Limerick"]

counties = np.random.choice(
    possibleCounties, 
    p=[0.1,0.3,0.2,0.12,0.28],
    size=(100)
)

unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels=unique)
plt.bar(unique,counts)
plt.show()