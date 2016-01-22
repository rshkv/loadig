# Loadig...
A minimal progress bar for Python.

```
Loadig...
████████████████████████████████████████      91%    0:01:43
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
bar = Bar(total=100, message="Loading...")

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
