#Name: Chang Ge
#Uniqname: changgge

import unittest
import hw5_cards as cards
# create the Hand with an initial set of cards
class Hand:
    '''a hand for playing card 
    Class Attributes
    ---------------- 
    None 

    Instance Attributes
    ------------------- 
    init_card: list a list of cards'''
    def __init__(self, init_cards=[]): 
        self.init_cards = init_cards

    
    def add_card(self, card):
        '''add a card to the hand silently, fails if the card is already in the hand 
        Parameters 
        ------------------- 
        card: instance a card to add 
        
        Returns
        ------- 
        None''' 
        card_strs = []
        for c in self.init_cards:
            card_strs.append(cards.Card.__str__(c))
        if card.__str__() not in card_strs: 
            self.init_cards.append(card) 

    
    def remove_card(self, card):
        '''remove a card from the hand 
        Parameters 
        ------------------- 
        card: instance a card to remove 
        
        Returns
        -------
        the card, or None if the card was not in the Hand''' 
        card_strs = []
        for c in self.init_cards:
            card_strs.append(cards.Card.__str__(c))
        if card.__str__() in card_strs:
            i = card_strs.index(card.__str__())
            self.init_cards.pop(i)
            return card
        if card.__str__() not in card_strs:
            return None
    
    def draw(self, deck):
        '''draw a card from a deck and add it to the hand side effect: the deck will be depleted by one card 
        Parameters 
        ------------------- 
        deck: instance a deck from which to draw 
        
        Returns
        ------- 
        None''' 
        cards.Deck.shuffle(deck)
        d = cards.Deck.deal_card(deck,-1)
        self.init_cards.append(d)



