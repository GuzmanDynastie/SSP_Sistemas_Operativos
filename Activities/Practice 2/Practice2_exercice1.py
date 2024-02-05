'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla 
una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

def calculate_discount(sales):
    return sales * (0.9)

while True:
    try:
        initial_year = int(input("Ingrese el año de inicio: "))
        final_year = int(input("Ingrese el ultimo año: "))
        print("\n")

        annual_sales = pd.DataFrame(columns=["Año", "Ventas"])

        for year in range(initial_year, final_year + 1):
            sales = float(input(f'Ingrese las ventas por año {year}: '))

            rows_no_empty = pd.DataFrame({"Año": [year], "Ventas": [sales]})
            annual_sales = pd.concat([annual_sales, pd.DataFrame({"Año": [year], "Ventas": [sales]})], ignore_index=True)

        annual_sales["Ventas con descuento"] = calculate_discount(annual_sales["Ventas"])
        
        print("\n -- Ventas originales --")
        print(annual_sales[["Año", "Ventas"]])

        print("\n -- Ventas con el descuento --")
        print(annual_sales[["Año", "Ventas con descuento"]])
        break
    
    except ValueError:
        print("Por favor, ingrese números enteros validos.")