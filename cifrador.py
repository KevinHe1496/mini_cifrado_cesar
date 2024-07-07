
from func_cifrador import crea_cifrador
from simple_screen import Screen_manager, Print, Input, locate, cls

def cifrador_cesar():
    with Screen_manager:
        cls()
        while True:
            locate(1, 1)
            Print("CIFRADOR CESAR")
            Print("==============")
            
            distancia = Input("D: ")
  
            if distancia == "":
                continue
                
            distancia_int = int(distancia)
            
            mensaje = Input("Entrada: ")
            
            if mensaje == "":
                continue
        
            distancia_cifra = crea_cifrador(distancia_int)
        

            Print(distancia_cifra(mensaje))

            denuevo = Input("Otro mensaje (S/n)?").upper()
            confirmar = "s"

            if denuevo == confirmar.upper():
                continue
            else:
                break

Print(f'Salida: {cifrador_cesar()}')



