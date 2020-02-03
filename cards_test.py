import unittest
import cards

class TestCard(unittest.TestCase):

    def testConstructCard(self):
        c1 = cards.Card(0, 2)
        c2 = cards.Card(1, 1)
        c3 = cards.Card(2, 10)
        c4 = cards.Card(3, 11)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")

        self.assertEqual(c3.suit, 2)
        self.assertEqual(c3.suit_name, "Hearts")
        self.assertEqual(c3.rank, 10)
        self.assertEqual(c3.rank_name, "10")

        self.assertEqual(c4.suit, 3)
        self.assertEqual(c4.suit_name, "Spades")
        self.assertEqual(c4.rank, 11)
        self.assertEqual(c4.rank_name, "Jack")

class TestDeck(unittest.TestCase):

    def testConstructDeck(self):
        pass


if __name__=="__main__":
    unittest.main()

