from bar import Bar
from time import sleep

bar = Bar(message="Loading...")
for i in range(0, 100):
    sleep(0.05)
    bar.update(i)
bar.clear()

for i in range(0, 100):
    sleep(0.05)
    bar.update(i)
