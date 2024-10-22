import numpy as np
from matplotlib import pyplot as plot

def ToVolt(data):
    data = [i / 256 * 3.3 for i in data]
    return data


"""
data = [float(i) for i in open("//home//b03-404//Downloads//data.txt").read().split('\n')]
settings = [float(i) for i in open("//home//b03-404//Downloads//settings.txt").read().split('\n')]
"""
# data = ToVolt(data)


data = np.array([float(i) for i in open("//home//b03-404//Desktop//Scripts//data.txt").read().split('\n')])
settings = np.array([float(i) for i in open("//home//b03-404//Desktop//Scripts//settings.txt").read().split('\n')])


fig, ax = plot.subplots(figsize=(14, 10))
plot.title("Процесс заряда и разряда конденсатора в RC-цепочке", wrap=True)
plot.xlabel("Время, с", fontsize=12)
plot.ylabel("Напряжение, В", fontsize=12)
plot.ylim(0.0, 3.5)
plot.xlim(0, settings[1] * len(data))


x = np.linspace(0, settings[1] * len(data), len(data))
point_data = [data[i] for i in range(0, len(data), 30)]
point_x = [i for i in range(0, len(x), 30)]

data_on = [data[i] for i in range(0, len(data)) if i <= data.argmax()]
data_off = [data[i] for i in range(0, len(data)) if i > data.argmax()]
on_time = str(settings[1] * len(data_on))[:5]
off_time = str(settings[1] * len(data_off))[:5]

ax.plot(x, data, c="darkblue", drawstyle="steps-mid", label="V(t)", markevery=point_x, marker=".", markersize=10)

plot.figtext(0.5, 0.5, f'Время заряда: {on_time}с', fontsize=10)
plot.figtext(0.5, 0.4, f'Время разряда: {off_time}с', fontsize=10)

ax.legend()
ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', ls=":")
fig.savefig("//home//b03-404//Desktop//Scripts//graphic.svg", dpi=400)
plot.show()