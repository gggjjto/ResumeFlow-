"""用户 相关路由"""

from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import user as models
from src.schemas import user as schemas
from src.utils.auth import create_access_token, get_password_hash, verify_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """创建用户"""
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """获取用户列表"""
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@router.post("/login")
async def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    """用户登录（支持邮箱和用户名）"""
    user = None
    # 尝试通过邮箱查找
    if "@" in user_credentials.login:
        user = (
            db.query(models.User)
            .filter(models.User.email == user_credentials.login)
            .first()
        )
    # 尝试通过用户名查找
    if not user:
        user = (
            db.query(models.User)
            .filter(models.User.username == user_credentials.login)
            .first()
        )

    if not user or not verify_password(
        user_credentials.password, str(user.hashed_password)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误"
        )

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/reset-password")
async def reset_password(
    reset_data: schemas.PasswordReset, db: Session = Depends(get_db)
):
    """重置密码"""
    user = db.query(models.User).filter(models.User.email == reset_data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")

    if not verify_password(reset_data.old_password, str(user.hashed_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="原密码错误"
        )

    user.hashed_password = get_password_hash(reset_data.new_password)
    db.add(user)
    db.commit()

    return {"message": "密码重置成功"}


@router.get("/{user_id}", response_model=schemas.UserDetail)
async def get_user_detail(
    user_id: int = Path(..., title="用户ID"), db: Session = Depends(get_db)
):
    """获取用户详细信息"""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


@router.put("/{user_id}", response_model=schemas.UserDetail)
async def update_user(
    user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)
):
    """更新用户信息"""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="用户不存在")

    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """删除用户"""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="用户不存在")

    db.delete(db_user)
    db.commit()
    return {"message": "用户已删除"}


@router.patch("/{user_id}/status")
async def update_user_status(
    user_id: int, is_active: bool = Body(..., embed=True), db: Session = Depends(get_db)
):
    """更新用户状态（启用/禁用）"""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="用户不存在")

    db_user.is_active = is_active
    db.commit()
    return {"message": "用户状态已更新"}
