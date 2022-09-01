from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.api.api_v1.endpoints.workspace import get_workspace
from app.schemas.dbref import RefWorkspace

from app.api import deps
from sqlalchemy.orm import Session
from app.crud.crud_workspace import CRUDWorkspace
from app import models
router = APIRouter()

# 3
@router.get("/{report_id}", status_code=status.HTTP_200_OK, response_model=schemas.WorkspaceOut)
def get_report(
    report_id: int, 
    db: Session = Depends(deps.get_db)
) -> models.Report:
    
    return crud.report.get(db=db, id=report_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReportOut)
def create_report(
    report_in: schemas.ReportCreate,
    reportdata_in: schemas.ReportdataCreate,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_user),
    workspace: models.Workspace = Depends(deps.get_current_workspace),
) -> models.Report:
    """
    Root Get
    """
    reportdata = crud.reportdata.create(db=db, obj_in=reportdata_in)
    
    report = crud.report.create(
        db=db, 
        workspace_in=workspace, 
        user_in=user,
        reportdata_in=reportdata,
        obj_in=report_in
    )

    return report