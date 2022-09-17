from app.detections import detections
import sys, time

try:

    try:
        gateway = input('\n[+] Ingrese su rango de red: ')

        time.sleep(1)

        print('\n[·] Detectando otros dispositivos...')

        detect = detections(gateway)

        ips = detect.checkNets()

        print('\n[+] Conectados:\n')

        for i in ips:

            print(f'[*] {i}')

            open('Conectados.txt', 'at').write(f'{i}\n')

        print('\n[+] Elementos guardados con exito!')

    except Exception as e:

        time.sleep(1)

        print(f'Error: {e}')

        time.sleep(1)

        sys.exit(1)

except KeyboardInterrupt:

    time.sleep(1)

    print('\n[!] Saliendo...')

    time.sleep(1)
    
    sys.exit(1)


