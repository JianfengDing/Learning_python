#change the working directory
#coding = utf-8
import os

pwd = ['d:\\pythoncode', 'd:\\Documents', 'e:\\', 'f:\\']
i = 0
print('现有的目录如下：\n')
for directory in pwd:
	print(i, '-->', directory)
	i += 1

#choice = input("请输入希望进入的目录： ")
#pwd = ['c:\\jupyterNotebook', 'd:\\', 'e:\\']
information = "请输入希望进入的目录对应的数字： \n\
(如果希望有其他的目录，请到pwd.py文件进行添加与修改。)\n\
默认为0\n"
#choice = int(input(information)) #choose the target directory 
choice = (input(information)) #choose the target directory 
if not choice:
	choice = 0	
else : 
	choice = int(choice)


pwd_change = pwd[choice] # the target directory
os.chdir(pwd_change) # change to the directory
