# Conditional Statement
print("Type front or back or anything")
print('Enter Your Command : ' , end="")
robot_move = input()
if robot_move == "front" :
    print("Moving Front")
elif robot_move == "back" :
    print("Moving Back")
else:
    print("Stand Still")
