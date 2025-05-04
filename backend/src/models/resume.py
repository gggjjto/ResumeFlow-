"""Resume model for storing user resumes."""

from src.models.template import Template
from src.models.user import User
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Resume(Model):
    """Resume model for storing user resumes."""

    id = fields.IntField(pk=True)
    user_id: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="resumes"
    )
    template_id: fields.ForeignKeyRelation["Template"] = fields.ForeignKeyField(
        "models.Template", related_name="resumes"
    )
    data: dict = fields.JSONField()
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)

    class Meta:
        """Specify the table name in the database"""

        table = "resumes"


# 创建 Pydantic 模型
Resume_Pydantic = pydantic_model_creator(Resume, name="Resume")
ResumeIn_Pydantic = pydantic_model_creator(
    Resume, name="ResumeIn", exclude_readonly=True
)
