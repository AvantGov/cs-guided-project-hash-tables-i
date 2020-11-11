"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.

    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
"""


"""
UNDERSTAND: 
- compare the words to make sure that item 1 is shorter than order 2
- compare every letter in each word to the alphabet to determine if the order is correct 
- each letter in teh new alphabet needs a numeric value so we know what comes first, second, etc. 

PLAN: 
1. map each letter to the numeric value in stored in dict 
2. iterate through words and compare pairs of words to see if theyre in sorted order
    - compare the first letters:
        - if different, determine which one comes first 
        - if they are the same, compare the next letters 
    - if not, return false 
3. return true (if condition met) 

"""


# def are_words_sorted(words, alpha_order):
    # create dictionary with input 

    # for item in list 
        # define next word in list 
        # check dict with first letter of first word to get index value 
        # check dict with first letter of second word to get index value 
        # if l1 w1 < l1 w2:
            # continue 
        # if l1 w1 > l1 w2:
            # return false 
        # if l1 w1 == l1 w2:
            # define l1 = l2 for w 1 + 2
            # recurse     

def are_words_sorted(words, alpha_order):
    # define dictionary 
    alphabet_dict = {}

    # map each letter (key) to number (value) in alpha dictionary to reference 
    for i in range(len(alpha_order)):
        character = alpha_order[i]
        alphabet_dict[character] = i

    for word_idx in range(len(words) - 1):
        # define the cur_word and next_word
        word_a = words[word_idx]
        word_b = words[word_idx + 1]
        
        for letter_idx in range(len(word_a)):
            # define the first letter of each word 
            char_a = word_a[letter_idx]
            char_b = word_b[letter_idx]
            
            # make sure that word a is not longer than word b
            if letter_idx >= len(word_b):
                return False

            # reference the dict in order to get the idx of the char 
            index_a = alphabet_dict[char_a]            
            index_b = alphabet_dict[char_b]

            # compare the current char idx to that of the next word
            if index_a == index_b:
                continue

            if index_a < index_b:
                # we know these word are in order, so break and go to the next 
                break

            if index_a > index_b:
                return False 
        
    return True