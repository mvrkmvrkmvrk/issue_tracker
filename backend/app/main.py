from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

#user management
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

#project management
@app.post("/projects/", response_model=schemas.Project) 
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/", response_model=list[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db=db, skip=skip, limit=limit)

@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project   

#issue management
# POST /issues - Create an issue
@app.post("/issues", response_model=schemas.Issue)
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    return crud.create_issue(db, issue)

# GET /projects/{project_id}/issues - Get all issues for a project
@app.get("/projects/{project_id}/issues", response_model=list[schemas.Issue])
def get_project_issues(project_id: int, db: Session = Depends(get_db)):
    return crud.get_project_issues(db, project_id)

# PUT /issues/{issue_id}/status - Update issue status
@app.put("/issues/{issue_id}/status", response_model=schemas.Issue)
def update_issue_status(issue_id: int, status_update: schemas.IssueUpdateStatus, db: Session = Depends(get_db)):
    issue = crud.update_issue_status(db, issue_id, status_update.status)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue

# PUT /issues/{issue_id}/assign - Assign issue to a user
@app.put("/issues/{issue_id}/assign", response_model=schemas.Issue)
def assign_issue(issue_id: int, assignment: schemas.IssueAssign, db: Session = Depends(get_db)):
    issue = crud.assign_issue(db, issue_id, assignment.user_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue

# GET /issues/{issue_id} - Get issue details
@app.get("/issues/{issue_id}", response_model=schemas.Issue)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = crud.get_issue(db, issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue

#issue comments
# POST /issues/{issue_id}/comments - Add comment to issue
@app.post("/issues/{issue_id}/comments", response_model=schemas.Comment)
def add_comment(issue_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    # Ensure issue exists
    issue = crud.get_issue(db, issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return crud.create_comment(db, issue_id, comment)

# GET /issues/{issue_id}/comments - Get all comments
@app.get("/issues/{issue_id}/comments", response_model=list[schemas.Comment])
def get_comments(issue_id: int, db: Session = Depends(get_db)):
    issue = crud.get_issue(db, issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return crud.get_issue_comments(db, issue_id)





