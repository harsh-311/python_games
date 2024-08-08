from collections import defaultdict
import random



print("Hello & Welcome to the Die game!")

user_opinion = input("Would you like to play the game (press enter)? ").lower()

print("""\nSome rules are you must know before playing the game:)
    1) This game will be win whose player whose achieving 30 point first.Here point are calculated using 
    what your dies are arrived at when you play the game(ex: your die is 5 then your point is 5).
    2) If any player get 1 while die drawing then their turn is turnout and their totalpoint will be zero.
    3) If you want to terminate before the die 1 then your point will be calulated of your last turn.
    4) This cycle is repeated for all the players until the anyone will reach 30 points.
    5) If multiple players reach 30 points at one round then we conduct next round for only whose players who reach 30 points.\n""")
    
while True:
    try:    
         no_of_members = int(input("How many members are you playing(2-4)? "))
        
    except ValueError:
        print("Please enter a number of members.")
    else:
        if (no_of_members > 1) and (no_of_members < 5):
            break
        else:
            print("Please enter a number between 2 and 4.")
        
members = []
members.extend(list(range(1,no_of_members+1)))

users = defaultdict(int)
winner = 0
tem = True

def authenticate_member():
    global members
    global disqulified_members
    disqulified_members = []
    
    upper_win_point_count = 0
    for user, point in users.items():
        if point >= 30:
            upper_win_point_count += 1
    below_win_point_count = 0
    for user, point in users.items():
        if point < 30:
            below_win_point_count += 1
   
    if (upper_win_point_count == len(members)) or (below_win_point_count == len(members)):
        return
    
    qulified_members = []

    for user, point in users.items():
        
        if point >= 30:
            qulified_members.append(user)
        else:
            disqulified_members.append(user)
            

    if len(qulified_members) == 1:
        global winner
        winner = qulified_members[0]
        return True
    else:
        members.clear()
        members.extend(qulified_members)
        users.clear()
        print()
        print(f"It's next round and member {"number" if len(disqulified_members)==1 else "numbers"} {disqulified_members} is disqulified...")
        print()
        
auth_purpose = False
while tem:
    
    if auth_purpose:
        
        value = authenticate_member()
        if value:
            tem = False
    
    if tem:
        for player in members:
            auth_purpose = True
            points = 0
            print()
            print(f"Player number {player} it's your turn")
            print(f"Now your total points : {users[player]}")
            while True:
                user_turn = input(f"Would you like to draw die(y/n)? ").lower()
                if user_turn == 'n':
                    users[player] = users[player] + points
                    print(f"Now your total points is :{users[player]}")
                    break
                die_op = random.randint(1,6)
                if die_op == 1:
                    print("You have drawn 1 Your turn is now terminated:)")
                    users[player] = 0
                    print("Now your total balance is: 0")
                    break
                print(f"You have drawn die_number {die_op}.")
                points += die_op
                print(f"Now your point is {points}")

print(f"\nThe winner player number is {winner} and Whose achieved total {users[winner]} points.")
