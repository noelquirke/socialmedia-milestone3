import datetime

from flask_login import UserMixin # noqa
from flask_bcrypt import generate_password_hash # noqa
from peewee import * # noqa

DATABASE = SqliteDatabase('social.db') # noqa


class User(UserMixin, Model): # noqa
    username = CharField(unique=True) # noqa
    email = CharField(unique=True) # noqa
    password = CharField(max_length=120) # noqa
    joined_at = DateTimeField(default=datetime.datetime.now) # noqa

    class Meta:
        database = DATABASE
        order_by = ("-joined_at",)

    def get_post(self):
        return Post.select().where(Post.user == self)

    def get_stream(self):
        return Post.select().where((Post.user << self.following()) | (Post.user == self)) # noqa

    def following(self):
        """ The users we are following """
        return (
            User.select().join(Relationship, on=Relationship.to_user).where(Relationship.from_user == self) # noqa
        )

    def followers(self):
        """ Get the users who follow me """
        return (
            User.select().join(Relationship, on=Relationship.from_user).where(Relationship.to_user == self) # noqa
        )

    @classmethod
    def create_user(cls, username, email, password):
        try:
            with DATABASE.transaction():
                cls.create(username=username, email=email, password=generate_password_hash(password)) # noqa
        except IntegrityError: # noqa
            raise ValueError('User already exist')


class Post(Model): # noqa
    user = ForeignKeyField(User, related_name='posts') # noqa
    timestamp = DateTimeField(default=datetime.datetime.now) # noqa
    content = TextField() # noqa

    class Meta:
        database = DATABASE
        order_by = ("-joined_at",)


class Relationship(Model): # noqa
    from_user = ForeignKeyField(User, related_name="repationships") # noqa
    to_user = ForeignKeyField(User, related_name="related_to") # noqa

    class Meta:
        database = DATABASE
        indexes = ((('from_user', 'to_user'), True),)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Relationship], safe=True)
    DATABASE.close()
