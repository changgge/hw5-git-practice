#Name: Chang Ge
#Uniqname: changgge

import unittest
import hw5_cards as cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = cards.Card(0, 2)
        c2 = cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")

    def test_q1(self):
        c = cards.Card(0,12)
        self.assertEqual(c.rank_name,'Queen')
    
    def test_q2(self):
        c = cards.Card(1,2)
        self.assertEqual(c.suit_name, "Clubs")

    def test_q3(self):
        c = cards.Card(3,13)
        self.assertEqual(cards.Card.__str__(c),'King of Spades')

    def test_q4(self):
        d = cards.Deck()
        self.assertEqual(len(d.cards),52)
    
    def test_q5(self):
        d = cards.Deck()
        self.assertTrue(cards.Deck.deal_card(d), cards.Card())
    
    def test_q6(self):
        d = cards.Deck()        
        cards.Deck.deal_card(d)
        self.assertEqual(len(d.cards),51)
    
    def test_q7(self):
        d = cards.Deck()        
        i = cards.Deck.deal_card(d,-1) #dealing the last card in the deck
        d.replace_card(i) #adding back the last card to the deck
        self.assertEqual(len(d.cards),52)
    
    def test_q8(self):
        d = cards.Deck()        
        d.replace_card(cards.Card(3,4)) #adding another card already in the deck
        self.assertEqual(len(d.cards),52)


if __name__=="__main__":
    unittest.main()