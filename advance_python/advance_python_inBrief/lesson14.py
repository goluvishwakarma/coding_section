# Date: 01-01-2021
# Topic: Join Function: important

sample_lst = ['programming', 'coding', 'python', 'java', 'android', 'c nd c++']

'''
    Suppose we want the output will be:
    'programming nd coding nd python nd java nd c nd c++'
    
'''
# 1st approach:
for item in sample_lst:
    if item != 'c nd c++':  # '!=' or 'is not' both are same nd also their operation.
        print(item, "and", end=" ")
    else:
        print(item)

# 2nd approach:
print(" and ".join(sample_lst))  # highly_recommended

# NOTE: both the approaches will be have same output.
