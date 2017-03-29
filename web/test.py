from orm import Model, StringField, IntegerField
import asyncio
import aiomysql
import orm

loop = asyncio.get_event_loop()



class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()

@asyncio.coroutine   
def test():
    yield from orm.create_pool(loop, host='127.0.0.1', port=3306, user='root', password='', db='test')
    # 创建实例:
    user = User(id=12, name='Michael Jackson')
    # 存入数据库:
    # yield from user.save()
    # # 查询所有User对象:
    # users = yield from User.find(1)
    user.name = 'wangfeng'

    yield from user.update()

loop.run_until_complete(test())

