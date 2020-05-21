run1=int(input("Enter the runs made by player 1 in 60 balls"))
run2=int(input("Enter the runs made by player 2 in 60 balls"))
run3=int(input("Enter the runs made by player 3 in 60 balls"))
sr1=run1*100/60
sr2=run2*100/60
sr3=run3*100/60
print("Strike rate of player 1 is",sr1)
print("Strike rate of player 2 is",sr2)
print("Strike rate of player 3 is",sr3)
print("Runs scored by player 1 if they were given 60 more balls is",run1*2)
print("Runs scored by player 2 if they were given 60 more balls is",run2*2)
print("Runs scored by player 3 if they were given 60 more balls is",run3*2)
print("Maximum no. of sixes player 1 could hit",run1//6)
print("Maximum no. of sixes player 2 could hit",run2//6)
print("Maximum no. of sixes player 3 could hit",run3//6)