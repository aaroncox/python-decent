from decent.instance import shared_decent_instance
from .account import Account
from .exceptions import CommitteeMemberDoesNotExistsException


class Committee(dict):
    """ Read data about a Committee Member in the chain

        :param str member: Name of the Committee Member
        :param decent decent_instance: decent() instance to use when accesing a RPC
        :param bool lazy: Use lazy loading

    """
    def __init__(
        self,
        member,
        decent_instance=None,
    ):
        self.member = member
        self.decent = decent_instance or shared_decent_instance()
        self.refresh()

    def refresh(self):
        account = Account(self.member)
        member = self.decent.rpc.get_committee_member_by_account(account["id"])
        if not member:
            raise CommitteeMemberDoesNotExistsException
        super(Committee, self).__init__(member)
        self.cached = True

    @property
    def account(self):
        return Account(self.member)
