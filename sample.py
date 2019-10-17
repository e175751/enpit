import os

def main():
    f = open("sample.txt")
    list=[]
    line = f.readline() 
    while line:
        list.append(line)
        line = f.readline()
    f.close
    print(list)
    fuga=[]
    for i in range(len(list)):
        hoge = list[i].rstrip('\n')
        item = hoge.split(",")
        fuga.append(item[0])
    print(item)
    print(fuga)
if __name__ == "__main__":
    main()

