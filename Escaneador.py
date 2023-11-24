# Escaneador.py
# Descripción: Utilidad de red escrita en Python para escanear y detectar dispositivos en un segmento de red indicado con nmap,
# obtener su dirección ip, dirección mac y sus puertos abiertos

# Librerias importadas
import nmap

# Predefinido
separador = "********************************************"

# Funciones
def printFoundHosts( allHostsList):
    if len( allHostsList ) > 0:
        print( "\n*--- Dispositivos encontrados:\n" )

        for i, host in enumerate( allHostsList ):
            print( separador )
            print( f"*** Dispositivo #{ i + 1 } ***" )
            print( f"Nombre:        { devScanner[host].hostname() }" )
            print( f"Dirección Ip:  { host }" )

            if 'mac' in devScanner[host]['addresses']:
                print( f"Dirección MAC: { devScanner[host]['addresses']['mac'] }" )

            print( f"Estado:        { devScanner[host].state() }" )

            protocolsList = devScanner[host].all_protocols()

            if len( protocolsList ) > 0:
                print( "\n* Protocolos *" )

                for proto in devScanner[host].all_protocols():
                    print( f"\tProtocolo: { proto }" )
                    lport = devScanner[host][proto].keys()
                    #lport.sort()
                    for port in lport:
                        print ( f"\t\tPuerto: { port }\tEstado: { devScanner[host][proto][port]['state'] }" )

        print( separador )
    else:
        print( "\nNo se encontraron dispositivos en el segmento de red indicado." )


### Cuerpo del código para el script
print( "\n*** Ivan Escaneador de dispositivos en la red ***\n" )

devScanner = nmap.PortScanner()

ip = input( "Ingresa el Rango Ip: " )

print( "\nBuscando dispositivos presentes en la red del rango Ip indicado: ", ip )
print( "Un momento por favor, en breve le mostraré el resultado.\nDetectando..." )

devScanner.scan( ip )

printFoundHosts( devScanner.all_hosts() )


