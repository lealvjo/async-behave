import asyncio
from os.path import exists
from os import makedirs
from shutil import rmtree
from urllib.parse import urljoin
from aiohttp import ClientSession
from aiofiles import open as aopen
from requests import get

resp = []


def set_resp(rep):
    resp.append(rep)


def get_resp():
    return resp


async def fetch(sem, session, id):
    async with sem:
        async with session.get(f"https://jsonplaceholder.typicode.com/todos/{id}") as response:
            print(f'get atual {id}')
            for c in range(0, 100):
                if c == 99:
                    result = await response.json()
            set_resp(result)


async def main():
    tasks = []
    sem = asyncio.Semaphore(10)

    async with ClientSession() as session:
        for id in range(1, 11):
            task = asyncio.ensure_future(fetch(sem, session, id))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses

