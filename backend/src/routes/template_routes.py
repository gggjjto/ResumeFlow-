"""routes/template_routes.py"""

from fastapi import APIRouter, HTTPException
from src.models.template import Template

from ..services.template_service import TemplateService

router = APIRouter()


@router.post("/templates/")
async def create_template(template: Template):
    """
    Create a new template.
    """
    return await TemplateService.create_template(template)


@router.get("/templates/")
async def get_templates():
    """
    Get all templates.
    """
    return await TemplateService.get_all_templates()


@router.get("/templates/{template_id}")
async def get_template(template_id: int):
    """
    Get a template by ID.
    """
    template = await TemplateService.get_template(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.put("/templates/{template_id}")
async def update_template(template_id: int, template: Template):
    """
    Update an existing template.
    """
    updated_template = await TemplateService.update_template(template_id, template)
    if not updated_template:
        raise HTTPException(status_code=404, detail="Template not found")
    return updated_template


@router.delete("/templates/{template_id}")
async def delete_template(template_id: int):
    """
    Delete a template by ID.
    """
    success = await TemplateService.delete_template(template_id)
    if not success:
        raise HTTPException(status_code=404, detail="Template not found")
    return {"message": "Template deleted successfully"}
