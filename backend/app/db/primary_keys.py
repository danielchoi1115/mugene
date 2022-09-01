
from typing import Literal


class PKey:
    @property
    def blocks(self):
        return 'blocks.block_id'
    @property
    def members(self):
        return 'members.member_id'
    @property
    def paid_targets(self):
        return 'paid_targets.paid_target_id'
    @property
    def reports(self):
        return 'reports.report_id'
    @property
    def targets(self):
        return 'targets.target_id'
    @property
    def users(self):
        return 'users.user_id'
    @property
    def workspaces(self):
        return 'workspaces.workspace_uuid'
    @property
    def reportdata(self):
        return 'reportdata.reportdata_id'
pkey = PKey()