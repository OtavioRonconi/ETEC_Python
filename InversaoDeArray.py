#arry
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#reversão do arry
ArrRevertido = arr[:7][::-1]

ArrList = list(reversed(arr))

#chamado do arr reverso
print("array invertido\n",ArrRevertido,"\n")
print("array invertido como lista\n",ArrList,"\n")
print("array normal\n", arr)