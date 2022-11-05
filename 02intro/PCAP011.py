import threading

def alguma_funcao(param):
    print('Executa algo...')
    print(f'Usa o parâmetro rebido: {param}')

    return param * param

th = threading.Thread(target=alguma_funcao, args=(42,))

th.start()
th.join() 