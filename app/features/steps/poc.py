import asyncio
import time
from behave import given
from behave.api.async_step import async_run_until_complete


@given(u'an async-step waits "{duration}" seconds')
@async_run_until_complete
async def step_async_step_waits_seconds_py35(context, duration):
    """Simple example of a coroutine as async-step (in Python 3.5)"""
    await asyncio.sleep(int(duration))
    print(f"duration {duration} timestamp {time.time()}")
