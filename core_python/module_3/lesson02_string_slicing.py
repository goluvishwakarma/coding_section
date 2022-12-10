# Date: 11-01-2021
# Topic: slicing with skip value:

"""
    *. slicing with skip value:
    we can provide a skip value as a part of our slice like thi.
            word = "amazing"
            word[1:6:2]  --- mzn
            
    *. other advance slicing techniques:
            word = "amazing"
            word[:6] ----> word[0:6] ----> 'amazing'
            word[0:] ----> word[0:6] ----> 'amazing'

"""
word = "amazing"
print(word[1:5:1])
print(word[0:6:2])

print(word[0:6:3])
