
from dipdup_test.types.tzbtc.parameter.transfer import TransferParameter
from dipdup.models import Transaction
from dipdup_test.types.tzbtc.storage import TzbtcStorage
from dipdup.context import HandlerContext

async def on_transfer(
    ctx: HandlerContext,
    transfer: Transaction[TransferParameter, TzbtcStorage],
) -> None:
    ...