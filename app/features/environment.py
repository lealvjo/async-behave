import asyncio
from services.service import main
from hamcrest import assert_that, equal_to
from services.service import get_resp, RESP


def before_feature(context, feature):
    RESP.clear()
    context.id_global = []
    context.loop = asyncio.get_event_loop()


def after_feature(context, feature):
    print(f"Validando Feature {feature.name}")
    future = asyncio.ensure_future(main(context.id_global))
    context.loop.run_until_complete(future)
    assert_that(len(get_resp()), equal_to(0))
