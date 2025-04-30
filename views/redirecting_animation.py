import sys
import time

class RedirectingAnimation:
    def __init__():
        super().__init__()

    @staticmethod
    def redirecting_animation(message, cycles=2, delay=0.5):
        for _ in range(cycles):
            for dots in range(1, 4):
                sys.stdout.write("\r" + f'{message}' + "." * dots + " " * (3 - dots))
                sys.stdout.flush()
                time.sleep(delay)
        
        sys.stdout.write("\r" + " " * (len(message) + 3) + "\r")  