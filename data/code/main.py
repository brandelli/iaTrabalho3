from classes.separator import Separator
from classes.gram import Gram
from classes.merge import Merge
from classes.structure import Structure

def main():
    arr_files = ['esportes', 'policia', 'problema', 'trabalhador']
    separator = Separator()
    gram = Gram()
    merge = Merge()
    for f in arr_files:
        text_list = separator.get_file(f)
        separator.separate_files(text_list, f)
        gram.create_ngrams(text_list, f)

    merge.merge_bow_files(arr_files)
    Structure(arr_files)


if __name__ == '__main__': main()