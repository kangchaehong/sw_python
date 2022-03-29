N = input()
cnt = 0

for i in range(int(N)+1) :
    # if '3' in str(i):
    #     cnt += 1
    for j in range(60) :
        # if '3' in str(j):
        #     cnt += 1
        # if str(j)[-1] == '3' or str(j)[0] == '3':
        #     cnt += 1
        for k in range(60) :
            # if '3' in str(k):
            #     cnt += 1
            # if str(k)[-1] == '3' or str(k)[0] == '3' :
            #     cnt += 1
            if '3' in str(i) + str(j) + str(k) :
                cnt +=1
print(cnt)