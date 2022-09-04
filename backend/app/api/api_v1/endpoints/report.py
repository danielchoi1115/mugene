from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status
from app import crud, exceptions, schemas
from app.api import deps
from sqlalchemy.orm import Session
from app.crud.crud_workspace import CRUDWorkspace
from app import models
router = APIRouter()

# 3
@router.get("/{report_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.ReportOut)
def get_report(
    report_uuid: str, 
    db: Session = Depends(deps.get_db)
) -> models.Report:
    
    return crud.report.get_by_uuid(db=db, uuid=report_uuid)

@router.put("/{report_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.ReportOut)
def update_report(
    report_uuid: str,
    report_in: schemas.ReportUpdate,
    db: Session = Depends(deps.get_db)
) -> models.Report:
    
    report_obj = crud.report.get_by_uuid(db=db, uuid=report_uuid)
    report = crud.report.update(db=db, db_obj=report_obj, obj_in=report_in)

    return report

@router.delete("/{report_uuid}", status_code=status.HTTP_200_OK, response_model=schemas.ReportOut)
def delete_report(
    report_uuid: str,
    db: Session = Depends(deps.get_db)
) -> models.Report:
    
    report = crud.report.delete_by_uuid(db=db, uuid=report_uuid)

    return report


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReportOut)
def create_report(
    report_in: schemas.ReportCreate,
    reportdata_in: schemas.ReportdataCreate,
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_user),
    workspace: models.Workspace = Depends(deps.get_current_workspace),
) -> models.Report:

    reportdata = crud.reportdata.create(db=db, obj_in=reportdata_in)
    
    report = crud.report.create(
        db=db, 
        workspace_in=workspace, 
        user_in=user,
        reportdata_in=reportdata,
        obj_in=report_in
    )

    return report