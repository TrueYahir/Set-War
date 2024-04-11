class Manager:
    def __init__(self):
        self.ejercitos = []
        
    def crear_ejercito(self, facciones_Cab, faccion_Aqr, faccion_Cle):
        nuevo_ejercito = [facciones_Cab, faccion_Aqr, faccion_Cle]
        ejercito = ejercito(nuevo_ejercito)
        self.ejercitos.append(ejercito)
        
    def estadisticas_batalla(self, conjunto_in, conjunto_out, opcion,uso, ataque):
        contador = 0
        contador_v = 0
        for i in conjunto_in.facciones[uso - 1]:
            contador += 1
            contador_2 = 0
            for j in conjunto_out.facciones[ataque - 1]:
                contador_2 += 1
                contador_v += 1
                if opcion == 1:
                    if(contador + 1 == len(conjunto_in.facciones[uso - 1])):
                        pass
                    elif contador_v % 5 == 0:
                        pass
                    else:
                        pass
                elif opcion == 2:
                    if(contador + 1 == len(conjunto_in.facciones[uso - 1])):
                        pass
                    elif contador_v % 5 == 0:
                        pass
                    else:
                        pass
                elif opcion == 3:
                    if i.health <= 0 or j.health <= 0:
                        if (contador + 1 == len(conjunto_in.facciones[uso - 1])):
                            pass
                        elif contador_v % 5 == 0:
                            pass
                        else:
                            pass
                elif opcion == 6:
                    if(contador + 1 == len(conjunto_in.facciones[uso - 1])):
                        pass
                    elif contador_v % 5 == 0:
                        pass
                    else:
                        pass
                    
                    