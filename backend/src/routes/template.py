from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import template as models
from src.schemas import template as schemas

router = APIRouter(prefix="/templates", tags=["templates"])


@router.post("/", response_model=schemas.TemplateResponse)
def create_template(template: schemas.TemplateCreate, db: Session = Depends(get_db)):
    db_template = models.Template(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template


@router.get("/", response_model=List[schemas.TemplateResponse])
def list_templates(db: Session = Depends(get_db)):
    return db.query(models.Template).all()


@router.get("/{template_id}", response_model=schemas.TemplateResponse)
def get_template(template_id: UUID, db: Session = Depends(get_db)):
    template = (
        db.query(models.Template).filter(models.Template.id == template_id).first()
    )
    if not template:
        raise HTTPException(status_code=404, detail="模板不存在")
    return template


@router.put("/{template_id}", response_model=schemas.TemplateResponse)
def update_template(
    template_id: UUID,
    template_update: schemas.TemplateUpdate,
    db: Session = Depends(get_db),
):
    db_template = (
        db.query(models.Template).filter(models.Template.id == template_id).first()
    )
    if not db_template:
        raise HTTPException(status_code=404, detail="模板不存在")
    update_data = template_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_template, key, value)
    db.commit()
    db.refresh(db_template)
    return db_template


@router.delete("/{template_id}")
def delete_template(template_id: UUID, db: Session = Depends(get_db)):
    db_template = (
        db.query(models.Template).filter(models.Template.id == template_id).first()
    )
    if not db_template:
        raise HTTPException(status_code=404, detail="模板不存在")
    db.delete(db_template)
    db.commit()
    return {"message": "模板已删除"}
