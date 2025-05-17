functions: card_generator(), facecard_counter(value), same_value(value,card), sandwich(value,card), jack(card), queen(card), king(card), ace(card)
classes: card, value

card_generator() would generate the cards for the game.
facecard_counter() would track the amount of face cards placed down, the jack() queen() king() ace() functions would rely on this function because 
each face card has a different function
same_value() and sandwich() would determine if the pile meets the right conditions to be slapped

card would be the card that's placed down
value would be the amount of cards that are similar to each other (numerical and face cards)
