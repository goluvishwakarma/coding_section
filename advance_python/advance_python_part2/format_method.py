# Date: 05-01-2021
# Topic: format_method.
"""
    *. format method(string):
    format the values inside the string into a desired output.
            template.format(p1, p2 ....)

    Example:
        "{} is a good {}".format("golu", "programmer") Output: golu is a good programmer
        "{1} is a good {0}".format("golu", "programmer") Output:  programmer is a good golu NOTE,

"""
name = "golu"
lang = "python"
work = "development"
# a = f"this is {name}"  # f-string
a = "this is {}".format(name)

prompt = "this is {0} and he is interested to learn {1} nd {2}".format(name, lang, work)
print(prompt)  # here we can also change the order
