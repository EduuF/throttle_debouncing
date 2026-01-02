import time

def throttle(func, delay):
    last_call = 0
    def wrapper(*args, **kwargs):
        nonlocal last_call
        current_time = time.time()
        passed_time = current_time - last_call
        print(f"Throttle | Passed time: {passed_time}")
        if passed_time >= delay:
            print(f"Throttle | Checking stopword")
            last_call = current_time
            func(*args, **kwargs)
            return True  # Retorna True if throttle is activated
        print(f"Throttle | Waiting {delay - passed_time} seconds to check stopword")
        return False  # return False when still waiting
    return wrapper