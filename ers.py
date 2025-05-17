import random

suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
face_cards = ["J", "Q", "K", "A"]
numeric_cards = [str(i) for i in range(2, 11)]
ranks = numeric_cards + face_cards

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Value:
    def __init__(self):
        self.count = 0

def card_generator():
    deck = [Card(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck[:26], deck[26:]

def facecard_counter(card):
    if card.rank == "J":
        return 1
    elif card.rank == "Q":
        return 2
    elif card.rank == "K":
        return 3
    elif card.rank == "A":
        return 4
    else:
        return 0

def same_value(pile):
    if len(pile) >= 2:
        return pile[-1].rank == pile[-2].rank
    return False

def sandwich(pile):
    if len(pile) >= 3:
        return pile[-1].rank == pile[-3].rank
    return False

def valid_slap(pile):
    return same_value(pile) or sandwich(pile)

def play_ers():
    import time
    player, computer = card_generator()
    pile = []
    turn = 0 

    while player and computer:
        print(f"\nPlayer: {len(player)} cards | Computer: {len(computer)} cards | Pile: {len(pile)} cards")
        if turn == 0:
            input("Your turn! Press Enter to play a card...")
            card = player.pop(0)
            print(f"You play: {card}")
        else:
            print("Computer's turn...")
            time.sleep(random.uniform(0.5, 1.2))
            card = computer.pop(0)
            print(f"Computer plays: {card}")

        pile.append(card)

        if card.rank in face_cards:
            challenge_player = 1 - turn 
            challenge_count = facecard_counter(card)
            face_winner = turn

            while challenge_count > 0 and player and computer:
                print(f"\nFace card challenge! {challenge_count} card(s) to play by {'You' if challenge_player == 0 else 'Computer'}")
                if challenge_player == 0:
                    input("Your challenge! Press Enter to play a card...")
                    next_card = player.pop(0)
                    print(f"You play: {next_card}")
                else:
                    print("Computer's challenge turn...")
                    time.sleep(random.uniform(0.5, 1.2))
                    next_card = computer.pop(0)
                    print(f"Computer plays: {next_card}")

                pile.append(next_card)

                if next_card.rank in face_cards:
                    
                    challenge_player = 1 - challenge_player
                    challenge_count = facecard_counter(next_card)
                    face_winner = 1 - challenge_player
                else:
                    challenge_count -= 1

                if valid_slap(pile):
                    if challenge_player == 0:
                        slap = input("Slap opportunity! Type 'slap' to slap, or press Enter to pass: ").strip().lower()
                        if slap == "slap":
                            print("You slap and win the pile!")
                            player += pile
                            pile = []
                            break
                        else:
                            time.sleep(random.uniform(0.3, 1.0))
                            if random.random() < 0.7:
                                print("Computer slaps and wins the pile!")
                                computer += pile
                                pile = []
                                break
                            else:
                                print("Computer missed the slap! Play continues.")
                    else:
                        time.sleep(random.uniform(0.3, 1.0))
                        if random.random() < 0.7:
                            print("Computer slaps and wins the pile!")
                            computer += pile
                            pile = []
                            break
                        else:
                            print("Computer missed the slap! Play continues.")

            if challenge_count == 0 and pile:
                print(f"Face card challenge won by {'You' if face_winner == 0 else 'Computer'}!")
                if face_winner == 0:
                    player += pile
                else:
                    computer += pile
                pile = []
            turn = 1 - face_winner 
            continue

        if valid_slap(pile):
            if turn == 0:
                slap = input("Slap opportunity! Type 'slap' to slap, or press Enter to pass: ").strip().lower()
                if slap == "slap":
                    print("You slap and win the pile!")
                    player += pile
                    pile = []
                else:
                    time.sleep(random.uniform(0.3, 1.0))
                    if random.random() < 0.7:
                        print("Computer slaps and wins the pile!")
                        computer += pile
                        pile = []
                    else:
                        print("Computer missed the slap! Play continues.")
            else:
                time.sleep(random.uniform(1.0, 2.0))
                if random.random() < 0.5:
                    print("Computer slaps and wins the pile!")
                    computer += pile
                    pile = []
                else:
                    print("Computer missed the slap! Play continues.")

        turn = 1 - turn

    if player:
        print("You win the game!")
    else:
        print("Computer wins the game!")


if __name__ == "__main__":
    play_ers()


        
