"""
Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
La función debe devolver el monto del descuento calculado.

Llamada a la Función:

Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.
Salida de Resultados:

Muestra los resultados de las llamadas a la función, incluyendo el monto del descuento y el monto final a pagar después del descuento.
Subida del Código: """

# Compre un celular Honor en $800 en na tienda HONOR el vendedor me indico que tenia un descuento del 10% por ser mi primera compra con ellos adicional adquirí una laptop a 1000 y tambien obtuve un descuento del 15%, ¿Cuánto debo pagar en total por cada producto?
def calcular_descuento(monto_total, porcentaje_descuento=10):
     return  monto_total * (porcentaje_descuento/100)

if __name__=="__main__":
    #Datos de compra
    monto_celular = 800 #Valor de celular Honor
    descuento_celular_defecto= 10 #Descuento por primera compra
    monto_laptop= 1000 # Precio de una laptop
    descuento_laptop= 15 #Descuento para la laptop

#Cálcular descuentos y montos finales
    ## llamada celular Honor
    descuento_celular = calcular_descuento (monto_celular)
    monto_final_celular= monto_celular - descuento_celular
    ## llamada Laptop
    descuento_laptop_valor = calcular_descuento(monto_laptop, descuento_laptop)
    monto_final_laptop = monto_laptop - descuento_laptop_valor
#Mostrar resultados
    print("###Resumen de Compras###")
    #Celular Honor
    print(f"#compra 1: Celular Honor")
    print(f"Monto total:${monto_celular:.2f}")
    print(f"Descuento aplicado ({descuento_celular_defecto}%):${descuento_celular:.2f}")
    print(f"Monto final a cancelar:${monto_final_celular:.2f}")
    #Laptop
    print(f"#compra 2: Laptop")
    print(f"Monto total:${monto_laptop:.2f}")
    print(f"Descuento aplicado ({descuento_laptop}%):${descuento_laptop_valor:.2f}")
    print(f"Monto final a laptop:${monto_final_laptop:.2f}")

