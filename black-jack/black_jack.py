"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def get_card_value(card, hand=False):
    card_map = {"J": 10, "Q": 10, "K": 10, "A": 1}
    if hand:
        card_map["A"] = 11

    if card in card_map:
        return card_map[card]
    return int(card)


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    return get_card_value(card)


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_1 = get_card_value(card_one)
    card_2 = get_card_value(card_two)

    if card_1 == card_2:
        return card_one, card_two

    return card_one if card_1 > card_2 else card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_1 = get_card_value(card_one, hand=True)
    card_2 = get_card_value(card_two, hand=True)
    return 1 if card_1 + card_2 + 11 > 21 else 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    TEN_CARD = {"J", "Q", "K", "10"}
    return (card_one == "A" and card_two in TEN_CARD) or (
        card_two == "A" and card_one in TEN_CARD
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    TEN_CARD = {"J", "Q", "K", "10"}
    card_1 = "10" if card_one in TEN_CARD else card_one
    card_2 = "10" if card_two in TEN_CARD else card_two

    return card_1 == card_2


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_1 = get_card_value(card_one)
    card_2 = get_card_value(card_two)
    return card_1 + card_2 in range(9, 12)
