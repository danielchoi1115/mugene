
class ColumnBase:
    def __init__(self, id: str) -> None:
        self.id: str = id

class PKey:
    blocks = ColumnBase('blocks.block_id')
    members = ColumnBase('members.member_id')
    paid_targets = ColumnBase('paid_targets.paid_target_id')
    reports = ColumnBase('reports.report_id')
    targets = ColumnBase('targets.target_id')
    users = ColumnBase('users.user_id')
    workspaces = ColumnBase('workspaces.workspace_id')
        
pkey = PKey()