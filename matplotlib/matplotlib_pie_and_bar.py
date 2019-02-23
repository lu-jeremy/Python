import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator

from collections import namedtuple

import numpy as np


LABELS = 'Safari', 'Youtube', 'Reminders', 'Chess', 'Crunchyroll'
SIZES = [20, 45, 12, 3, 20]
EXPLODE = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

      
fig1, ax = plt.subplots()
ax.pie(SIZES, explode = EXPLODE, labels = LABELS,
        shadow = True, startangle = 90)

ax.axis('equal')

plt.show()

########################

INDEX = np.arange(6)

BAR_WIDTH = 0.35

fig, ax = plt.subplots()


ax.set_xlabel('Test Scores')
ax.set_ylabel('Number of Students')

ax.set_title('Scores by Number of Students')

ax.set_xticks(INDEX + BAR_WIDTH/6)
ax.set_xticklabels(('Ate a potato','0-20', '21-40', '41-60', '61-80', '81-100'))

rects1 = ax.bar(INDEX, (1, 1, 1, 1, 7, 12) , BAR_WIDTH,
                color='g', label='Students')

ax.legend()

plt.show()
