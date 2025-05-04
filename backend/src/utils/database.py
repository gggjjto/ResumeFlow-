"""数据库连接和模型定义"""

from tortoise import Tortoise, fields
from tortoise.models import Model


async def init_db():
    """初始化数据库连接"""
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # 数据库连接信息，可以根据需要修改
        modules={
            "models": ["src.models.user", "src.models.resume", "src.models.template"]
        },
    )
    await Tortoise.generate_schemas()


class User(Model):
    """用户模型"""

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100)
    profile: dict = fields.JSONField()


class Resume(Model):
    """简历模型"""

    id = fields.IntField(pk=True)
    user_id: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="resumes"
    )
    template_id: fields.ForeignKeyRelation["Template"] = fields.ForeignKeyField(
        "models.Template", related_name="resumes"
    )
    data: dict = fields.JSONField()
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)


class Template(Model):
    """简历模板模型"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    content = fields.TextField()
