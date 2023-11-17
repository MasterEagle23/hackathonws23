from models.bet import Bet
from models.table import Table
import datetime


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)
    we = table.players[table.activePlayer]

    print(f"[{datetime.datetime.now()}]Cards: {we.cards}")

    bet_amount = table.minimumBet + (1/table.round) * we.stack
    print(f"{bet_amount}")

    return Bet(int(bet_amount))
