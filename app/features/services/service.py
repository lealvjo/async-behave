import asyncio
from aiohttp import ClientSession

RESP = []


async def main(ids: list):
    tasks = []
    sem = asyncio.Semaphore(int(ids[-1]))

    async with ClientSession() as session:
        for id in ids:
            task = asyncio.ensure_future(fetch(sem, session, id))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses


async def fetch(sem, session, id):
    async with sem:
        while True:
            async with session.get(f"https://jsonplaceholder.typicode.com/todos/{id}") as response:
                print(f'get atual {id}')
                result = await response.json()
                await asyncio.sleep(5)
                if True:
                    set_resp(result)
                    break


def set_resp(rep):
    RESP.append(rep)
    print(rep)


def get_resp():
    return RESP
