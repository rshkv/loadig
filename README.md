# Loadig...
A minimal progress bar for Python.

```
Loadig...
[===========================           ]  72%
```

# Installation
```
pip3 install loadig
```

# Usage
```python
from loadig import Bar

# Initialization
bar = Bar()
bar = Bar(total=100, characters=40, message="Loading...")

# Update progress
bar.update()  # Increment by one
bar.update()
...
bar.update(23)  # Or set values explicitly
bar.update(24)
...

# Update message
bar.update("Damn, still loading...")

# Clear everything
bar.clear()
```
