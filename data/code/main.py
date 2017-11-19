from classes.separator import Separator
def main():
    print "testinho"
    teste = Separator()
    text_list = teste.get_file('trabalhadorTagged.txt')
    teste.print_texts(text_list)


if __name__ == '__main__': main()