import time

def countdown_timer():
  print("+--"*12 + "+")
  print("Ingresa el temporalizador en segundos")
  print("+--"*12 + "+\n")
  duration = int(input()) # segundos convertidos a numeros
  start_time = time.time()  # tiempo inicial en segundos desde la época
  end_time = start_time + duration  # calcula el tiempo final sumando el tiempo inicial con la duracion
  while time.time() < end_time: # bucle para contar hacia atras
      time_left = end_time - time.time()  # se calcula el tiempo restante restando el tiempo final con el tiempo actual
      mins, secs = divmod(time_left, 60)  # se conviete el tiempo en minutos y segundos. divmod es una division que devuelve el cociente y el resto
      timer = '{:02d}:{:02d}'.format(int(mins), int(secs))  # se formatea el tiempo restante en formato mm:ss
      print(timer, end="\r\n")  # imprime el tiempo restante en la consola
      time.sleep(1) # se pausa el contandor por 1 segundo
  print('¡Tiempo agotado!')

countdown_timer(duration)