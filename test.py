from loadig import Bar
from time import sleep


sleep_time = 0.2

bar = Bar(total=1000, message="Loadig...", columns=60)
for i in range(0, 1000):
    sleep(sleep_time/10)
    bar.update(i)

bar = Bar(total=100, message="Running test...")
sleep(1)
for i in range(0, 100):
    sleep(sleep_time)
    bar.update()
    if i == 25:
        bar.update("Does this look good?")
    if i > 75:
        bar.update("Going to clear in %d" % (bar.total - i))

sleep(0.5)
bar.clear()

sleep(0.5)
bar = Bar(total=100)
for i in range(0, 100):
    sleep(sleep_time)
    bar.update()
    if i == 50:
        bar.update("Did the clearing look good?")

sleep(1.0)
bar = Bar(total=100, message="This is another test...")
for i in range(0, 100):
    sleep(sleep_time)
    bar.update()
