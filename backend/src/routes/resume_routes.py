"""FastAPI routes for resume management."""

from fastapi import APIRouter, HTTPException
from src.models.resume import Resume, Resume_Pydantic, ResumeIn_Pydantic
from src.services.resume_service import ResumeService

router = APIRouter()


@router.post("/resumes/", response_model=Resume_Pydantic)
async def create_resume(resume_data: ResumeIn_Pydantic):
    """
    Create a new resume.
    """
    return await ResumeService.create_resume(resume_data)


@router.get("/resumes/{resume_id}", response_model=Resume_Pydantic)
async def get_resume(resume_id: int):
    """
    Get a resume by ID.
    """
    resume = await ResumeService.get_resume(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume


@router.put("/resumes/{resume_id}", response_model=Resume_Pydantic)
async def update_resume(resume_id: int, resume_data: ResumeIn_Pydantic):
    """
    Update an existing resume.
    """
    updated_resume = await ResumeService.update_resume(resume_id, resume_data)
    if not updated_resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return updated_resume


@router.delete("/resumes/{resume_id}", response_model=dict)
async def delete_resume(resume_id: int):
    """
    Delete a resume by ID.
    """
    deleted = await ResumeService.delete_resume(resume_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {"detail": "Resume deleted successfully"}
