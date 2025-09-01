from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Secret(BaseModel):
    id: str
    value: str
    version: int
    expires_at: Optional[datetime]

class SecretCreate(BaseModel):
    value: str
    expires_at: Optional[datetime]

class SecretRotate(BaseModel):
    value: str
    expires_at: Optional[datetime]

class AccessLog(BaseModel):
    secret_id: str
    accessed_by: str
    timestamp: datetime
    action: str
