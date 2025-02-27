# archivo-apendice.py
while True:
    print ("ingrese palabra clave, nn para salir del programa") 
    palabraclave = input ()
    if palabraclave == 'nn':
        print("Muchas gracias")
        break
    f = open('tema.txt','a')
    f.write( "," + palabraclave)
f.close()
