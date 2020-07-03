import asyncio

number_of_events_read = 0
filepath = '/dev/input/event5'

async def log_events():
    file = open(filepath, 'rb')

    def callback():
        global number_of_events_read
        read_val = file.read(10)
        print(f'{read_val} in log_events')
        print(f'{number_of_events_read} in log_events')
        number_of_events_read += 1

    loop.add_reader(file.fileno(), callback)


async def notify_events():
    file = open(filepath, 'rb')

    def callback():
        global number_of_events_read
        read_val = file.read(10)
        print(f'{read_val} in notify_events')
        print(f'{number_of_events_read} in notify_events')
        number_of_events_read += 1

    loop.add_reader(file.fileno(), callback)


tasks = asyncio.gather(log_events(), notify_events())
loop = asyncio.get_event_loop()
loop.run_forever()
