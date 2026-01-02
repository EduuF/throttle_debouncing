# Throttle & Debouncing Research

This is a research repository for studying and implementing **throttle** and **debouncing** techniques in Python.

## How It Works

### Queue Logic

The program maintains a queue (`search_queue`) that stores all words entered by the user. Words are added to the queue on each input, but stop word checking only occurs when the throttle is activated.

### User Input

The program continuously requests words through `input()`. Each typed word is automatically added to the queue.

### Throttle

The throttle limits the execution of the `check_stop_word` function to **10-second intervals**. This means:

- Words are collected in the queue while the user types
- Stop word checking only happens when the throttle is activated (after 10 seconds since the last execution)
- When the throttle is activated, all words in the queue are checked
- After checking, the queue is automatically reset

### Flow Example

1. User types "hello" → added to queue
2. User types "world" → added to queue
3. User types "the" → added to queue
4. After 10 seconds → throttle activated → checks all words → resets queue

