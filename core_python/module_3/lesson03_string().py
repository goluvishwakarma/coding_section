# Date: 11-01-2021
# Topic: string()

"""
    *. String() Function:
    string.replace("old_word", "new_word") - this function replace the old_word with new_word in the entire string.

    *.

"""

story = "once upon a time there was a pythons named code_with_python" \
        " who made a awesome projects"


print("length is: ", len(story))
print(story.endswith("projects"))

print("count is: ", story.count("o"))
print(story.capitalize())  # it will capitalize the 1st string_character

print(story.find("was"))  # it will return index of 1st occurrence of that word in that string
print(story.find("Was"))  # it will return -1, e.i not present in that string

print(story.replace("awesome", "outstanding"))
print(story.replace("a", "outstanding"))
