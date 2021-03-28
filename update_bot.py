import requests
import time
import logging



if __name__ == '__main__':
    prev_time = time.time()
    while True:
        time.sleep(300)
        r = requests.get("http://spoj-tour.herokuapp.com/update_all_user")