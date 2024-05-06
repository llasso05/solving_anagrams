from functions.loader import read_dictionary


def main():
    # load digital dict as a list
    dictionary_name = input('\nEnter dictionary name \n')
    dictionary = read_dictionary(dictionary_name)

    # accept a word from user
    word = input('\nInsert Anagram to solve:\n')
    anagrams = []# create an empty list to hold anagrams
    
    # sort the user-word
    s_word = sorted(word)
    ####print(s_word)

    # loop trough the dict
    for word in dictionary:
        sorted_dict = sorted(word.lower()) # sort the word
        if sorted_dict == s_word:
            anagrams.append(word)

    # print anagram list
    print(anagrams)


if __name__ == '__main__':
    main()

