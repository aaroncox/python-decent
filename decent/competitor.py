from decent.instance import shared_decent_instance
from .exceptions import CompetitorDoesNotExistException


class Competitor(dict):
    """ Read data about a competitor on the chain

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
        assert self.identifier[:5] == "1.17.",\
            "Identifier needs to be of form '1.17.xx'"
        data = self.decent.rpc.get_object(self.identifier)
        if not data:
            raise CompetitorDoesNotExistException(self.identifier)
        dict.__init__(data)
