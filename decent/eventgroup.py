from decent.instance import shared_decent_instance
from .exceptions import EventGroupDoesNotExistException


class EventGroup(dict):
    """ Read data about an event group on the chain

        :param str identifier: Identifier
        :param decent decent_instance: decent() instance to use when accesing a RPC

    """
    def __init__(
        self,
        identifier,
        lazy=False,
        decent_instance=None,
    ):
        self.decent = decent_instance or shared_decent_instance()
        self.cached = False

        if isinstance(identifier, str):
            self.identifier = identifier
            if not lazy:
                self.refresh()
        elif isinstance(identifier, dict):
            self.cached = False
            self.identifier = identifier.get("id")
            super(EventGroup, self).__init__(identifier)

    def refresh(self):
        assert self.identifier[:5] == "1.18.",\
            "Identifier needs to be of form '1.18.xx'"
        data = self.decent.rpc.get_object(self.identifier)
        if not data:
            raise EventGroupDoesNotExistException(self.identifier)
        super(EventGroup, self).__init__(data)
        self.cached = True

    def __getitem__(self, key):
        if not self.cached:
            self.refresh()
        return super(EventGroup, self).__getitem__(key)

    def items(self):
        if not self.cached:
            self.refresh()
        return super(EventGroup, self).items()

    def __repr__(self):
        return "<EventGroup %s>" % str(self.identifier)

    @property
    def sport(self):
        from .sport import Sport
        return Sport(self["sport_id"])


class EventGroups(list):
    """ List of all available EventGroups

        :param str sport_id: Sport ID (``1.16.xxx``)
    """
    def __init__(self, sport_id, decent_instance=None):
        self.decent = decent_instance or shared_decent_instance()
        self.eventgroups = self.decent.rpc.list_event_groups(sport_id)

        super(EventGroups, self).__init__([
            EventGroup(x, lazy=True, decent_instance=decent_instance)
            for x in self.eventgroups
        ])
