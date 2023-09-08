staring_num = int(input())
ending_num= int(input())


for i in range(staring_num,ending_num):
    if (i % 2) == 0:
        print("Even Number")
    else:
        print("Odd Number")