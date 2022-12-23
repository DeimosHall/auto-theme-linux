#!/bin/python3
from datetime import datetime
import time
from theme import Theme

theme = Theme()
print(f"Theme: {theme.get()}")

while True:
    now = datetime.now()

    if now.hour >= 9 and now.hour <= 20:
        theme.set_light()
        print("set theme")
    else:
        theme.set_dark()
        print("set theme")

    time.sleep(1)