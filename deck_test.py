import unittest
import cards

class TestDeck(unittest.TestCase):

    def test_deal_card(self):
        d1 = cards.Deck()
        d1.shuffle()
        c1 = d1.deal_card()

        self.assertEqual(len(d1.cards), 51)
        self.assertNotIn(c1, d1.cards)



if __name__=="__main__":
    unittest.main()

