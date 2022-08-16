import random
import time



end = False
cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
                return cards[random.randint(1,12)]
        
def calculate_score(card_list):
        for i in range(len(card_list)):
                if  card_list[i] == 11 and sum(card_list) > 21:
                        card_list.remove(11)
                        card_list.append(1)

        if sum(card_list) == 21:
                return 0
        else:
                return sum(card_list)

def bj_bust():
        global end
        if calculate_score(user_cards) == 0:
                print("Congratulations. You just got a BLACKJACK. You win!")
                end = True
        elif calculate_score(user_cards) > 21:
                print("BUST. You went over 21. You lose, GAME OVER.")
                end = True

def compare(user_score, computer_score):
        if user_score == computer_score:
                print("It's a draw.")
        elif calculate_score(user_cards) == 0:
                print("BLACKJACK. You win.")
        elif user_score > 21:
                print("You lose. Computer wins.")
        elif computer_score > 21:
                print("Computer loses. You win.")
        else:
                if user_score > computer_score:
                        print("Computer loses. You win.")
                else:
                       print("You lose. Computer wins.")
        global end
        end = True

# def play_again():
#         print("Do you want to play again?")
#         if choice.strip().lower() == "yes":
#                 pass #main()
#         elif choice.strip().lower() == "no":
#                 pass #quit

user_cards.append(deal_card())
user_cards.append(deal_card())


computer_cards.append(deal_card())
computer_cards.append(deal_card())

# print(user_cards)
# print(computer_cards)
# print(calculate_score())

print("Here are your cards:", user_cards, "  |   Here is your score:", calculate_score(user_cards))
print("Here is the dealer's first card:", computer_cards[0])
bj_bust()

print("Do you want to \"HIT\" or \"STICK\"?")
choice = input("---> ")

if choice.lower().strip() == "hit":
        user_cards.append(deal_card())
        print("Here are your cards:", user_cards, "  |   Here is your score:", calculate_score(user_cards))
        print("Here is the dealer's first card:", computer_cards[0])
        bj_bust()
        choice = input("---> ")

if choice.lower().strip() == "stick":
        print("Your final hand:", user_cards, "Final score:", calculate_score(user_cards))
        while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())
        print("Computer's final hand:", computer_cards, "Computer's final socre:", calculate_score(computer_cards))
        compare(calculate_score(user_cards), calculate_score(computer_cards))