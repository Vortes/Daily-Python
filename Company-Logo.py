
def sort(user_input):
    count_dictionary = {}
    top_three = {}
    letters = list(set(user_input))

    for i in range(len(letters)):
        count_dictionary[letters[i]] = user_input.count(letters[i])

    # biggest_value = max(count_dictionary, key=count_dictionary.get)
    for key, value in count_dictionary.items():
        max_value = 0
        top_three[key] = 


if __name__ == '__main__':
    user_input = input()
    sort(user_input)
