word_list = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house",
             "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write"]

possible_combination_list = []
input_list3 = []
input_list4 = []
input_list1 = []
output_list = []

print("Enter 1st position options")
for i in range(6):
    input_list1.append(input().lower())

print("Enter 4th position options")
for i in range(6):
    input_list4.append(input().lower())

for word in word_list:
    if word[3] in input_list4 and word[0] in input_list1:
        output_list.append(word)

if len(output_list) <= 3:
    print(output_list)
else:
    word_list = output_list
    output_list = []
    print("Enter 3rd position options")
    for i in range(6):
        input_list3.append(input().lower())
    for word in word_list:
        if word[2] in input_list3:
            output_list.append(word)
    print(output_list)

