"""Template Service for managing templates in the database."""

from tortoise import fields
from tortoise.models import Model


class Template(Model):
    """Template model for storing resume templates."""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    content = fields.TextField()

    class Meta:
        """Specify the table name in the database"""

        table = "templates"

    def __str__(self):
        return self.name

    async def save_template(self):
        """Save the template to the database."""
        await self.save()

    @classmethod
    async def get_template(cls, template_id):
        """Get a template by its ID."""
        return await cls.get(id=template_id)

    @classmethod
    async def update_template(cls, template_id, **kwargs):
        """Update a template by its ID."""
        template = await cls.get(id=template_id)
        for key, value in kwargs.items():
            setattr(template, key, value)
        await template.save()

    @classmethod
    async def delete_template(cls, template_id):
        """Delete a template by its ID."""
        template = await cls.get(id=template_id)
        await template.delete()


class TemplateService:
    """Service layer for managing templates."""

    @staticmethod
    async def create_template(template_data):
        """
        Create a new template.
        """
        template = await Template.create(**template_data.dict())
        return template

    @staticmethod
    async def get_all_templates():
        """
        Get all templates.
        """
        return await Template.all()

    @staticmethod
    async def get_template(template_id):
        """
        Get a template by its ID.
        """
        return await Template.filter(id=template_id).first()

    @staticmethod
    async def update_template(template_id, template_data):
        """
        Update a template by its ID.
        """
        template = await Template.filter(id=template_id).first()
        if template:
            await template.update_from_dict(template_data.dict()).save()
        return template

    @staticmethod
    async def delete_template(template_id):
        """
        Delete a template by its ID.
        """
        deleted_count = await Template.filter(id=template_id).delete()
        return deleted_count > 0
