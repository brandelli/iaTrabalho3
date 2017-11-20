from os import path


class Merge:
    def merge_bow_files(self, arr_files):
        self.merge_unigram_training_bow(arr_files)
        self.merge_bigram_training_bow(arr_files)
        self.merge_trigram_training_bow(arr_files)
        self.merge_unigram_test_bow(arr_files)
        self.merge_bigram_test_bow(arr_files)
        self.merge_trigram_test_bow(arr_files)

    def merge_unigram_training_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTrainingUnigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TrainingUnigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()

    def merge_bigram_training_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTrainingBigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TrainingBigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()

    def merge_trigram_training_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTrainingTrigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TrainingTrigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()

    def merge_unigram_test_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTestUnigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TestUnigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()

    def merge_bigram_test_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTestBigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TestBigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()

    def merge_trigram_test_bow(self, arr_files):
        file_uni = path.realpath('../formatado/bowTestTrigram.txt')
        uni_bow = open(file_uni, 'w')
        words_list = []
        for str_file in arr_files:
            file_bow = path.realpath('../formatado/' + str_file + 'TestTrigramBagOfWords.txt')
            with open(file_bow) as bow:
                for line in bow:
                    if words_list.count(line) < 1:
                        words_list.append(line)
        for words in words_list:
            uni_bow.write(words)

        uni_bow.close()
