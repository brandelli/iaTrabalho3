from os import path
from word import Word

class Separator:
    def __init__(self):
        print "Iniciou separador"

    def get_file(self, str_file):
        text_list = []
        word_list = []
        file_path = path.realpath('../formatado/'+str_file)
        with open(file_path) as f:
            for line in f:
                word = Word()
                if line != '\n':
                    new_line = line.strip('\n')
                    str_word, str_type = new_line.split()
                    word.word = str_word
                    word.type = str_type
                    word_list.append(word)
                else:
                    text_list.append(word_list)
                    word_list = []

        return text_list

    def print_texts(self, text_list):
        print len(text_list)
        for text in text_list:
            for word in text:
                print word.word + " " + word.type