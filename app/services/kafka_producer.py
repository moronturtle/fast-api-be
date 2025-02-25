from aiokafka import AIOKafkaProducer
import asyncio

async def send_message(topic: str, message: str):
    producer = AIOKafkaProducer(bootstrap_servers="kafka:9092")
    await producer.start()
    try:
        await producer.send_and_wait(topic, message.encode("utf-8"))
    finally:
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(send_message("news_topic", "New article published!"))