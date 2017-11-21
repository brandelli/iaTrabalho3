from os import path


class Structure:
    def __init__(self, arr_files):
        self.create_unigram_structure(arr_files)
        self.create_bigram_structure(arr_files)
        self.create_trigram_structure(arr_files)

    def create_unigram_structure(self, arr_files):
        self.create_unigram_test_structure(arr_files)
        self.create_unigram_training_structure(arr_files)

    def create_bigram_structure(self, arr_files):
        self.create_bigram_test_structure(arr_files)
        self.create_bigram_training_structure(arr_files)

    def create_trigram_structure(self, arr_files):
        self.create_trigram_test_structure(arr_files)
        self.create_trigram_training_structure(arr_files)

    def create_unigram_test_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTestUnigram.txt')
        # file_path = path.realpath('../formatado/bowTrainingUnigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/unigramTestStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION UnigramTest \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i+1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TestUnigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result+'\n')
                        str_result = ""

        structure_file.close()

    def create_unigram_training_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTrainingUnigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/unigramTrainingStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION UnigramTraining \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i + 1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TrainingUnigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result + '\n')
                        str_result = ""

        structure_file.close()

    def create_bigram_test_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTestBigram.txt')
        # file_path = path.realpath('../formatado/bowTrainingBigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/bigramTestStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION BigramTest \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i + 1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TestBigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result+'\n')
                        str_result = ""

        structure_file.close()

    def create_bigram_training_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTrainingBigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/bigramTrainingStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION BigramTraining \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i + 1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TrainingBigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result + '\n')
                        str_result = ""

        structure_file.close()

    def create_trigram_test_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTestTrigram.txt')
        # file_path = path.realpath('../formatado/bowTrainingTrigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/trigramTestStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION TrigramTest \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i + 1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TestTrigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result+'\n')
                        str_result = ""

        structure_file.close()

    def create_trigram_training_structure(self, arr_files):
        words_list = []
        file_path = path.realpath('../formatado/bowTrainingTrigram.txt')
        with open(file_path) as f:
            for line in f:
                words_list.append(line.strip('\n'))

        file_structure = path.realpath('../formatado/trigramTrainingStructure.txt')
        structure_file = open(file_structure, 'w')
        structure_file.write('@RELATION TrigramTraining \n')
        structure_file.write('\n')
        for i in range(len(words_list)):
            structure_file.write('@ATTRIBUTE "P' + `i + 1` + words_list[i] + '" integer \n')

        str_classes = ''
        for i in range(len(arr_files)):
            str_classes += arr_files[i]
            if i != len(arr_files) - 1:
                str_classes += ','

        structure_file.write('@ATTRIBUTE class {' + str_classes + '} \n')
        structure_file.write('\n')
        structure_file.write('@DATA')
        structure_file.write('\n')

        for str_file_name in arr_files:
            file_path = path.realpath('../formatado/' + str_file_name + 'TrainingTrigram.txt')
            with open(file_path) as f:
                text_words = []
                str_result = ''
                for line in f:
                    if line != '\n':
                        new_line = line.strip('\n')
                        text_words.append(new_line)
                    else:
                        for word in words_list:
                            if text_words.count(word) > 0:
                                str_result += `1` + ','
                            else:
                                str_result += `0` + ','
                        text_words = []
                        str_result += str_file_name
                        structure_file.write(str_result + '\n')
                        str_result = ""

        structure_file.close()
