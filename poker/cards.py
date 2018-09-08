#how do we represent cards in code
# a characteristic is an attribute so we need to make a self of it

class Card:
    def __init__(
        self,
        suit,
        value,
    ):
        self.suit = suit
        self.value = value

    def __repr__(
        self,
    ):
        return '{}<{} of {}s>'.format(
            self.__class__.__name__,
            self.value.name,
            self.suit.name,
        )

    def __eq__(
        self,
        other,
    ):
        return self.value == other.value

    def __gt__(
        self,
        other,
    ):
        return self.value > other.value


class CardSuit:
    def __init__(
        self,
        name,
    ):
        self.name = name


suits = [
    CardSuit('Club'),
    CardSuit('Diamond'),
    CardSuit('Heart'),
    CardSuit('Spade'),
]


class CardValue:
    def __init__(
        self,
        value,
        name,
    ):
        self.value = value
        self.name = name

    def __eq__(
        self,
        other,
    ):
        return self.value == other.value

    def __gt__(
        self,
        other,
    ):
        return self.value > other.value


card_names = [
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace',
]

values = [
    CardValue(
        value,
        name,
    )
    for value, name in enumerate(
        card_names,
        2,
    )
]
deck = [
    Card(
        suit,
        value,
    )
    for suit in suits
    for value in values
]
