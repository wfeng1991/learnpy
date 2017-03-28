import asyncio
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test_example():
    conn = yield from aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='', db='test',
                                       charset='utf8',autocommit=True,
                                       loop=loop)

    cur = yield from conn.cursor()
    yield from cur.execute('insert into users (name) values ("你好")')   
    yield from cur.execute("SELECT id,name FROM users")
    print(cur.description)
    r = yield from cur.fetchall()
    print(r)
    yield from cur.close()
    conn.close()

loop.run_until_complete(test_example())