import time
import random
import sys

def fake_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.02, 0.04, 0.08, 0.014, 0.018,
          0.06, 0.02, 0.04, 0.02, 0.04
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)