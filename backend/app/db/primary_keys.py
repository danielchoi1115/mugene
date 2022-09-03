
from typing import Literal


class PKey:
    @property
    def files_id(self):
        return 'files.file_id'
    @property
    def members_id(self):
        return 'members.member_id'
    @property
    def paid_targets_id(self):
        return 'paid_targets.paid_target_id'
    @property
    def reports_id(self):
        return 'reports.report_id'
    @property
    def targets_id(self):
        return 'targets.target_id'
    @property
    def users_id(self):
        return 'users.user_id'
    @property
    def workspaces_id(self):
        return 'workspaces.workspace_uuid'
    @property
    def reportdata_id(self):
        return 'reportdata.reportdata_id'
    @property
    def files_uuid(self):
        return 'files.file_uuid'
    @property
    def members_uuid(self):
        return 'members.member_uuid'
    @property
    def paid_targets_uuid(self):
        return 'paid_targets.paid_target_uuid'
    @property
    def reports_uuid(self):
        return 'reports.report_uuid'
    @property
    def targets_uuid(self):
        return 'targets.target_uuid'
    @property
    def users_uuid(self):
        return 'users.user_uuid'
    @property
    def workspaces_uuid(self):
        return 'workspaces.workspace_uuid'
    @property
    def reportdata_uuid(self):
        return 'reportdata.reportdata_uuid'
pkey = PKey()