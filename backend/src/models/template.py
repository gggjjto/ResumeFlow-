"""Template model for Tortoise ORM."""

from tortoise import Model, fields


class Template(Model):
    """Template model for storing resume templates."""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    content = fields.TextField()
