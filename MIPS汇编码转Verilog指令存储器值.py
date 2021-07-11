Inst = []
name = []
i = 0 
with open("bag.txt","r",encoding='utf-8') as file:
    for line in file:
        line=line.strip('\n')#删除换行符
        Inst.append("ROM_data[8'd%s] <= {"%(i)+"32'h"+line+"};")
        i = i + 1
    file.close()
while '' in Inst:
    Inst.remove('')
with open("assmble.txt","r",encoding='utf-8') as file:
    for line in file:
        line=line.strip('\n')#删除换行符
        name.append(line)
    file.close()
while '' in name:
    name.remove('') #删除空行
N = name
A = []
j = 0
for i in range(max(len(N),len(Inst))):
    if (N[i].strip()[-1] == ':' or N[i].strip()[0] == '#'):
        A.append('//'+N[i])
    else:
        A.append(Inst[j] + '    //' +N[i])
        j = j + 1
with open("as.txt","w",encoding='utf-8') as file:
    for i in A:
        file.write(i+'\n')
    file.close()
