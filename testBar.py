from bar import Bar
from time import sleep

bar = Bar(message="Bar 1:")
for i in range(0, 100):
    sleep(0.01)
    bar.update(i)
bar.clear()

for i in range(0, 100):
    sleep(0.01)
    bar.update(i)