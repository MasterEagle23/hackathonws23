from models.bet import Bet
from models.table import Table


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)
    we = table.players[table.activePlayer]

    print(f"Cards: {we.cards}")

    bet_amount = table.minimumBet + (1/table.round) * we.stash
    print(f"{bet_amount}")

    return Bet(int(bet_amount))
