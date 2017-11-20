from os import path
from word import Word


class Separator:
    def __init__(self):
        print "Iniciou separador"

    def get_file(self, str_file):
        # print str_file
        text_list = []
        word_list = []
        file_path = path.realpath('../formatado/'+str_file+'Tagged.txt')
        with open(file_path) as f:
            for line in f:
                word = Word()
                if line != '\n':
                    new_line = line.strip('\n')
                    str_word, str_type = new_line.split()
                    word.word = str_word.lower()
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

    def create_test(self, text_list, n_training, str_file_name):
        # print 'inicio do arquivo de teste'
        file_path = path.realpath('../formatado/'+str_file_name+'Test.txt')
        test_file = open(file_path,'w')
        for i in range(n_training, len(text_list)):
            for word in text_list[i]:
                test_file.write(word.word + " " + word.type+"\n")
            test_file.write("\n")
        test_file.close()
        # print 'fim do arquivo de teste'

    def create_training(self, text_list, n_training, str_file_name):
        # print 'inicio do arquivo de treino'
        file_path = path.realpath('../formatado/' + str_file_name + 'Training.txt')
        test_file = open(file_path, 'w')
        for i in range(0, n_training):
            for word in text_list[i]:
                test_file.write(word.word + " " + word.type + "\n")
            test_file.write("\n")

        test_file.close()
        # print 'fim do arquivo de treino'

    def separate_files(self, text_list, str_file_name):
        n_texts = len(text_list)
        n_training = int((n_texts * 0.8))
        self.create_training(text_list, n_training, str_file_name)
        self.create_test(text_list, n_training, str_file_name)

