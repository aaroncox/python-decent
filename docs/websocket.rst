******************
decentWebsocket
******************

This class allows subscribe to push notifications from the decent
node.

.. code-block:: python

    from pprint import pprint
    from decentapi.websocket import decentWebsocket

    ws = decentWebsocket(
        "wss://node.testnet.decent.eu",
        markets=[["1.3.0", "1.3.172"]],
        accounts=["xeroc"],
        objects=["2.0.x", "2.1.x"],
        on_market=pprint,
        on_account=print,
    )

    ws.run_forever()

Defintion
=========
.. autoclass:: decentapi.websocket.decentWebsocket
    :members:
    :undoc-members:
    :private-members:
    :special-members:
