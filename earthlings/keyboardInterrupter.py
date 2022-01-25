import time
while True:
    try:
        print("Loop processing...")
        print("Press ctrl+c to break")
        time.sleep(1)
    except KeyboardInterrupt:
        print('User interrupted the loop...exiting...')
        break