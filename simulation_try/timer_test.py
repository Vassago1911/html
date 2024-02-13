from browser import document, alert, html, timer
from random import randint
from time import time

tick_timer = None
btn = document["button_alert"]

def stop_timer():
    timer.clear_interval(tick_timer)

def start_timer():
    tick_timer = timer.set_interval(tick, 500)

def tick():
    btn.innerHTML = f"{int(time())}"

start_timer()