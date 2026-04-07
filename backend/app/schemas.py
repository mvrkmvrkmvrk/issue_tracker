from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .models import IssueStatus, IssuePriority

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

#user management
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass        

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

#project management
class ProjectBase(BaseModel):
    name: str
    description: str
    created_by: int 

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

#issue management
class IssueBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: IssueStatus = IssueStatus.OPEN
    priority: IssuePriority = IssuePriority.MEDIUM

class IssueCreate(IssueBase):
    project_id: int
    assigned_to: Optional[int] = None

class IssueUpdateStatus(BaseModel):
    status: IssueStatus

class IssueAssign(BaseModel):
    user_id: int

class Issue(IssueBase):
    id: int
    project_id: int
    assigned_to: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

#issue comments
class CommentBase(BaseModel):
    message: str

class CommentCreate(CommentBase):
    user_id: int

class Comment(CommentBase):
    id: int
    issue_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True 
