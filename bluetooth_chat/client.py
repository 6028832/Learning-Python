import asyncio
from bleak import BleakScanner, BleakClient

address = "4C:D5:77:B9:64:02"

async def discover_services(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  Characteristic: {characteristic.uuid}")

loop = asyncio.get_event_loop()
loop.run_until_complete(discover_services(address))
async def send_message(address, message):
    async with BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                if "write" in characteristic.properties:
                    await client.write_gatt_char(characteristic.uuid, message.encode())
                    print(f"Sent message: {message}")
                    return
        print("No writable characteristic found")

async def receive_message(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            for characteristic in service.characteristics:
                if "notify" in characteristic.properties:
                    def callback(sender, data):
                        print(f"Received message: {data.decode()}")
                    await client.start_notify(characteristic.uuid, callback)
                    await asyncio.sleep(10)  # Listen for 10 seconds
                    await client.stop_notify(characteristic.uuid)
                    return
        print("No notifiable characteristic found")

async def main():
    address = "4C:D5:77:B9:64:02"
    await discover_services(address)
    await send_message(address, "Hello, Bluetooth!")
    await receive_message(address)

loop.run_until_complete(main())