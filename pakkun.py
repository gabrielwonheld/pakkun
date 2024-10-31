import math, sys, os, re
from pathlib import Path

def checarParametro():

    if len(sys.argv) < 2:

        print('Necessita do diretório a ser explorado.')
        return False


def listarDir():

    checarParametro()
    diretorio = sys.argv[1]
    listagem = os.listdir(diretorio)

    print('\n'.join(listagem))



def progress_callback(current, total):
    percent_complete = (current / total) * 100
    num_hash = math.floor(percent_complete)
    barra = '#' * num_hash
    #print(f"Progresso: {percent_complete:.2f}% ({current} de {total} bytes)", end="\r")
    print(f"\rProgresso: {percent_complete:.2f}% [{barra:<100}] ({current} de {total} bytes)", end='')

def finditem(nome):


    padrao_regex = re.compile(rf'{nome}')
    caminho = Path(sys.argv[1])
    todos_arquivos = list(caminho.rglob("*"))
    total_arquivos = len(todos_arquivos)

    arquivos_encontrados = []
    
    
    for i, arquivo in enumerate(todos_arquivos, start=1):
        
        try:
            progress_callback(i, total_arquivos)
            if padrao_regex.search(arquivo.name):
                arquivos_encontrados.append(arquivo)
        except PermissionError:
            continue
        except Exception as e:
            print(f"\nErro ao processar {arquivo}: {e}")
            continue

    
    if arquivos_encontrados:
        for arquivo in arquivos_encontrados:
            print(f'\nArquivo Encontrado: {arquivo}')
        print(f'Total de Arquivo encontrados: {total_arquivos}')
        return arquivos_encontrados
    else:
        print('arquivo não encontrado')
        return None



if __name__ == '__main__':

    try:

        
        #listarDir()
        
        finditem(sys.argv[2])

    except NotImplementedError:
        print('Elemento não encontrado')
    except NotADirectoryError:
        print('Dir não encontrado')

    except Exception as e:
        print(e)

