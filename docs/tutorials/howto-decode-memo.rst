*****************
Decoding the Memo
*****************

In decent, memos are usually encrypted using a distinct memo key. That way,
exposing the memo private key will only expose transaction memos (for that key)
and not compromise any funds. It is thus safe to store the memo private key in
3rd party services and scripts.

Obtaining memo wif key from cli_wallet
======================================

The memo public key can be obtained from the cli_wallet account settings
or via command line:::

    get_account myaccount

in the cli wallet. The corresponding private key can be obtain from:::

    get_private_key <pubkey>

Note that the latter command exposes all private keys in clear-text wif.

That private key can be added to the pydecent wallet with:

.. code-block:: python

    from decent import Decent
    DCT = decent()
    # Create a new wallet if not yet exist
    DCT.wallet.create("wallet-decrypt-password")
    DCT.wallet.unlock("wallet-decrypt-password")
    DCT.wallet.addPrivateKey("5xxxxxxxxxxx")

Decoding the memo
=================

The memo is encoded with a DH-shared secret key. We don't want to go
into too much detail here, but a simple python module can help you here:

The encrypted memo can be decoded with:

.. code-block:: python

    from decent.memo import Memo
    transfer_operation = {
        'amount': {'amount': 100000, 'asset_id': '1.3.0'},
        'extensions': [],
        'fee': {'amount': 2089843, 'asset_id': '1.3.0'},
        'from': '1.2.18',
        'memo': {'from': 'DCT1894jUspGi6fZwnUmaeCPDZpke6m4T9bHtKrd966M7qYz665xjr',
                 'message': '5d09c06c4794f9bcdef9d269774209be',
                 'nonce': 7364013452905740719,
                 'to': 'DCT16MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV'},
        'to': '1.2.6'}
    memo = Memo(
        transfer_operation["from"],
        transfer_operation["to"],
    )
    memo.decent.wallet.unlock("wallet-decrypt-password")
    print(memo.decrypt(transfer_operation["memo"]))


Alternatively, the 'history' command on the *cli-wallet* API, exposes
the decrypted memo aswell.
