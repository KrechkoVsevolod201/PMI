import re

# суп с сухариками. должен быть.точно


def get_string():
    return str(input())


def change_string(sentence=str):
    new_sentence = sentence.split(".")
    for i in range(len(new_sentence)):
        new_substring = new_sentence[i]
        new_sub = ""
        for j in range(0, len(new_substring)):
            if j == 0 and new_substring[j] != ' ':
                new_sub += new_substring[j].upper()
            elif j == 0 and new_substring[j] == ' ':
                j = 1
                new_sub += ' '
                new_sub += new_substring[j].upper()
            elif j > 1 and new_substring[0] == ' ':
                new_sub += new_substring[j]
            elif j > 0 and new_substring[0] != ' ':
                new_sub += new_substring[j]

        new_sentence[i] = str(new_sub)
        new_sentence[i] = new_sentence[i] + ". "
        if i + 1 <= len(sentence) - 1:
            i += 1
    print("".join(new_sentence))


def change_string2(sentence=str):
    dot_indexes = []
    new_sentence = ""
    for i in range(len(sentence)):
        if sentence.find(".", i, i+1) != -1:
            dot_indexes.append(sentence.find(".", i, i+1))
    print(dot_indexes)
    j = 0
    for i in range(len(sentence)):
        if i == (dot_indexes[j]+2):
            new_sentence += sentence[i].upper()
            print(new_sentence)
            if j < len(dot_indexes) - 1:
                j = j + 1
        else:
            new_sentence += sentence[i]
    return new_sentence


if __name__ == '__main__':
    change_string(get_string())