# Face Unlock for KDE Plasma


## Unlocking plasma

Here we will use the following script
```python
import os

os.system('loginctl unlock-session')
```

## Running script when Lock Screen is used

Here we will use the following checking mechanism
```bash
dbus-monitor --session "type='signal',interface='org.freedesktop.ScreenSaver'"
```
