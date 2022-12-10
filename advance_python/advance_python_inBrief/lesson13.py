# Date: 01-01-2021
# Topic: Format Function

users = ['rohan das', 'anjali sharma', 'skill f', 'neha', 'shubham']
computer = ['raspberry pi', 'android', 'windows', 'macOs', '100rs wala computer']

# in normal-way:
# for i in range(0, len(users)):
#     print("Computer used by", users[i], "is", computer[i])

# in python_ic_way:
for i in range(0, len(users)):
    # template = "computer used by {} is {}".format(users[i], computer[i])
    template = "computer used by {1} is {0}"  # here we can change the order, as w done
    print(template.format(users[i], computer[i]))


