"""FastAPI router for the application."""

from fastapi import APIRouter

from .resume_routes import router as resume_router
from .template_routes import router as template_router
from .user_routes import router as user_router

router = APIRouter()

# Include user routes
router.include_router(user_router, prefix="/users", tags=["users"])

# Include resume routes
router.include_router(resume_router, prefix="/resumes", tags=["resumes"])

# Include template routes
router.include_router(template_router, prefix="/templates", tags=["templates"])
