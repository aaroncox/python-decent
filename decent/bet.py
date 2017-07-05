from decent.instance import shared_decent_instance
from .exceptions import BetDoesNotExistException


class Bet(dict):
    """ Read data about a Bet on the chain

        :param str identifier: Identifier
        :param decent decent_instance: decent() instance to use when accesing a RPC

    """
    def __init__(
        self,
        identifier,
        decent_instance=None,
    ):
        self.identifier = identifier
        self.decent = decent_instance or shared_decent_instance()
        self.refresh()

    def refresh(self):
        assert self.identifier[:5] == "1.22.",\
            "Identifier needs to be of form '1.22.xx'"
        data = self.decent.rpc.get_object(self.identifier)
        if not data:
            raise BetDoesNotExistException(self.identifier)
        dict.__init__(data)
