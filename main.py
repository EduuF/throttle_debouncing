#from debouncing.debouncing import debounce
from throttle.throttle import throttle
from check_stop_word import check_stop_word

def main() -> None:
    search_queue = []

    throttler = throttle(check_stop_word, 10) # 10 seconds

    while(True):
        user_input = input("Enter a word: ")
        search_queue.append(user_input)

        throttle_activated = throttler(search_queue)    
        if throttle_activated:
            search_queue = []

if __name__ == "__main__":
    main()