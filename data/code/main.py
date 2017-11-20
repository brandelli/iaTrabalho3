from classes.separator import Separator
from classes.gram import Gram

def main():
    arr_files = ['esportes', 'policia', 'problema', 'trabalhador']
    separator = Separator()
    gram = Gram()
    for f in arr_files:
        text_list = separator.get_file(f)
        separator.separate_files(text_list, f)
        gram.create_ngrams(text_list,f)



if __name__ == '__main__': main()