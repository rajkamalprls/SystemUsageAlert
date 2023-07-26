Rajkamal="name"
import time
from plyer import notification

if __name__ == "__main__":
 while True:
    notification.notify(
        title = "ALERT!!!",
        message = "take a break! It has an hour!",
        timeout = 10
    )
    time.sleep(3600)
