import time

def debounce(func, delay):
    last_run = time.time()
    def wrapper(*args, **kwargs):
        nonlocal last_run
        current_time = time.time()
        passed_time = current_time - last_run
        print(f"Debounce | Passed time: {passed_time}")
        if passed_time >= delay:
            print(f"Debounce | Checking stopword")
            last_run = current_time
            return func(*args, **kwargs)
        print(f"Debounce | Waiting {delay - passed_time} seconds to check stopword")
        
        

    return wrapper