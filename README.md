# WhoInMyNet

Script escrito por mi en `python` para sacar/identificar las ip de los usuarios conectados a nuestra red

## Requerimientos

* python
* pip

## Instrucciones

1. Antes de ejecutar los archivos deberas de tener python y pip para instalar los siguientes modulos

~~~bash
$ pip3 install nmap python-nmap

Requirement already satisfied: nmap in $HOME/.local/lib/python3.9/site-packages (0.0.1)
Requirement already satisfied: python-nmap in $HOME/.local/lib/python3.9/site-packages (0.7.1)
~~~

2. Despues de instalar los modulos, deberas de ejecutar el archivo `main.py`

~~~bash
$ python3 main.py

[+] Ingrese su rango de red: 192.168.1.0/24

[·] Detectando otros dispositivos...

[+] Conectados:

[*] 192.168.1.254
[*] 192.168.1.66
[*] 192.168.1.67
[*] 192.168.1.70
[*] 192.168.1.89

[+] Elementos guardados con exito!
~~~

3. Se guardaran las ip en un archivo `.txt` donde podras usarlas para futuras ocasiones

~~~bash
$ cat Conectados.txt

───────┬────────────────────────────────────────────────────────────────────────────────────────────────────────
       │ File: Conectados.txt
───────┼────────────────────────────────────────────────────────────────────────────────────────────────────────
   1   │ 192.168.1.254
   2   │ 192.168.1.66
   3   │ 192.168.1.67
   4   │ 192.168.1.70
   5   │ 192.168.1.89
───────┴────────────────────────────────────────────────────────────────────────────────────────────────────────

~~~

Ya puedes seguir hackeando como un pro


