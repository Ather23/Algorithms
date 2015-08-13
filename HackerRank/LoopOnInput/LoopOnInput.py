__author__ = 'root'

def main():

    lines = int(input("Enter lines"))
    for i in range(0,lines):
        num1,num2 = input().split()
        num1,num2 = int(num1),int(num2)
        print(num1+num2)






if __name__ == '__main__':
   main()