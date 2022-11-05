import threading # Passo 1
import time


def main():
    print("Passo 1 importa Thread")
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12))  
    ]
    
    
    print("Passo 2 adiciona a Thread na Pool de Threads prontas com o th.start()")
    [th.start() for th in threads] # Adiciona a nossa Thread na pool de threads prontas para execução # Passo 3
    print("Podemos fazer outras coisas enquanto a Thread está executando...")
    print("Gekk University" * 2)
    print("Passo 3 - Avisa para a ficar aguardando até aqui até que a Thread termine a execução ")
    [th.join() for th in threads] # Avisa para ficar aguardando aqui até a thread terminar a execução # Passo 4
    print("Pronto!!!!")
    
def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(3)
        
if __name__ == '__main__':
    main()
     