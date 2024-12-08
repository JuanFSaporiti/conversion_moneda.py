 # Paso1: Definir el valor actual del Euro y Dolar can respecto al Peso Mexicano.

tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

 # Paso2: Solicitar al usuario el tipo de conversion.

tipo_conversion = input("ingrese la moneda origen para la conversion (EUR/USD): ")

 # Paso3: Solicitar al ususario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

 # Paso4: Realizar la conversionutilizando el tipo de cambio correspndiente.

if tipo_conversion.upper() == "EUR":
   resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
   print("El resutlado de la conversion de EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD":
     resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
     print("El resultado de al conversion de USD a MXN es:",resultado)
else:
    print("No esta disponible este tipo de conversion actualmente")