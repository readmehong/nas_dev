import asyncio

@asyncio.coroutine
def echo_twice(msg):
	print(msg)
	yield from asyncio.sleep(1)
	print(msg)

loop = asyncio.get_event_loop
asyncio.ensure_future(echo_twice('Hello'))
asyncio.ensure_future(echo_twice('There'))
loop.run_forever()
