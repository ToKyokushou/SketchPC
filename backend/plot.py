import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

data = [
    [1, 1, 1, 1, 1, 1, 2, 5, 4, 1, 1, 1]
]

labels = 'Number of Sketch',


plt.figure(figsize=(5, 5))
plt.title('Results of Questionnaire')
plt.boxplot([data[0]], labels=labels, patch_artist=True, showmeans=True, showcaps=True,
            boxprops={'facecolor': 'blue'})
my_y_tixks = np.arange(0, 10, 1)
plt.yticks(my_y_tixks)

plt.show()
