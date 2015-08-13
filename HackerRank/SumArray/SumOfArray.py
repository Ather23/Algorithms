__author__ = 'root'

def main():
    n = int(input())
    for i in range(1,n):
        arrays = input().split()
        mainOutput = 0

        for j in range(0,len(arrays)):
            nums = arrays[j]
            mainOutput = mainOutput+int(nums)

        print(mainOutput)


if __name__ == '__main__':
    main()