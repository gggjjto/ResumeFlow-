"""mian.py"""

from fastapi import FastAPI

from src.database import engine
from src.models import user as models
from src.routes import resume, template

app = FastAPI(title="ResumeFlow API")

# 创建数据库表
models.Base.metadata.create_all(bind=engine)

# 注册路由
app.include_router(user.router)
app.include_router(resume.router)
app.include_router(template.router)


@app.get("/")
def read_root():
    """根路由"""

    return {"message": "Welcome to ResumeFlow API"}
