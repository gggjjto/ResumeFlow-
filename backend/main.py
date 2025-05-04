"""FastAPI应用程序的入口点"""

import config
from fastapi import FastAPI
from src.routes.resume_routes import router as resume_router
from src.routes.template_routes import router as template_router
from src.routes.user_routes import router as user_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

# Register routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(resume_router, prefix="/resumes", tags=["resumes"])
app.include_router(template_router, prefix="/templates", tags=["templates"])

# Database configuration
register_tortoise(
    app,
    db_url=config.DATABASE_URL,
    modules={"models": ["src.models.user", "src.models.resume", "src.models.template"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    """根路由"""
    return {"message": "Welcome to the Intelligent Resume Generator API!"}
