import threading
import time

start = time.perf_counter()


def do_something():
    print('Sleeping for 1 sec')
    time.sleep(1)
    print('Slept for 1 sec')


# do_something()
# do_something()
# do_something()
# This is taking 3.00259 sec as it is running sequentially


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t3 = threading.Thread(target=do_something)

t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()

finish = time.perf_counter()

print(finish - start)
