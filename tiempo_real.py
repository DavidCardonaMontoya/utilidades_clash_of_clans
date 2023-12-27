tiempo_inicial = list(map(int, input("Dime el tiempo (HH:MM:SS): ").split(':')))

tiempo_en_horas = 0

for unidad_tiempo, a_hora in zip(tiempo_inicial, [1, 1/60, 1/3600]): #[1, 1/60, 1/3600]: [h->h, min->h, seg->h]
    
    tiempo_en_horas += unidad_tiempo * a_hora 

velocidad = float(input("Dime la velocidad: "))

tiempo_final = tiempo_en_horas / velocidad

horas = int(tiempo_final)

minutos = int((tiempo_final-horas)*60)

segundos = int(((tiempo_final-horas)*60 - minutos)*60)

formato_salida = f"{horas} horas, {minutos} minutos, {segundos} segundos"
        
print(formato_salida)