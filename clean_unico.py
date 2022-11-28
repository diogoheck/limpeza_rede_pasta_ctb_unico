import os
import shutil


lista_proibidos = ['Trabalhista']
pasta_sincronizacao = ['.sync']


def limpeza_unico_pastas():

    folder_list = []
    os.chdir('U:\\')
    cwd = os.getcwd()

    for i in os.listdir(cwd):
        if os.path.isdir(i) and i not in lista_proibidos and i not in pasta_sincronizacao:
            folder_list.append(i)
        elif i not in lista_proibidos and i not in pasta_sincronizacao and '.py' not in i:
            os.remove(i)
            pass

    for folder_raiz in folder_list:
        if folder_raiz:
            path2 = cwd + '\\' + folder_raiz
            os.chdir(path2)
            sub_folder_list = [i if os.path.isdir(
                i) else os.remove(i) for i in os.listdir(path2)]
        
        for subfolder in sub_folder_list:
            if subfolder:
                path3 = path2 + '\\' + subfolder
                os.chdir(path3)
                for folder2 in os.listdir(path3):
                    if folder2:
                        try:
                            if os.path.isfile(folder2):
                                os.remove(folder2)
                            else:
                                shutil.rmtree(folder2)
                        except:
                            pass
    print('')
    print('*' * 50)
    print('limpeza efetuada com sucesso!!')
    print('*' * 50)
    print('')

limpeza_unico_pastas()