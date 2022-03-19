#!/usr/bin/env python3
import requests
from datetime import datetime

def is_prime(num):
    is_prime = True
    for idx in range(num):
        current_num = (idx + 1)
        if current_num == 1:
            continue
        if current_num == num:
            continue
        if num % current_num == 0:
            is_prime = False
            break
    return is_prime

if __name__ == "__main__":
    print("[{0}] client_start".format(
        datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
    ))
    while(True):
        print("[{0}] request".format(
            datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")
        ))
        res = requests.get("http://localhost:8000/").json()
        number = res["number"]
        if number is None:
            break
        
        if is_prime(res["number"]):
            print("[{0}] {1}_is_prime".format(
                datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
                number
            ))
            continue
        print("[{0}] {1}_is_not_prime".format(
            datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
            number
        ))
    print("[{0}] client_terminated".format(
        datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"),
    ))
