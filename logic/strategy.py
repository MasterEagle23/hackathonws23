from models.bet import Bet
from models.table import Table


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    print(f"Cards: {table.players.get(table.activePlayer).cards}")

    bet_amount = table.minimumBet + (1/table.round) * table.activePlayer.stash
    print(f"{bet_amount}")

    return Bet(int(bet_amount))
