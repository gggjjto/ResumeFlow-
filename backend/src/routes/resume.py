from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import resume as models
from src.schemas import resume as schemas
from src.utils.ai_optimizer import AIOptimizer

router = APIRouter(prefix="/resumes", tags=["resumes"])


@router.post("/", response_model=schemas.ResumeResponse)
def create_resume(
    user_id: UUID, resume: schemas.ResumeCreate, db: Session = Depends(get_db)
):
    db_resume = models.Resume(
        user_id=user_id,
        content=resume.content,
        template_id=resume.template_id,
        status=resume.status,
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume


@router.get("/", response_model=List[schemas.ResumeResponse])
def list_resumes(user_id: UUID, db: Session = Depends(get_db)):
    resumes = db.query(models.Resume).filter(models.Resume.user_id == user_id).all()
    return resumes


@router.get("/{resume_id}", response_model=schemas.ResumeResponse)
def get_resume(resume_id: UUID, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    return resume


@router.put("/{resume_id}", response_model=schemas.ResumeResponse)
def update_resume(
    resume_id: UUID, resume_update: schemas.ResumeUpdate, db: Session = Depends(get_db)
):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    update_data = resume_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_resume, key, value)
    db.commit()
    db.refresh(db_resume)
    return db_resume


@router.delete("/{resume_id}")
def delete_resume(resume_id: UUID, db: Session = Depends(get_db)):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    db.delete(db_resume)
    db.commit()
    return {"message": "简历已删除"}


@router.post("/{resume_id}/optimize")
def optimize_resume(resume_id: UUID, db: Session = Depends(get_db)):
    """
    使用大模型API优化简历内容
    """
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    original_content = db_resume.content

    # 构造优化提示词
    optimize_prompt = (
        "请以专业HR视角对以下结构化简历进行优化，要求：\n"
        "1. 执行关键词密度分析（目标岗位JD关键词覆盖率需达85%+）\n"
        "2. 应用STAR法则重构项目经历描述\n"
        "3. 将模糊表述转换为量化成果（模板：动词+技术栈+业务指标）\n"
        "4. 根据[行业类型]调整专业术语权重（科技行业：云计算/AI优先；金融行业：合规/风控优先）\n"
        "用户提示词：{data}\n"
        "输入简历片段：{content}\n"
        "输出要求：\n"
        "- 保留JSON结构但增强语义表达\n"
        '- 添加隐含上下文（如"使用Pandas处理10M级数据集"）\n'
        "- 包含技术栈扩展建议（如补充SQL/PySpark）"
    )

    # 组织传递给AI的内容
    ai_input = {"data": "请优化我的简历", "content": original_content}

    # 调用AI优化器
    optimizer = AIOptimizer(prompt=optimize_prompt)
    result = optimizer.get(ai_input)

    return result
