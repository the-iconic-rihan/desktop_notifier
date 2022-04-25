from plyer import *
import time

#this program shows a notification on desktop after very 4 hours.
if __name__ == '__main__':
    while True:
        notification.notify (
            title="Launch time!!!",
            app_icon="Icons8-Windows-8-Sports-Exercise.ico",
            message="Its time have launch",
            timeout=6
        )
        time.sleep(60*60*4)
