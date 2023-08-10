import string


# суп с   сухариками       должен быть точно


eng_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"
rus_letters = "А а Б б В в Г г Д д Е е Ё ё Ж ж З з И и Й й К к Л л М м Н н О о П п Р р С с Т т У у Ф ф Х х Ц ц Ч ч Ш ш Щ щ Ъ ъ Ы ы Ь ь Э э Ю ю Я я"
rus_letters = rus_letters.split()
eng_letters = eng_letters.split()
eng_set = set(eng_letters)
rus_set = set(rus_letters)


def get_string():
    return str(input())


def count_words(sentence=str):
    counter = 0
    for i in range(len(sentence)):
        new_char = sentence[i]
        if i <= len(sentence) - 2:
            if (rus_set.issuperset(new_char) or eng_set.issuperset(new_char)) and sentence[i+1] == ' ':
                counter += 1
        elif (rus_set.issuperset(new_char) or eng_set.issuperset(new_char)) and sentence[len(sentence) - 1] != ' ':
            counter += 1
    print(counter)


if __name__ == '__main__':
    count_words(get_string())