from os import path


class Gram:
    def __init__(self):
        print 'Inicio n-grama'

    def unigram(self, text_list, str_file_name):
        ngram_frequency = {}
        file_path = path.realpath('../formatado/' + str_file_name + 'Unigram.txt')
        ngram_file = open(file_path, 'w')
        for text in text_list:
            for words in text:
                if self.is_unigram(words.type):
                    ngram_file.write(words.word + "\n")
                    if words.word in ngram_frequency:
                        ngram_frequency[words.word] += 1
                    else:
                        ngram_frequency[words.word] = 1
            ngram_file.write('\n')

        self.save_fequency(ngram_frequency, str_file_name + "Unigram")
        self.sort_frequencies(ngram_frequency, str_file_name + "Unigram")
        print 'unigram'

    def bigram(self, text_list, str_file_name):
        ngram_frequency = {}
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
                            str_result = first_word + " " + second_word
                            ngram_file.write(str_result + "\n")
                            if str_result in ngram_frequency:
                                ngram_frequency[str_result] += 1
                            else:
                                ngram_frequency[str_result] = 1
                            break
                        i += 1

            ngram_file.write('\n')

        self.save_fequency(ngram_frequency, str_file_name + "Bigram")
        self.sort_frequencies(ngram_frequency, str_file_name + "Bigram")
        print 'bigram'

    def trigram(self, text_list, str_file_name):
        ngram_frequency = {}
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
                                    str_result = first_word + " " + second_word + " " + third_word
                                    ngram_file.write(str_result + "\n")
                                    if str_result in ngram_frequency:
                                        ngram_frequency[str_result] += 1
                                    else:
                                        ngram_frequency[str_result] = 1
                                    break
                                i += 1
                            break
                        i += 1

            ngram_file.write('\n')
        self.save_fequency(ngram_frequency, str_file_name + "Trigram")
        self.sort_frequencies(ngram_frequency, str_file_name + "Trigram")
        print 'trigram'

    def is_unigram(self, str_type):
        return str_type == 'V' or str_type == 'N' or str_type == 'PROP' or str_type == 'ADJ' or str_type == 'ADV'

    def is_multigram(self, str_type):
        return self.is_unigram(str_type) or str_type == 'PRP'

    def print_frequency(self, dictionary):
        for entry in dictionary:
            print entry + " " + `dictionary[entry]`

    def save_fequency(self, dictionary, str_file_name):
        file_path = path.realpath('../formatado/' + str_file_name + 'Frequency.txt')
        ngram_file = open(file_path, 'w')
        for entry in dictionary:
            ngram_file.write(entry + " " + `dictionary[entry]` + "\n")

        ngram_file.close()

    def sort_frequencies(self, dictionary, str_file_name):
        sorted_frequencies = []
        temp_sorted = {}
        for key in dictionary:
            n_index = dictionary[key]
            if sorted_frequencies.count(n_index) == 0:
                sorted_frequencies.append(n_index)

            if not n_index in temp_sorted:
                temp_sorted[n_index] = []
                temp_sorted[n_index].append(key)
            else:
                temp_sorted[n_index].append(key)

        sorted_frequencies.sort(None, None, True)
        self.create_bag_of_word(sorted_frequencies, temp_sorted, str_file_name)

    def create_bag_of_word(self, arr_sorted_frequencies, dic_frequencies, str_file_name):
        n_words_in_bag = 10
        file_path = path.realpath('../formatado/' + str_file_name + 'BagOfWords.txt')
        file_path2 = path.realpath('../formatado/' + str_file_name + 'BagOfWordsFrequency.txt')
        ngram_file = open(file_path, 'w')
        ngram_file_with_frequency = open(file_path2, 'w')
        while n_words_in_bag > 0:
            for key in arr_sorted_frequencies:
                for words in dic_frequencies[key]:
                    ngram_file.write(words + "\n")
                    ngram_file_with_frequency.write(words + ' ' + `key` + "\n")
                    # print words + ' ' + `key`
                    n_words_in_bag -= 1
                    if n_words_in_bag == 0:
                        break

                if n_words_in_bag == 0:
                    break
        ngram_file.close()
        ngram_file_with_frequency.close()

    def create_ngrams(self, text_list, str_file_name):
        print str_file_name
        training_list, test_list = self.separate_lists(text_list)
        self.unigram(training_list, str_file_name + "Training")
        self.unigram(test_list, str_file_name + "Test")
        self.bigram(training_list, str_file_name + "Training")
        self.bigram(test_list, str_file_name + "Test")
        self.trigram(training_list, str_file_name + "Training")
        self.trigram(test_list, str_file_name + "Test")

    def separate_lists(self, text_list):
        training_list = []
        test_list = []
        n_texts = len(text_list)
        n_training = int((n_texts * 0.8))
        for i in range(0, n_training):
            training_list.append(text_list[i])

        for i in range(n_training, n_texts):
            test_list.append(text_list[i])

        return training_list, test_list
