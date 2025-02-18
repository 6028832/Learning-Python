from bluetooth import BluetoothSocket, RFCOMM
import asyncio
from bleak import BleakServer

server = BluetoothSocket(RFCOMM)
server.bind(("4C:D5:77:B9:64:02", 4))
server.listen(1)

client, addr = server.accept()
print(f"Connected to {addr}")

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message:")
        client.send(message.encode('utf-8'))
except OSError as e:
    print(f"Error: {e}")
finally:
    client.close()
    server.close()
    class ChatServer:
        def __init__(self, address):
            self.address = address
            self.server = BleakServer(self.address)

        async def handle_client(self, client):
            print(f"Connected to {client.address}")
            try:
                while True:
                    data = await client.read_gatt_char("00002a37-0000-1000-8000-00805f9b34fb")
                    if not data:
                        break
                    print(f"Message: {data.decode('utf-8')}")
                    message = input("Enter message:")
                    await client.write_gatt_char("00002a37-0000-1000-8000-00805f9b34fb", message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
            finally:
                await client.disconnect()

        async def start(self):
            await self.server.start()
            print(f"Server started at {self.address}")
            while True:
                client = await self.server.accept()
                asyncio.create_task(self.handle_client(client))

    if __name__ == "__main__":
        address = "4C:D5:77:B9:64:02"
        server = ChatServer(address)
        asyncio.run(server.start())