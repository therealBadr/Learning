import random
import time
from turtle import clear





def deal_card():
                cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                return cards[random.randint(1,12)]
        
def calculate_score(card_list):
        for i in range(len(card_list)):
                if  card_list[i] == 11 and sum(card_list) > 21:
                        card_list.remove(11)
                        card_list.append(1)

        if sum(card_list) == 21 and len(card_list) == 2:
                return 0
        return sum(card_list)

             

def compare(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
                return "You busted. You lose."
        if user_score == computer_score:
                return "It's a draw."
        elif user_score == 0:
                return "BLACKJACK. You win."
        elif computer_score == 0:
                return "BLACKJACK for the computer. You lose."
        elif user_score > 21:
                return "BUST. You lose."
        elif computer_score > 21:
                return "Computer busted. You win."
        elif user_score > computer_score:
                print("Computer loses. You win.")
        else:
                print("You lose. Computer wins.")
        


def main():

        end = False
        

        user_cards = []
        computer_cards = []

        for i in range(2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
        
        while end is False:
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)

                print("Here are your cards:", user_cards, "  |   Here is your score:", user_score)
                print("Here is the dealer's first card:", computer_cards[0])
                
                if user_score == 0 or user_score > 21 or computer_score == 0:
                        end = True
                else:
                        print("Do you want to \"HIT\" or \"STICK\"?")
                        choice = input("---> ")

                        if choice.lower().strip() == "hit":
                                user_cards.append(deal_card())
                        else:
                                end = True
                        

        while computer_score != 0 and computer_score < 17:
                                computer_cards.append(deal_card())
                                computer_score = calculate_score(computer_cards)
                                time.sleep(2)
                                print("Your final hand is:", user_cards, "Your final score is:", user_score)
                                print("Computer's final hand:", computer_cards, "Computer's final socre:", calculate_score(computer_cards))
                                print(compare(user_score, computer_score))
                                

print("Do you want to play the game again? (Yes/No)")
start = input("---> ")
while start.strip().lower() == "yes":
        clear()
        main()