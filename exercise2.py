# Create a function that counts how many distinct words are in the string below, then outputs a dictionary
# with the words as the key and the value as the amount of times that word appears in the string.
# Example Output:{'in': 1, 'computing': 1, 'a': 5, ...}

a_text = 'In computing, a hash table hash map is a data structure in computing which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def count_words(string):
    # split the string into words
    words = string.split()

    # create an empty dictionary to store word counts
    word_count = {}

    # go through the words and update the counts
    for word in words:
        # change the word to lowercase to ensure case-insensitivity
        word = word.lower()

        # see if the word is already in the dictionary
        if word in word_count:
            # if it is, increase the count
            word_count[word] += 1
        else:
            # if not add it to the dictionary with a count of 1
            word_count[word] = 1
    return word_count


# usage:
result = count_words(a_text)
print(result)
