import random
import string
from paquetes import bd_palabras
from paquetes import diagramas

def juego_ahorcados(palabra):
    print("=======================================")
    print(" ¡Bienvenido al juego del Ahorcado! ")
    print("=======================================")

    letras_por_adivinar = set(palabra) 
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()

    intentos = 7
    
    while len(letras_por_adivinar) > 0 and intentos > 0:
        
        print(f"Te quedan {intentos} intentos y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        
        print(diagramas.vidas[intentos])
        
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input('Escoge una letra: ').upper()
        
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
                
            else:
                intentos = intentos - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
                
        elif letra_usuario in letras_adivinadas:
                print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.") 
            
    if intentos == 0:
        print(diagramas.vidas[intentos])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')
            
palabra = random.choice(bd_palabras.bdPalabras).upper()
juego_ahorcados(palabra)

