from pathlib import Path

FILE_PATH = './dict'

# Returns True or False.
def does_file_exist(file_path):
    my_file = Path(file_path)
    return my_file.is_file()


def read_words_meanings(line):
    texts = line.split(' - ')
    word = texts[0]
    print(word)
    # if the corresponding meaning exists
    if len(texts) > 1:
        meanings = texts[1].split(', ')
        print(*meanings, sep='\n')


if does_file_exist(FILE_PATH):
    with open("dict", 'r') as fp:
        for line in fp:
            read_words_meanings(line)



