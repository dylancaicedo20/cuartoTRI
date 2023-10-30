
def ingresar_ip():
    return input("ingrese la direccion ip: ")

def validar_direccion_ip(ip_func):
    def wrapper(*args):
        for direccion in args:
            octetos = direccion.split('.')
            if len(octetos) != 4:
                print("no es una dirección IP válida")
            else:
                octetos_validos = True
                for octeto in octetos:
                    try:
                        valor = int(octeto)
                        if valor < 0 or valor > 255:
                            print(f"Error: {direccion} contiene un octeto inválido ({octeto})")
                            octetos_validos = False
                        
        # Tu función aquí
        print("Función ejecutada con éxito para la dirección IP:", ip)

@validar_direccion_ip
def determinar_clase_ip(direccion_ip):
    try:
        primer_octeto = int(direccion_ip.split('.')[0])
        if 0 <= primer_octeto <= 127:
            return 'Clase A - Privada'
        elif 128 <= primer_octeto <= 191:
            return 'Clase B - Privda'
        elif 192 <= primer_octeto <= 223:
            return 'Clase C - Privada'
        elif 224 <= primer_octeto <= 239:
            return 'Clase D (Multicast) - Publica'
        elif 240 <= primer_octeto <= 255:
            return 'Clase E (Reservada) - Publica'
        else:
            return 'No se pudo determinar la clase (Fuera de rango)'
    except (ValueError, IndexError):
        return 'Dirección IP no válida'

@validar_direccion_ip
def calcular_hosts_posibles(direccion_ip):
    try:
        primer_octeto = int(direccion_ip.split('.')[0])
        if 1 <= primer_octeto <= 126:
            return 2 ** 24 - 2
        elif 128 <= primer_octeto <= 191:
            return 2 ** 16 - 2
        elif 192 <= primer_octeto <= 223:
            return 2 ** 8 - 2
        else:
            return 0 
    except (ValueError, IndexError):
        return 0 



direccion_ip = ingresar_ip()


funcion_con_ips(direccion_ip)


clase = determinar_clase_ip(direccion_ip)
print(f"La dirección IP {direccion_ip} pertenece a la {clase}")

hosts_posibles = calcular_hosts_posibles(direccion_ip)
print(f"La dirección IP {direccion_ip} puede direccionar {hosts_posibles} hosts")




