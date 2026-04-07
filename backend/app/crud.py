from sqlalchemy.orm import Session
from . import models, schemas

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#user management
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#project management
def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()     

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name, description=project.description, created_by=project.created_by)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

#issue management
def create_issue(db: Session, issue: schemas.IssueCreate):
    db_issue = models.Issue(
        title=issue.title,
        description=issue.description,
        status=issue.status,
        priority=issue.priority,
        project_id=issue.project_id,
        assigned_to=issue.assigned_to,
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

def get_project_issues(db: Session, project_id: int):
    return db.query(models.Issue).filter(models.Issue.project_id == project_id).all()

def get_issue(db: Session, issue_id: int):
    return db.query(models.Issue).filter(models.Issue.id == issue_id).first()

def update_issue_status(db: Session, issue_id: int, status: schemas.IssueStatus):
    issue = get_issue(db, issue_id)
    if issue:
        issue.status = status
        db.commit()
        db.refresh(issue)
    return issue

def assign_issue(db: Session, issue_id: int, user_id: int):
    issue = get_issue(db, issue_id)
    if issue:
        issue.assigned_to = user_id
        db.commit()
        db.refresh(issue)
    return issue

#issue comments
def create_comment(db: Session, issue_id: int, comment: schemas.CommentCreate):
    db_comment = models.Comment(
        issue_id=issue_id,
        user_id=comment.user_id,
        message=comment.message,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_issue_comments(db: Session, issue_id: int):
    return db.query(models.Comment).filter(models.Comment.issue_id == issue_id).all()