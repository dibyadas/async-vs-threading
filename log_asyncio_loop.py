import asyncio
import select

number_of_events_read = 0
filepath = '/dev/input/event5'

async def log_events():
    global number_of_events_read
    file = open(filepath,'rb')
    while True:
        # select returns after 0.05 secs and we have to check if r is 
        # empty( == socket not ready ) or non-empty ( == socket ready to be read)
        r,_,_ = select.select([file],[],[], 0.00005)
        if r != []: # if not ready to read
            read_val = file.read(10)
            print(f'{read_val} in log_events')
            print(f'{number_of_events_read} in log_events')
            number_of_events_read += 1
        await asyncio.sleep(0) # suspend for some time and let others run
            
async def notify_events():
    global number_of_events_read
    file = open(filepath,'rb')
    while True:
        # select returns after 0.05 secs and we have to check if r is 
        # empty( == socket not ready ) or non-empty ( == socket ready to be read)
        r,_,_ = select.select([file],[],[], 0.00005) 
        if r != []: # if not ready to read
            read_val = file.read(10)
            print(f'{read_val} in notify_events')
            print(f'{number_of_events_read} in notify_events')
            number_of_events_read += 1
        await asyncio.sleep(0) # suspend for some time and let others run

tasks = asyncio.gather(log_events(), notify_events())
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)