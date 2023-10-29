print('   2 3 4 5 6 7\n -------------')
for i in range(16):
    print(f'{hex(i)[2].upper()}: '+' '.join([chr(int(str(j)+hex(i)[2],16))if str(j)+hex(i)[2]!='7f'else'DEL'for j in range(2,8)]))
