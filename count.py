import random

decks = 6
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4 * decks
tens = [10, "J", "Q", "K"]
starting_cards = len(cards)
random.shuffle(cards)
running_count = 0
shoe_change = 0
true_count = 0
player_wins = 0
dealer_wins = 0
ties = 0
bank = 6000
player = []
dealer = []
first_hand = []
second_hand = []
second_hand_value = 0
first_hand_value = 0
first_hand_bust = 0
second_hand_bust = 0
first_hand_bet = 0
second_hand_bet = 0
split = 0
lose = 0
games = 0

while True:
    first_hand.clear()
    second_hand.clear()
    dealer.clear()
    player.clear()
    blackjack = 0
    player_value = 0
    dealer_value = 0
    bust = 0
    ace_check = 0
    bet_insurance = 0
    insurance = 0
    while True:
        bet = input("Place your bet: ")
        if not bet.isdigit() or int(bet) < 10:
            print("Enter a valid number!")
        else:
            bet = int(bet)
            break
    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())
    print(dealer[0])
    shoe_change += 4

    # DEALING THE CARDS ====================================================================================
    for c in player:
        if c in tens:
            player_value += 10
            running_count -= 1
        elif c == "A":
            running_count -= 1
            if player[0] == player[1]:
                player_value = 12
            else:
                player_value += 11
        else:
            player_value += c
            if c <= 6:
                running_count += 1
    for c in dealer:
        if c in tens:
            running_count -= 1
            dealer_value += 10
        elif c == "A":
            running_count -= 1
            if dealer[0] == dealer[1]:
                dealer_value = 12
            else:
                dealer_value += 11
        else:
            dealer_value += c
            if c <= 6:
                running_count += 1

    # PLAYER'S TURN ==========================================================================================
    print(player)
    if dealer[0] == "A":
        insurance = input("Would you like to buy insurance (y/n): ").lower()
        if insurance == "y":
            bet_insurance = bet / 2
            bank -= bet_insurance
    if (player_value == 21 and len(player) == 2) or (dealer_value == 21 and len(dealer) == 2):
        blackjack = 1
    else:
        print("You have", player_value)
        ace_check = 0
        t = 0
        second_hand_value = 0
        first_hand_value = 0
        first_hand_bust = 0
        second_hand_bust = 0
        second_hand_bet = 0
        first_hand_bet = 0
        first_hand.clear()
        second_hand.clear()
        split = 0
        lose = 0
        while True and split != 1:
            if player[0] == player[1] or ((player[0] in tens) and (player[1] in tens)):
                if len(player) != 2:
                    while True:
                        q = input("Hit(y) or stand(n): ").lower()
                        if q != "y" and q != "n":
                            print("Enter a correct move")
                        else:
                            break
                else:
                    while True:
                        q = input("Hit(y), split(s), double(d) or stand(n): ").lower()
                        if q != "y" and q != "n" and q != "d" and q != "s":
                            print("Enter a correct move")
                        else:
                            break
            elif (player_value <= 11 or ("A" in player)) and len(player) == 2:
                while True:
                    q = input("Hit(y), double(d) or stand(n): ").lower()
                    if q != "y" and q != "n" and q != "d":
                        print("Enter a correct move")
                    else:
                        break
            else:
                while True:
                    q = input("Hit(y) or stand(n): ").lower()
                    if q != "y" and q != "n":
                        print("Enter a correct move")
                    else:
                        break
            if q == "y":
                shoe_change += 1
                p = cards.pop()
                player.append(p)
                if ace_check == 0:
                    for i in player:
                        if i == "A":
                            t = 1
                            break
                if p in tens:
                    running_count -= 1
                    player_value += 10
                    if t == 1 and player_value > 21:
                        player_value -= 10
                        ace_check = 1
                        t = 0
                elif p == "A":
                    running_count -= 1
                    player_value += 11
                    if player_value > 21:
                        player_value -= 10
                        if player_value > 11 and (10 in player or "J" in player or "Q" in player or "K" in player):
                            ace_check = 1
                            t = 0
                else:
                    player_value += p
                    if t == 1 and player_value > 21:
                        player_value -= 10
                        t = 0
                        ace_check = 1
                    if p <= 6:
                        running_count += 1
                print(player)
                if player_value <= 21:
                    print("You have", player_value)
                    if player_value == 21:
                        break
                else:
                    print("You busted. Good luck next time!")
                    dealer_wins += 1
                    bank -= bet
                    bust = 1
                    break
            elif q == "d":
                shoe_change += 1
                bet *= 2
                print("You double your bet and you only get one card. Good luck!")
                p = cards.pop()
                player.append(p)
                for i in player:
                    if i == "A":
                        t = 1
                        break
                if p in tens:
                    running_count -= 1
                    player_value += 10
                    if t == 1 and player_value > 21:
                        player_value -= 10
                elif p == "A":
                    running_count -= 1
                    player_value += 11
                    if player_value > 21:
                        player_value -= 10
                else:
                    player_value += p
                    if t == 1 and player_value > 21:
                        player_value -= 10
                    if p <= 6:
                        running_count += 1
                print(player)
                if player_value <= 21:
                    print("You have", player_value)
                    break
                else:
                    print("You busted. Good luck next time!")
                    dealer_wins += 1
                    bank -= bet
                    bust = 1
                    break
            elif q == "s":
                split = 1
                lose = 0
                print("You play two hands")
                first_hand.append(player[0])
                second_hand.append(player[1])
                first_hand.append(cards.pop())
                second_hand.append(cards.pop())
                shoe_change += 2
                if first_hand[0] == second_hand[0] == "A":
                    print("You only get one card with no Blackjack")
                    for i in range(2):
                        hand_bet = bet
                        if i == 0:
                            hand = first_hand
                            hand_value = first_hand_value
                        else:
                            hand = second_hand
                            hand_value = second_hand_value
                        print(hand)
                        for c in hand:
                            if c in tens:
                                hand_value += 10
                                running_count -= 1
                            elif c == "A":
                                running_count -= 1
                                if hand[0] == hand[1]:
                                    hand_value = 12
                                else:
                                    hand_value += 11
                            else:
                                hand_value += c
                                if c <= 6:
                                    running_count += 1
                        print("You have", hand_value)
                else:
                    for i in range(2):
                        move = 0
                        hand_bet = bet
                        if i == 0:
                            hand = first_hand
                            hand_value = first_hand_value
                        else:
                            hand = second_hand
                            hand_value = second_hand_value
                        print(hand)
                        for c in hand:
                            if c in tens:
                                hand_value += 10
                                running_count -= 1
                            elif c == "A":
                                running_count -= 1
                                if hand[0] == hand[1]:
                                    hand_value = 12
                                else:
                                    hand_value += 11
                            else:
                                hand_value += c
                                if c <= 6:
                                    running_count += 1
                        if hand_value == 21:
                            move = 1
                            if i == 0:
                                first_hand_value = hand_value
                            else:
                                second_hand_value = hand_value
                            print("You have", hand_value)
                        else:
                            if i == 0:
                                print("On the first hand you have", hand_value)
                            else:
                                print("On the second hand you have", hand_value)
                            ace_check = 0
                            t = 0
                            while move == 0:
                                if len(hand) == 2:
                                    while True:
                                        q2 = input("Hit(y), double(d) or stand(n): ").lower()
                                        if q2 != "y" and q2 != "n" and q2 != "d":
                                            print("Enter a correct move")
                                        else:
                                            break
                                else:
                                    while True:
                                        q2 = input("Hit(y), stand(n): ").lower()
                                        if q2 != "y" and q2 != "n":
                                            print("Enter a correct move")
                                        else:
                                            break
                                if q2 == "y":
                                    shoe_change += 1
                                    p = cards.pop()
                                    hand.append(p)
                                    if ace_check == 0:
                                        for v in hand:
                                            if v == "A":
                                                t = 1
                                                break
                                    if p in tens:
                                        running_count -= 1
                                        hand_value += 10
                                        if t == 1 and hand_value > 21:
                                            hand_value -= 10
                                            ace_check = 1
                                            t = 0
                                    elif p == "A":
                                        running_count -= 1
                                        hand_value += 11
                                        if hand_value > 21:
                                            hand_value -= 10
                                            if hand_value > 11 and (10 in hand or "J" in hand or "Q" in hand or "K" in hand):
                                                ace_check = 1
                                                t = 0
                                    else:
                                        hand_value += p
                                        if t == 1 and hand_value > 21:
                                            hand_value -= 10
                                            t = 0
                                            ace_check = 1
                                        if p <= 6:
                                            running_count += 1
                                    print(hand)
                                    if hand_value <= 21:
                                        print("You have", hand_value)
                                        if hand_value == 21:
                                            move = 1
                                    else:
                                        print("This hand busted")
                                        lose += 1
                                        move = 1
                                        bank -= bet
                                        if i == 0:
                                            first_hand_bust = 1
                                        else:
                                            second_hand_bust = 1
                                elif q2 == "d":
                                    move = 1
                                    shoe_change += 1
                                    ace_check = 0
                                    hand_bet = bet*2
                                    if i == 0:
                                        first_hand_bet = hand_bet
                                    else:
                                        second_hand_bet = hand_bet
                                    t = 0
                                    p = cards.pop()
                                    hand.append(p)
                                    if ace_check == 0:
                                        for v in hand:
                                            if v == "A":
                                                t = 1
                                                break
                                        if p in tens:
                                            running_count -= 1
                                            hand_value += 10
                                            if t == 1 and hand_value > 21:
                                                hand_value -= 10
                                                ace_check = 1
                                                t = 0
                                        elif p == "A":
                                            running_count -= 1
                                            hand_value += 11
                                            if hand_value > 21:
                                                hand_value -= 10
                                        else:
                                            hand_value += p
                                            if t == 1 and hand_value > 21:
                                                hand_value -= 10
                                                t = 0
                                                ace_check = 1
                                            if p <= 6:
                                                running_count += 1
                                        print("You double in this hand")
                                        print(hand)
                                        print("You have", hand_value)
                                elif q2 == "n":
                                    if i == 0:
                                        first_hand_value = hand_value
                                    else:
                                        second_hand_value = hand_value
                                    move = 1
            elif q == "n":
                break

    # DEALER'S TURN ============================================================================================
    if blackjack == 1:
        print(dealer)
    else:
        if bust == 0:
            ace_check = 0
            t = 0
            print(dealer)
            if dealer_value == 21 and len(dealer) == 2:
                print("Dealer has a Blackjack")
            elif dealer_value > 16:
                print("Dealer has", dealer_value)
            else:
                while dealer_value <= 16:
                    shoe_change += 1
                    p = cards.pop()
                    dealer.append(p)
                    if ace_check == 0:
                        for i in dealer:
                            if i == "A":
                                t = 1
                                break
                    if p in tens:
                        running_count -= 1
                        dealer_value += 10
                        if t == 1 and dealer_value > 21:
                            dealer_value -= 10
                            ace_check = 1
                            t = 0
                    elif p == "A":
                        running_count -= 1
                        dealer_value += 11
                        if dealer_value > 21:
                            dealer_value -= 10
                            if dealer_value > 11 and (10 in dealer or "J" in dealer or "Q" in dealer or "K" in dealer):
                                ace_check = 1
                                t = 0
                    else:
                        dealer_value += p
                        if t == 1 and dealer_value > 21:
                            dealer_value -= 10
                            t = 0
                            ace_check = 1
                        if p <= 6:
                            running_count += 1
                if dealer_value > 21:
                    print(dealer)
                    print("Dealer busts. You win!")
                    player_wins += 1
                    bank += bet
                else:
                    print(dealer)
                    print("Dealer has", dealer_value)
        else:
            print(dealer)

    # COMPARING THE RESULTS ========================================================================================
    if (dealer_value == 21 and len(dealer) == 2 and player_value == 21 and len(
            player) == 2):
        if bet_insurance != 0:
            print("Insurance pays you the original bet")
            bank += bet
        else:
            print("Tie!")
    elif dealer_value == 21 and len(dealer) == 2:
        if dealer[0] == "A" and bet_insurance != 0:
            print("Dealer has a Blackjack. Insurance returns your bet")
            bank += bet_insurance
        else:
            print("Dealer has a Blackjack. Good luck next time!")
            dealer_wins += 1
            bank -= bet
    elif player_value == 21 and len(player) == 2:
        print("You have a Blackjack. You win!")
        player_wins += 1
        bank += bet * 1.5
    elif split == 1:
        for i in range(2):
            if i == 0:
                hand = first_hand
                hand_value = first_hand_value
                hand_bust = first_hand_bust
                hand_bet = first_hand_bet
            else:
                hand = second_hand
                hand_value = second_hand_value
                hand_bust = second_hand_bust
                hand_bet = second_hand_bet
            if hand_bust == 0:
                if 22 > dealer_value > hand_value:
                    bank -= hand_bet
                    lose += 1
                elif 22 > hand_value > dealer_value:
                    bank += hand_bet
                elif hand_value == dealer_value:
                    continue
        if lose == 0:
            print("You win both hands! Congratulations!")
            player_wins += 1
        elif lose == 1:
            print("You win one hand. Congratulations!")
        else:
            print("You lost both hands. Good luck next time!")
            dealer_wins += 1
    elif dealer_value == player_value:
        print("Tie!")
        ties += 1
    elif 22 > dealer_value > player_value:
        print("Dealer wins. Good luck next time!")
        dealer_wins += 1
        bank -= bet
    elif 22 > player_value > dealer_value:
        print("You win! Congratulations!")
        player_wins += 1
        bank += bet
    games += 1
    print("Running count:", running_count)
    print("True count:", running_count / (len(cards) / 52))
    if shoe_change >= starting_cards / 2 or bank <= 0:
        break
    print("=================================================================================================")
print("Total games:", games)
print("Dealer wins:", dealer_wins)
print("Player wins:", player_wins)
print("Ties:", ties)
print("Wallet:", bank)
