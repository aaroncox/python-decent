import datetime
from pprint import pprint
from decent import decent

DCT = decent(
    # this account creates the proposal
    proposer="xeroc",
    # Proposal needs to be approve within 1 hour
    proposal_expiration=60 * 5,
    # For testing, set this to true
    nobroadcast=False,
    # We want to bundle many operations into a single transaction
    bundle=True,
)
DCT.wallet.unlock("")

DCT.resolve_betting_market(
    "1.21.0",
    "win"
)

# Broadcast the whole transaction
pprint(
    DCT.txbuffer.broadcast()
)
