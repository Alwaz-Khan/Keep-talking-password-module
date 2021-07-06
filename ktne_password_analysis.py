word_list = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house",
             "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write"]

len_list0 = {}
for k in range(5):
    temp_list0 = []
    for word in word_list:
        if word[k] not in temp_list0:
            temp_list0.append(word[k])
    len_list0[k+1] = len(temp_list0)

print(len_list0.values())
print(len_list0)


len_list = {}
for i in range(5):
    for j in range(i + 1, 5):
        temp_list = []
        for word in word_list:
            if (word[i] + word[j]) not in temp_list:
                temp_list.append(word[i] + word[j])
        len_list[i+1, j+1] = len(temp_list)

print(len_list.values())
print(len_list)


len_list2 = {}
for a in range(5):
    for b in range(a + 1, 5):
        for c in range(b + 1, 5):
            temp_list2 = []
            for word in word_list:
                if (word[a] + word[b] + word[c]) not in temp_list2:
                    temp_list2.append(word[a] + word[b] + word[c])
            len_list2[a+1, b+1, c+1] = len(temp_list2)

print(len_list2.values())
print(len_list2)
