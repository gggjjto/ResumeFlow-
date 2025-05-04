"""User Service Module"""

from tortoise import fields
from tortoise.models import Model
from passlib.hash import bcrypt


class User(Model):
    """User model for storing user information."""

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    email = fields.CharField(max_length=100, unique=True)
    profile = fields.JSONField()

    def set_password(self, password: str):
        """Hash the password using bcrypt."""
        self.password = bcrypt.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify the password against the hashed password."""
        return bcrypt.verify(password, self.password)
