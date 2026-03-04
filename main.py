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

    print()

    if Operacion == 1:

        print("El saldo actual es de ", Saldo)

    elif Operacion == 2:

        monto = int(input("Cuanto va a retirar = "))

        print()

        if monto > Saldo:
            
            print("Fondos insuficientes")
        
        elif monto <= Saldo and monto != 0:

            print("Acabas de retirar", monto)
            
            print()

            Saldo_Actual = Saldo - monto

            print("Saldo actual es", Saldo_Actual )

            print()
        
        else:
            while monto <= 0:
                print("Monto equivocado, intente nuevamente")

                monto = int(input("Cuanto va a retirar = "))

                print()

                if monto > Saldo:
            
                    print("Fondos insuficientes")
        
                elif monto <= Saldo and monto != 0:

                    print("Acabas de retirar", monto)
                    
                    print()

                    Saldo_Actual = Saldo - monto

                    print("Saldo actual es", Saldo_Actual )

                    print()
    
    elif Operacion == 3:

        monto = int(input("Cuanto va a depositar = "))

        print ()

        while monto <= 0:
                print("Monto equivocado, intente nuevamente")

                monto = int(input("Cuanto va a depositar = "))

                print()

                if monto > 0:

                    Fondo = monto + Saldo
            
                    print("El nuevo saldo es", Fondo)

                print()