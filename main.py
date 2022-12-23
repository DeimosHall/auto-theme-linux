#!/bin/python3
from datetime import datetime
import time
from theme import theme

light_theme = "ZorinBlue-Light"
dark_theme = "ZorinBlue-Dark"

while True:
    now = datetime.now()
    now_secs = now.hour * 3600 + now.minute * 60 + now.second
    print(f"\rTime: {now_secs}", end="")

    # Between 9 am and 7 pm
    if now_secs >= 3600 * 9 and now_secs <= 3600 * 19:
        if theme.get() == dark_theme:
            theme.set_light()
            print(" Set light theme")
    # Between 12 am and 9 am, and between 7 pm and 12 am
    elif now_secs >= 0 and now_secs <= 3600 * 9 - 1 or now_secs >= 3600 * 19 + 1 and now_secs <= 3600 * 24:
        if theme.get() == light_theme:
            theme.set_dark()
            print(" Set dark theme")

    time.sleep(1)