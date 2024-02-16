import sys
def dog():
    print('Buw')
def default():
    print("Hello")
def main():
    if sys.argv[1]=='cat':
        dog()
    else:
         default()
if __name__=='_main_':
    main()
