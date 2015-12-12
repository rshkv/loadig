# loading...
A minimal progress bar for Python.

```
Loading...
[===========================           ]  72%
```

# Usage
```python
from loading.bar import Bar

# Initialization
bar = Bar(total=100, characters=40, message="Loading...")

# Update progress
bar.update(1)
bar.update(2)
...

# Update message
bar.update("Damn, still loading...")

# Clear everything
bar.clear()
```
