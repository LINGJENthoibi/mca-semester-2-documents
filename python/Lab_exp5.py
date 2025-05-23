def insert_card(sorted_cards, new_card):
    for i in range(len (sorted_cards)):
        if new_card < sorted_cards[i]:
            sorted_cards.insert(i, new_card)
            return
    sorted_cards.append(new_card)
cards = [3, 5, 8, 12]
print("Before:", cards)
insert_card(cards, 9)
print("After inserting 9:", cards)
