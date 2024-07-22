variavel = 2

try:
    var = bad_var
    if variavel == 1:
        raise Exception('Content') # raise chama um erro 'customizado'
except Exception as e:
    # 'except Exception:' roda caso qualquer erro ocorra.
    print(f"Tipo de erro: {e.__class__.__name__}")
    print(f"Mensagem de erro: {e.args[0]}")
    # Acessar outras informações como variáveis locais e backtrace aqui
    print("Detalhes adicionais do erro:")
    print('Atributo __context__:', e.__context__)
    print('Atributo __traceback__:', e.__traceback__)
    raise
else:
    # Esse bloco será executado no caso de sucesso.
    pass
finally:
    input('Press Enter to exit')

# criar arquivos

# Abrir arquivo para edição, e cria o arquivo se ele nao existir:

f = open('arquivo.txt', 'w')
f.close()

#  cria o arquivo especificado, mas retorna um erro se o arquivo já existir:

# importar lib os para checar se o arquivo existe.
import os
if not os.path.exists('arquivo.txt'):
    f = open('arquivo.txt', 'x')
    f.close()
else:
    print(f'O Arquivo já existe.')


# deletar arquivos

if os.path.exists('arquivo.txt'):
    os.remove('arquivo.txt')
else:
    print('Arquivo nao existe')
