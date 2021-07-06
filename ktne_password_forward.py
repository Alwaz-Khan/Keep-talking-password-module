word_list = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house",
             "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write"]

possible_combination_list = []

for i in range(5):
    input_list = []
    temp_list = []
    output_list = []

    print("Enter " + str(i + 1) + " position options")
    for j in range(6):
        input_list.append(input().lower())

    if possible_combination_list:
        for word1 in possible_combination_list:
            for letter in input_list:
                temp_list.append(word1 + letter)
        possible_combination_list = temp_list
    else:
        possible_combination_list = input_list

    for word2 in possible_combination_list:
        for word3 in word_list:
            if word2 == word3[:len(word2)]:
                output_list.append(word3)

    if len(output_list) <= 3:
        break
    else:
        word_list = output_list

print(output_list)