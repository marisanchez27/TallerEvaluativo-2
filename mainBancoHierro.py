from bancoHierroClases.Cuenta import Cuenta

opcion=1
cuenta=Cuenta(0)

# cuenta.consultarSaldo=12350000
# print (f"mi saldo es: {cuenta.consultarSaldo}")

while(opcion!=0):
    
    opcion=int(input("digite una opcion: "))

    if(opcion==1):
        cantidadIngresar=int(input("ingrese la cantidad a consignar: "))
        cantidadRetirar=int(input("El saldo a retirar es de: "))
        
        #cuenta=Cuenta(saldo)

        cuenta.ingresarSaldo(cantidadIngresar)
        cuenta.retirarSaldo(cantidadRetirar)
print (f"mi saldo es: {cuenta.saldo}")



# • Se debe permitir consultar saldo en cualquier momento
# • Se debe permitir ingresar o retirar dinero cuando se desee