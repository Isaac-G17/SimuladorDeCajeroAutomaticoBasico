print()

print("CAJERO AUTOMÁTICO")

print()

Saldo= 1000
Numero_Operaciones = int(input("Cuantas operaciones desea realizar = "))

print()

for i in range(Numero_Operaciones):

    print()

    print("OPERACIONES QUE PUEDE REALIZAR")

    print()

    print("1 → Consultar saldo")
    print("2 → Retirar dinero")
    print("3 → Depositar dinero")

    print()

    Operacion = int(input("Escoge la opcion a realizar = "))

    while Operacion not in (1,2,3):

        print()
         
        print("Opción inválida") 

        print()

        Operacion = int(input("Intenta nuevamente = "))

    print()

    if Operacion == 1:

        print("El saldo actual es de ", Saldo)

    elif Operacion == 2:

        monto = int(input("Cuanto va a retirar = "))

        print()

        while monto <= 0:
                print("Monto equivocado, intente nuevamente")

                monto = int(input("Cuanto va a retirar = "))

                print()

        if monto > Saldo:
            
            print("Fondos insuficientes")
        
        else:
            
            Saldo <= Saldo and monto != 0

            print("Acabas de retirar", monto)
            
            print()

            Saldo= Saldo - monto

            print("Saldo actual es", Saldo)

            print()
    
    elif Operacion == 3:

        monto = int(input("Cuanto va a depositar = "))

        print ()

        while monto <= 0:
                
                print("Monto equivocado, intente nuevamente")

                monto = int(input("Cuanto va a depositar = "))

                print()

        else: 

            monto > 0

            print()

            Saldo = monto + Saldo
            
            print("El nuevo saldo es", Saldo)

            print()

else: 
    
    Operacion == (1 or 2 or 3)

    print()        
        
    print("Gracias por usar el cajero automático")

    print()                
