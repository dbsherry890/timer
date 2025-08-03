# Profiling utility

### Purpose

<ul>
    <li>Timer class allows multiple named timers, collected in a dictionary</li>
    <li>nano_timer allows precise timing</li>
    <li>Timer context manager allows timing a piece of a function</li>
</ul>

### Usage

```Python
from Timer import functimer
# simple decorator
@functimer
def myFunc():
    pass
```

```Python
from Timer import Timer
# context manager
with Timer(name="firstTimer") as t:
    def myFunc()
```
