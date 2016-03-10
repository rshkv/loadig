# Loadig...
A minimal progress bar for Python.

![Loadig preview](https://www.dropbox.com/s/8qe15kz524mb24g/loadig.png?dl=1 "Loadig preview")

## Requirements
Make sure you are using Python **3.3** and your terminal supports ANSI Escape Codes. 

## Installation
```
pip install loadig
```
(Yes, *loading* was taken.)

## Usage
```python
from loadig import Bar
```

### Initialization
Pass the total value (your 100%). You can pass a message to display above the bar. `shutil` is used to get the number of columns in your terminal. If you know what you want in life, you can also pass a number of columns to use.
```python
bar = Bar(total=100)
bar = Bar(100, message="Loading...")
bar = Bar(100, columns=80)
```

### Update Progress
Pass a number or string to update the bar or message, respectively. If nothing is passed, the value -not percentage- is inceremented by one.
```python
bar.update()  #  Increment by one
bar.update(23)  #  Set values explicitly
bar.update("Damn, still loading...")  #  Update the message
```

### Clearing
The cursor is always kept under the bar so you don't have to worry about going to a new line before you... well, do other things. Anyway, you can get rid of it.
```python
bar.clear()
```
