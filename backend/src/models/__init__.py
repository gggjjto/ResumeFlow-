from tortoise import Tortoise, fields
from tortoise.models import Model

# Initialize the models module
__all__ = ["User", "Resume", "Template"]


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100)
    profile = fields.JSONField()


class Resume(Model):
    id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField("models.User", related_name="resumes")
    template_id = fields.ForeignKeyField("models.Template", related_name="resumes")
    data = fields.JSONField()
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)


class Template(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    content = fields.TextField()
