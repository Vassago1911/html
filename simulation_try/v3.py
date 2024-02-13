from browser import document, alert
from time import time

btn = document["button_alert"]

def hello(ev):
    btn = document["button_alert"]
    btn.innerHTML = int(time())
    alert("hello!")

btn.bind("click",hello)