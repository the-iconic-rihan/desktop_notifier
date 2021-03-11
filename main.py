from plyer import *
import time

# print(60*60*4)
if __name__ == '__main__':
    while True:
        notification.notify (
            title="Launch time!!!",
            app_icon="Icons8-Windows-8-Sports-Exercise.ico",
            message="Its time have launch",
            timeout=6
        )
        time.sleep(60*60*4)
