import sys
import os

filename = "generatedfile/file.txt"

def generate(size):
    fo = open(filename,"wb")
    fo.seek(size-1)
    fo.write(b"\0")
    fo.close()


def file_creator():
    if sys.argv[2].lower()=="byte":
        size=int(sys.argv[1])
        generate(size)
    elif sys.argv[2].lower()=="kb":
        size=int(sys.argv[1])*1024
        generate(size)
    
    elif sys.argv[2].lower()=="mb":
        size=int(sys.argv[1])*1024*1024
        generate(size)
    
    elif sys.argv[2].lower()=="gb":
        size=int(sys.argv[1])*1024*1024*1024
        generate(size)
    
    elif sys.argv[2].lower()=="tb":
        answer=input("Do you really want to generate a 1 TB File?(Yes/No): ")
        if answer.lower()=="yes":
            size=int(sys.argv[1])*1024*1024*1024*1024
            generate(size)
        else:
            print("Aborting!!!")
            sys.exit()
        
    elif sys.argv[2].lower()=="pb":
        answer=input("Do you really want to generate a 1 TB File?(Yes/No): ")
        if answer.lower()=="yes":
            size=int(sys.argv[1])*1024*1024*1024*1024*1024
            generate(size)
        else:
            print("Aborting!!!")
            sys.exit()
    else:
        print("The given storage unit type is not supported!!")
    

if __name__ == "__main__":
    file_creator()