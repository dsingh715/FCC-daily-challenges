import string
alphabet = list(string.ascii_lowercase)
alphabet_values = list(range(1,27))
alphabet_mapping = dict(zip(alphabet,alphabet_values))
def sum_letters(s):
    total = 0
    s = s.lower()
    s = remove_items(s)
    sentence = s
    if not sentence:
        s = 0
    else:
        for i in range(len(sentence)):
            running_total = alphabet_mapping[f"{sentence[i]}"]
            total = total + running_total
            s = total
    return s

def remove_items(sentence):
    updated_list = []
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            updated_list.append(sentence[i])
    return updated_list

sum_letters("The quick brown fox jumps over the lazy dog.")