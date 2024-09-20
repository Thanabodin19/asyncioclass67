# https://aiokafka.readthedocs.io/en/stable/
from aiokafka import AIOKafkaProducer
import asyncio
from time import sleep, ctime

async def send_one():
    i = 0
    while True:
        producer = AIOKafkaProducer(
            bootstrap_servers='localhost:9092')
        # Get cluster layout and initial topic/partition leadership information
        await producer.start()
        try:
            # Produce message
            message = f'send {i}'.encode('UTF8')
            await producer.send_and_wait("my_topic", message)
        finally:
            # Wait for all pending messages to be delivered or expire.
            await producer.stop()
        i += 1
        sleep(1)

async def main():
    await send_one()
      
asyncio.run(main())



 