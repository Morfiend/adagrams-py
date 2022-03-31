import random
from collections import Counter

LETTER_POOL = {
    'A': [9, 1], 
    'B': [2, 3], 
    'C': [2, 3], 
    'D': [4, 2], 
    'E': [12, 1], 
    'F': [2, 4], 
    'G': [3, 2], 
    'H': [2, 4], 
    'I': [9, 1],
    'J': [1, 8],
    'K': [1, 5],
    'L': [4, 1],
    'M': [2, 3],
    'N': [6, 1], 
    'O': [8, 1],
    'P': [2, 3],
    'Q': [1, 10], 
    'R': [6, 1],
    'S': [4, 1],
    'T': [6, 1], 
    'U': [4, 1], 
    'V': [2, 4], 
    'W': [2, 4], 
    'X': [1, 8], 
    'Y': [2, 4],
    'Z': [1, 10]
}


def draw_letters():
    
    letter_list = []
    returned_letters = []
    for letter, number in LETTER_POOL.items():
        letter_list += letter * number[0]
    for i in range(10):
        current_letter = letter_list[random.randint(0, len(letter_list) - 1)]
        returned_letters.append(current_letter)
        letter_list.remove(current_letter)

    return returned_letters
    

def uses_available_letters(word, letter_bank):
    letter_dict = Counter(letter_bank)

    for letter in word.upper():
        try:
            if letter in letter_dict.keys() and letter_dict[letter] > 0:
                letter_dict[letter] -= 1
            else:
                return False
        except KeyError:
            return False
    
    return True

def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_POOL[letter.upper()][1]
    if len(word) > 6:
        score += 8
    return score


def get_highest_word_score(word_list):

    scores = []
    lowest = ()

#gets the scores of all words and keeps track
#of only the highest scores.
#adds the word and the score as a tuple to a list

    for word in word_list:
        current_word_score = score_word(word)
        if not scores: 
            scores.append((word, current_word_score))
        elif current_word_score > scores[0][1]:
            scores = [(word, current_word_score)]
        elif current_word_score == scores[0][1]:
            scores.append((word, current_word_score))
            
#if we don't have a tie all we need to do is return 
#the only item in the list

    if len(scores) == 1:
        return scores[0]

#for tie scenarios. As soon as we come across the
#first word w a length of 10, we can end and
#return that word and score.
#we then define a lowest variable to get the shortest
#word in the list 

    for word, top_score in scores:
        word_length = len(word)
        if word_length == 10:
            return word, top_score
        elif not lowest:
            lowest = (word, top_score, word_length)
        elif word_length < lowest[2]:
            lowest = (word, top_score, word_length)

    return lowest[0], lowest[1]


'''
this is the code we had previously for reference:


    word_scores = {}
    highest_score = 0
    highest_scoring_words = []

    for word in word_list:
        word_scores[word] = score_word(word)

    for score in word_scores.values():
        if score > highest_score:
            highest_score = score

    for word_key, high_score in word_scores.items():
        if high_score == highest_score:
            highest_scoring_words.append(word_key)

    if len(highest_scoring_words) == 1:
        return highest_scoring_words[0], word_scores[highest_scoring_words[0]]
    else:
        if len(highest_scoring_words[0]) == len(highest_scoring_words[1]):
            if word_list.index(highest_scoring_words[0]) > word_list.index(highest_scoring_words[1]):
                return highest_scoring_words[1], word_scores[highest_scoring_words[1]]
            else:
                return highest_scoring_words[0], word_scores[highest_scoring_words[0]]
        elif len(highest_scoring_words[0]) == 10:
            return highest_scoring_words[0], word_scores[highest_scoring_words[0]]
        elif len(highest_scoring_words[1]) == 10:
            return highest_scoring_words[1], word_scores[highest_scoring_words[1]]
        elif len(highest_scoring_words[0]) < len(highest_scoring_words[1]):
            return highest_scoring_words[0], word_scores[highest_scoring_words[0]]
        else:
            return highest_scoring_words[1], word_scores[highest_scoring_words[1]]

'''
