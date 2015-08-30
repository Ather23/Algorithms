def main():
    inputLines= int(input())
    lines=[0 for i in range(inputLines)]

    for i in range(0,inputLines):
        value = input()
        times = input()
        lines[i]=value+'|'+times

    response = [0 for j in range(inputLines)]

    for j in range(0,inputLines):
        x = lines[j].split('|')
        n =x[0].split()[0]
        k = int(x[0].split()[1])
        students = x[1].split()

        before=0
        after=0
        for s in range(0,int(n)):
            time = int(students[s])
            if(time)>0:
                after=after+1
            else:
                before=before+1

        if (before>=k):
           response[j]="NO"
        else:
           response[j]="YES"

    for j in range(0,inputLines):
        print(response[j])

if __name__ == "__main__": main()