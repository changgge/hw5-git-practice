#Name: Chang Ge
#Uniqname: changgge

import unittest
import hw5_cards_ec1 as cards_ec1
import hw5_cards as cards

class TestCard(unittest.TestCase):

    def test_init(self):
        h = cards_ec1.Hand([])
        self.assertEqual(len(h.init_cards),0)
    
    def test_addcard(self):
        h = cards_ec1.Hand()
        h.add_card(cards.Card(3,4))
        self.assertEqual(len(h.init_cards),1)

    def test_removecard(self):
        h = cards_ec1.Hand([cards.Card(1,2)])
        card = cards.Card(1,2)
        h.remove_card(card)
        self.assertEqual(len(h.init_cards),0)
    
    def test_draw(self):
        h = cards_ec1.Hand([])
        d = cards.Deck()
        h.draw(d)
        self.assertEqual(len(d.cards),51)
        self.assertEqual(len(h.init_cards),1)


if __name__=="__main__":
    unittest.main()



