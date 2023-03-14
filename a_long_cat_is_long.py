# function that receives text and returns a dictionary of length of each word


def count_words(text):
    newText = [letter for letter in text if letter.isalpha() or letter == ' ']
    newText = ''.join(newText)
    dictionary = {word: len(word) for word in newText.split()}
    return dictionary


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(text))
