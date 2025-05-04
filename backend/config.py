"""智能简历生成器配置文件"""

import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/resume_db")

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": ["src.models.user", "src.models.resume", "src.models.template"],
            "default_connection": "default",
        }
    },
}
