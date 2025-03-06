import asyncio

from aiokafka import AIOKafkaConsumer


async def consume_messages():
    consumer = AIOKafkaConsumer(
        "news_topic",
        bootstrap_servers="kafka:9092",
        group_id="news_group",
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Received: {msg.value.decode('utf-8')}")
    finally:
        await consumer.stop()


if __name__ == "__main__":
    asyncio.run(consume_messages())
