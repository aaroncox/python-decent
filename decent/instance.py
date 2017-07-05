import Decent as DCT

_shared_decent_instance = None


def shared_decent_instance():
    """ This method will initialize ``_shared_decent_instance`` and return it.
        The purpose of this method is to have offer single default
        decent instance that can be reused by multiple classes.
    """
    global _shared_decent_instance
    if not _shared_decent_instance:
        _shared_decent_instance = DCT.decent()
    return _shared_decent_instance


def set_shared_decent_instance(decent_instance):
    """ This method allows us to override default decent instance for all users of
        ``_shared_decent_instance``.

        :param decent.decent.decent decent_instance: decent instance
    """
    global _shared_decent_instance
    _shared_decent_instance = decent_instance
