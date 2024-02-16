import sys
def dog():
    print('Buw')
def cat():
    print('Meow')
def default():
    print("Hello")
def main():
    if sys.argv[1]=='cat':
        dog()
    else:
         default()
    if __name__=='_main_':
        cat()
    else:
         default()
    if __name__=='__main__':
     main()
