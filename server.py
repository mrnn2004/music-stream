#!/usr/bin/env python

import asyncio
import websockets

port = 3000


print('server is listening on port '+str(port))
async def echo(websocket):
    print('A client just connected')
    async for message in websocket:
        print(message)
        await websocket.send('hello client')

async def main():
    async with websockets.serve(echo, "localhost", port):
        await asyncio.Future()  # run forever

asyncio.run(main())