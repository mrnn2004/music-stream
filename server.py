import websockets
import asyncio



PORT = 3000

print(str(PORT))
    

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")

    try:
        async for message in websocket:
            print(message)
            await websocket.send("shot")

    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()