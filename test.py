import asyncio

from submission import  log_metric

async def main():
    for i in range (10):
        await log_metric('loss', 0.5+i)
        i += 1
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())