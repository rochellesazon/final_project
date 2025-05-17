Logic: The objective of the game is to obtain all 52 cards in the deck through slapping the central card pile before the other player gets a chance or through the special functions of face cards.
For the sake of making the project feasible in the timeframe I have, I'll be coding the game of Egyptian Ratslap (ERS) as a two player game. 
The deck of 52 cards will be split into 2 decks for each player to play with, meaning both players will start with 26 cards in their hands. 
Players then will take turns placing cards face-up in the middle, forming a central card pile that players can slap to claim the pile for themselves. 
In order to be able to slap the pile, the two top-most cards must be of the same numerical value or a card of a different value must be "sandwiched" between cards of the same value.
The first to slap the pile gets the pile to themselves. If the slapped pile does not meet the conditions above, the player who slapped the pile must "burn" a card (place one of their cards down on the pile).
Face cards (Jack, Queen. King, Ace) have special functions when placed down. If a Jack is placed down, the next player places down a card to determine if the pile goes to the player who placed down the Jack.
If a non face card is placed on top of the Jack, the whole central card pile goes to the one who placed down the Jack. If another face card is placed down instead, the same process would occur.
For a Queen, 2 cards have to be placed down, a King would be 3 cards, and an Ace would be 4 cards. The game ends once one player holds all the cards in the deck in their hands.

Functions: card_generator(), facecard_counter(value), same_value(value,card), sandwich(value,card), jack(card), queen(card), king(card), ace(card)

Example use cases: Genuinely, I think someone would really only use this for entertainment purposes. If they just want to play a game when they're bored, this game would definitely engage their minds.

Does my program take data as input?
  
