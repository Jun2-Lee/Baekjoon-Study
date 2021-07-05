num = int(input())
n_list = [0,1]
for i in range (num):
    n_list.append(n_list[i]+n_list[i+1])
print(n_list[num])