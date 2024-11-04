#!/usr/bin/env python3
import random
import shutil
import whois
import socket
import os

user = os.getlogin()

art1 = """         ((((c,               ,7))))
        (((((((              ))))))))
         (((((((            ))))))))
          ((((((@@@@@@@@@@@))))))))
           @@@@@@@@@@@@@@@@)))))))
        @@@@@@@@@@@@@@@@@@))))))@@@@
       @@/,:::,\/,:::,\@@@@@@@@@@@@@@
       @@|:::::||:::::|@@@@@@@@@@@@@@@
       @@\':::'/\':::'/@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@\\
             /    \        (     \\
            (      )        \     \\
             \    /          \
"""

art2 = """\
      ,,                ,,
    (((((              )))))
   ((((((              ))))))
   ((((((              ))))))
    (((((,r@@@@@@@@@@e,)))))
     (((@@@@@@@@@@@@@@@@)))
      \@@/,:::,\/,:::,\@@
     /@@@|:::::||:::::|@@@\\
    / @@@\\':::'/\':::'/@@@ \\
   /  /@@@@@@@//\\\\@@@@@@@\\  \\
  (  /  '@@@@@====@@@@@'  \\  )
   \\(     /          \\     )/
     \\   (            )   /
          \\          /"""

art3 = """                  . '  .
               ' .( '.) '
       _     ('-.)' (`'.) '
      |0|- -(. ')`( .-`) (-')
   .--`+'--.  .  (' -,).(') .
   |`-----'|   (' .) - ('. )
   |       |    . (' `.  )
   |  .-.  |       ` .  `
   | (0.0) |
   | >|=|< |
   |  `"`  |
   |       |
gui|       |
   `-.___.-'
"""


art4 = """          .--.         .--.
              \       /        
       |\      `\___/'       /|
        \\    .-'@ @`-.     //  
        ||  .'_________`.  ||
         \\.'^    Y    ^`.//
         .'       |       `.
        :         |         :
       :          |          :
       :          |          :
       :     _    |    _     :
       :.   (_)   |   (_)    :
     __::.        |          :__
    /.--::.       |         :--.\\
 __//'   `::.     |       .'   `\\\___
`--'     //`::.   |     .'\\\     `--'
         ||  `-.__|__.-'   || 
gui      ||                ||
         //                \\\\
        
        """


art5 = """
     
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
gui   |/                          \\
                                   ||
                                   ||
                                   \\
     
     """



def print_art():
    escolha = random.choice([art1, art2, art3, art4, art5])
    return escolha


print(print_art())

while True:
    try:
        ip = input(f'Ola, {user} qual dominio gostaria de pesquisar? exp: robertet.com ')
        info = whois.whois(ip)
        print(info)

    except socket.gaierror:
        print('Domínio não existe')

    except Exception as any_error:
        print('Erro, entre em contato com adm! ')


    salvar = input('gostaria de salvar as informacoes? ').strip().lower()
    if salvar == 's':
        try:
            dir_path = input('Gostaria de escolher o caminho para salvar? s/n (Caso nao, por padrao, sera salvo no Desktop!) ')
            if dir_path == 's':
                try:
                    dir_path2 = input('Qual caminho sera o caminho? Forneca o caminho completo, por exemplo: /home/seu_usuario/dir_a_ser_criado ')
                    new_path = dir_path2
                    path = new_path
                    os.mkdir(path)
                except FileExistsError:
                    print(f'Erro! ja existe um diretorio com nome "{dir_path2}" ')
                    rm = str(input('gostaria de remover o diretorio antigo e criar o um novo? s/n '))
                    if rm == 's':
                        shutil.rmtree(new_path)
                        os.mkdir(new_path)
                        print(f"Ok, diretorio criado em '{new_path}'  ")
                        with open(os.path.join(new_path, f'info info domain.txt'), 'w') as arc:
                            arc.write(str(info))
                except PermissionError:

                    try:
                        print(f'Erro! Voce nao possui privilegios suficientes para criar um diretorio aqui. Por favor, escolha outro caminho!')
                        dir_path2 = input('Qual caminho sera o caminho? ')
                        new_path = dir_path2
                        path = new_path
                        os.mkdir(path)
                        print(f"Ok, diretorio criado em '{path}' ")
                        with open(os.path.join(new_path, f'info info domain.txt'), 'w') as arc:
                            arc.write(str(info))
                    except FileExistsError:
                        print(f'Erro! ja existe um diretorio com nome "{dir_path2}" ')
                        rm = str(input('gostaria de remover o diretorio antigo e criar o um novo? s/n '))
                        if rm == 's':
                            shutil.rmtree(new_path)
                            os.mkdir(new_path)
                            print(f"Ok, diretorio criado em '{new_path}'  ")
                            with open(os.path.join(new_path, f'info info domain.txt'), 'w') as arc:
                                arc.write(str(info))
            else:
                dir_name = str(input('Qual nome do diretorio? '))
                path = f'/home/{user}/{dir_name}'.lower().strip()
                os.mkdir(path)
                print(f"Ok, diretorio criado em '{path}' com nome '{dir_name}' ")
                with open(os.path.join(path, f'info {ip}.txt'), 'w') as arc:
                    arc.write(str(info))
        except FileExistsError:
            print(f'Erro! ja existe um dir com nome "{dir_name}" ')
            rm = str(input('gostaria de remover o diretorio antigo e criar o um novo? s/n '))
            if rm == 's':
                shutil.rmtree(path)
                path = f'/home/{user}/{dir_name}'.lower().strip()
                os.mkdir(path)
                print(f"Ok, diretorio criado em '{path}' com nome '{dir_name}' ")
                with open(os.path.join(path, 'info dominio.txt'), 'w') as arc:
                    arc.write(str(info))
    else:
        continue
    continua = input('Gostaria de pesquisar mais algum? s/n ').strip().lower()
    if continua == 'n':
        break






