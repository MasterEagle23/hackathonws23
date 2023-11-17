from models.bet import Bet
from models.table import Table


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    bet_amount = table.minimumBet + (1/table.round) * table.activePlayer.stash
    print(f"{bet_amount}")

    return Bet(bet_amount)
