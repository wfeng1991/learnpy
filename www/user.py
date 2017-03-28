from orm import Model, StringField, IntegerField, create_pool


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()


def test():
    yield from create_pool(None, {'user': 'root', 'password': '', 'database': 'test'})

    user = User(id=123, name='Michael')

    yield from user.save()

test()
