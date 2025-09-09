 def obter_distancia(trig, echo):
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    distancia = (duracao / 2) * 0.0343
    return distancia

#colocamos main para as variáveis ficarem juntas
def main():
    trig = Pin(25, Pin.OUT)
    echo = Pin(27, Pin.IN)
    led_intruder = Pin(26, Pin.OUT)

    contador_caixas = 0
    contador_itens = 0
    item_detectado = False

    while True:
        dist = obter_distancia(trig, echo)

        if dist <= 10 and not item_detectado:
            print("Item detectado")
            led_intruder.value(1)
            item_detectado = True
            contador_itens += 1
            print("Itens na caixa:", contador_itens)

            if contador_itens >= 10:
                contador_caixas += 1
                contador_itens = 0
                print("Caixa completada. Total de caixas:", contador_caixas)

        elif dist > 10 and item_detectado:
            print("Aguardando novo item...")
            item_detectado = False
            led_intruder.value(0)

        time.sleep(2)

main()
