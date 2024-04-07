from fastapi import FastAPI


from api.routers import (
    accounts,
    issue_blockers,
    issue_labels,
    issue_relationships,
    issues,
    projects,
)

app = FastAPI()

app.include_router(accounts.router, tags=["Accounts"])
app.include_router(projects.router, tags=["Projects"])
app.include_router(issues.router, tags=["Issues"])
app.include_router(issue_relationships.router, tags=["Issue Relationships"])
app.include_router(issue_blockers.router, tags=["Issue Blockers"])
app.include_router(issue_labels.router, tags=["Issue Labels"])
