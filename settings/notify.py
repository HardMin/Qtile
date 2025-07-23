import os

def notify(message):
    os.system(message)

def test_notify(message):
    os.system(f'notify-send "{message}"')