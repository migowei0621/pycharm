import collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=0, hearts=1, diamonds=2, clubs=3)
def spades_low(card):
        revl = []
        for c in reversed(FrenchDeck.ranks):
            revl.append(c)
        rank_value = revl.index(card.rank)
        return rank_value*len(suit_values) + suit_values[card.suit]
def main():

    fr = FrenchDeck()
    #for card  in reversed(FrenchDeck.ranks):
     #   print(card)

    for card in sorted(fr, key=spades_low()):
        print(card)



if __name__ =='__main__':
    main()