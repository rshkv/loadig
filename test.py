from bar import Bar
from time import sleep

sleep_time = 0.01
bar = Bar(message="Running test...")
for i in range(0, 100):
    sleep(sleep_time)
    bar.update(i)
    if i == 25:
        bar.update("Does this look good?")
    if i > 75:
        bar.update("Going to clear in %d" % (bar.total - i))
bar.clear()

for i in range(0, 100):
    sleep(sleep_time)
    bar.update(i)
    if i == 50:
        bar.update("Did the clearing look good?")

bar = Bar(message="This is another test...")
for i in range(0, 100):
    sleep(sleep_time)
    bar.update(i)
