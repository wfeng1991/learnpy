import logging,asyncio,orm
from orm import Model, StringField, IntegerField
from aiohttp import web

class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()


logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body='Awesome')

def add(request):
    # 创建实例:
    user = User(id=213, name='zhaoyang')
    # 存入数据库:
    yield from user.save()
    # # 查询所有User对象:
    # users = yield from User.find(1)
    # user.name = 'wangfeng'
    return web.Response(body='success')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/add', add)
    yield from orm.create_pool(loop, host='127.0.0.1', port=3306, user='root', password='', db='test')
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


