# Date: 01-1-2021,

try:
    print("i will try code ")

except Exception as e:
    print("i will run only if try block fails")

else:
    print("i will run only if there is no exception. Use this to run code which should nly"
          " execute if there is no exception")

finally:
    print("This will be printed in every case")
