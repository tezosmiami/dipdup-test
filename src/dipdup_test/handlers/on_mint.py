
from dipdup.models import Transaction
from dipdup_test.types.tzbtc.parameter.mint import MintParameter
from dipdup_test.types.tzbtc.storage import TzbtcStorage
from dipdup.context import HandlerContext

async def on_mint(
    ctx: HandlerContext,
    mint: Transaction[MintParameter, TzbtcStorage],
) -> None:
    ...