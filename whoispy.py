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




art3 ="""                  . '  .
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


def print_art():
    escolha = random.choice([art1,art2, art3])
    return escolha
print(print_art())


while True:
    try:
        ip = input(f'Ola, {user} qual dominio gostaria de pesquisar? ')
        info = whois.whois(ip)
        print(info)

    except socket.gaierror:
        print('Domínio não existe')

    except Exception as any_error:
        print('Erro, entre em contato com adm! ')

    salvar = input('gostaria de salvar as informacoes? ').strip().lower()
    if salvar == 's':
        try:
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






