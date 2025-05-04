"""Resume service module."""

from tortoise import fields
from tortoise.models import Model


class Resume(Model):
    """Resume model for storing user resumes."""

    id = fields.IntField(pk=True)
    user_id = fields.ForeignKeyField("models.User", related_name="resumes")
    template_id = fields.ForeignKeyField("models.Template", related_name="resumes")
    data = fields.JSONField()
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)

    class Meta:
        """Specify the table name in the database"""

        table = "resumes"


class ResumeService:
    """Service layer for managing resumes."""

    @staticmethod
    async def create_resume(resume_data):
        """
        Create a new resume.
        """
        resume = await Resume.create(**resume_data.dict())
        return resume

    @staticmethod
    async def get_resume(resume_id):
        """
        Get a resume by ID.
        """
        return await Resume.filter(id=resume_id).first()

    @staticmethod
    async def update_resume(resume_id, resume_data):
        """
        Update an existing resume.
        """
        resume = await Resume.filter(id=resume_id).first()
        if resume:
            await resume.update_from_dict(resume_data.dict()).save()
        return resume

    @staticmethod
    async def delete_resume(resume_id):
        """
        Delete a resume by ID.
        """
        deleted_count = await Resume.filter(id=resume_id).delete()
        return deleted_count > 0
