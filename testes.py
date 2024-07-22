import os
from datetime import datetime
from datetime import date

error_occurrence = False # Variavel que controla os logs

# pegar data atual
hoje = date.today()
hoje = hoje.strftime('%d-%m-%Y')

current_file = __file__ # pegar caminho do arquivo sendo executado

linha_erro = None
last_error = None

try:



except Exception as e:
    error_occurrence = True
    last_error = e
    print('-----------------------------------------------------------------')
    print(f"Ocorreu um erro durante a execução.")
    linha_erro = e.__traceback__.tb_lineno
    print(f"Linha {linha_erro}: {e}")
    print(f"Tipo de erro: {e.__class__.__name__}")
    # Acessar outras informações como variáveis locais e backtrace aqui
    print("Detalhes adicionais do erro:")
    print('Atributo __context__:', e.__context__)
    print('Atributo __traceback__:', e.__traceback__)
    print('-----------------------------------------------------------------')

else:
    # Esse bloco será executado no caso de sucesso.
    pass
finally:
    try:
        if error_occurrence is True:
            # Criar arquivo de log
            log_file = 'logs\log_' + hoje + '.txt'
            if not os.path.exists(log_file):
                f = open(log_file, 'x')
                f.close()
            else:

                # informações para o log
                arq_error_name = os.path.basename(current_file)
                horario_log = datetime.now()
                horario_log = horario_log.strftime("%H:%M:%S")
                # setar mensagem
                mensagem = (f"\n"
                        f"{horario_log} - Ocorreu um erro no arquivo {arq_error_name}. Detalhes:\n"
                        f"Linha {linha_erro}: {last_error}\n"
                        f"Tipo de erro: {last_error.__class__.__name__}\n"
                        f"Atributo __context__: {last_error.__context__}\n"
                        f"Atributo __traceback__: {last_error.__traceback__}\n"
                        "-----------------------------------------------------------------")

    except Exception as e:
        error_occurrence = True
        last_error = e
        print('-----------------------------------------------------------------')
        print(f"Ocorreu um erro durante a execução.")
        linha_erro = e.__traceback__.tb_lineno
        print(f"Linha {linha_erro}: {e}")
        print(f"Tipo de erro: {e.__class__.__name__}")
        # Acessar outras informações como variáveis locais e backtrace aqui
        print("Detalhes adicionais do erro:")
        print('Atributo __context__:', e.__context__)
        print('Atributo __traceback__:', e.__traceback__)
        print('-----------------------------------------------------------------')






input('Execução finalizada')
