# date: 18.08.2022,  @author...

# counting the word occurrences


# quote
quote = "time is too slow for those who wait too swift for those who fear too long for" \
        "those who grieve too short for those who rejoicebut for those who love, time is eternity"

frequency_dict = {word: quote.split(" ").count(word) for word in quote.split(" ")}
print(frequency_dict, "\n")
