import asyncio
from www.orm import create_pool
from www.models import User, Blog, Comment


async def test(loop):
    await create_pool(loop=loop, user='root', password='123456', db='python_db')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()