import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2FA', 'Login', 'Login - Dispositivo', 'Recuperación de cuenta', 'Recuperación de cuenta / Dispositivo', 'Solo Password']
session_percent = [88.2, 47.8, 59.3, 49.7, 46.6, 89.5]
week_percent = [98.4, 97.3, 97.9, 93.8, 94.6, 95.8]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, session_percent, width, label='Misma sesión',color='blue',edgecolor='black')
rects2 = ax.bar(x + width/2, week_percent, width, label='Una semana',color='orange',edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% Acierto')
ax.set_title('Fuente inicial de falla', size=16)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, size=10)
ax.legend(loc=3)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()