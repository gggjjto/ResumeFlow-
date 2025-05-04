"""User model for Tortoise ORM."""

from tortoise import Model, fields


class User(Model):
    """User model for storing user information."""

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100, unique=True)
    profile = fields.JSONField()

    class Meta:
        """Specify the table name in the database"""

        table = "users"
