import time

light_on = False

while True:
    time_on = int(input("Введите время включения света (в секундах): "))
    if time_on <= 0:
        print("Неверное значение. Попробуйте еще раз.")
        continue
    print("Свет включен.")
    light_on = True
    time.sleep(time_on)
    print("Свет выключен.")
    light_on = False
