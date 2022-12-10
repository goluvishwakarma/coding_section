# Date: 01-1-2021,

try:
    file = open("this.txt", 'r')

except EOFError as e:
    print("eof error")

except IOError as e:
    print("we can handle this error")

finally:
    print("this will be printed irrespective of the exceptions occurrence")
