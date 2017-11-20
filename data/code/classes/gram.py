from os import path


class Gram:
    def __init__(self):
        print 'Inicio n-grama'

    def unigram(self, text_list, str_file_name):
        file_path = path.realpath('../formatado/' + str_file_name + 'Unigram.txt')
        ngram_file = open(file_path, 'w')
        for text in text_list:
            for words in text:
                if self.is_unigram(words.type):
                    ngram_file.write(words.word + "\n")
            ngram_file.write('\n')

        print 'unigram'

    def bigram(self, text_list, str_file_name):
        file_path = path.realpath('../formatado/' + str_file_name + 'Bigram.txt')
        ngram_file = open(file_path, 'w')
        for text in text_list:
            n_text_size = len(text) - 1
            for i in range(0, n_text_size):
                if self.is_multigram(text[i].type):
                    first_word = text[i].word
                    i += 1
                    while i <= n_text_size:
                        if self.is_multigram(text[i].type):
                            second_word = text[i].word
                            ngram_file.write(first_word + " " + second_word + "\n")
                            break
                        i += 1

            ngram_file.write('\n')

        print 'bigram'

    def trigram(self, text_list, str_file_name):
        file_path = path.realpath('../formatado/' + str_file_name + 'Trigram.txt')
        ngram_file = open(file_path, 'w')
        for text in text_list:
            n_text_size = len(text) - 1
            for i in range(0, n_text_size):
                if self.is_multigram(text[i].type):
                    first_word = text[i].word
                    i += 1
                    while i <= n_text_size:
                        if self.is_multigram(text[i].type):
                            second_word = text[i].word
                            i += 1
                            while i <= n_text_size:
                                if self.is_multigram(text[i].type):
                                    third_word = text[i].word
                                    ngram_file.write(first_word + " " + second_word + " " + third_word + "\n")
                                    break
                                i += 1
                            break
                        i += 1

            ngram_file.write('\n')
        print 'trigram'

    def is_unigram(self, str_type):
        return str_type == 'V' or str_type == 'N' or str_type == 'PROP' or str_type == 'ADJ' or str_type == 'ADV'

    def is_multigram(self, str_type):
        return self.is_unigram(str_type) or str_type == 'PRP'

    def create_ngrams(self, text_list, str_file_name):
        print str_file_name
        self.unigram(text_list, str_file_name)
        self.bigram(text_list, str_file_name)
        self.trigram(text_list, str_file_name)