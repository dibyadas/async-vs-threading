import select
import threading

number_of_events_read = 0

def log_events(lock):
    global number_of_events_read
    file = open('/dev/input/event5','rb')
    while True:
        # select returns after 0.05 secs and we have to check if r is 
        # empty( == socket not ready ) or non-empty ( == socket ready to be read)
        r,_,_ = select.select([file],[],[], 0.00005)
        if r != []: # if not ready to read
            lock.acquire()
            read_val = file.read(10)
            print(f'{read_val} in log_events')
            print(f'{number_of_events_read} in log_events')
            number_of_events_read += 1
            lock.release()

            
def notify_events(lock):
    global number_of_events_read
    file = open('/dev/input/event5','rb')
    while True:
        # select returns after 0.05 secs and we have to check if r is 
        # empty( == socket not ready ) or non-empty ( == socket ready to be read)
        r,_,_ = select.select([file],[],[], 0.00005) 
        if r != []: # if not ready to read
            lock.acquire()
            read_val = file.read(10)
            print(f'{read_val} in notify_events')
            print(f'{number_of_events_read} in notify_events')
            number_of_events_read += 1
            lock.release()

lock = threading.Lock()
t1 = threading.Thread(target=log_events, args=(lock,))
t2 = threading.Thread(target=notify_events, args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()