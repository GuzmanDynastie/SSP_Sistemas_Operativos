import pandas as pd
import numpy as np
from datetime import datetime

emisiones_2016 = './Activities/Practice 10/CSV/emisiones-2016.csv'
emisiones_2017 = './Activities/Practice 10/CSV/emisiones-2016.csv'
emisiones_2018 = './Activities/Practice 10/CSV/emisiones-2016.csv'
emisiones_2019 = './Activities/Practice 10/CSV/emisiones-2016.csv'

class Emisiones():
    def __init__(self, paths):
        self.paths = paths
        self.dataCSV()
        
    def dataCSV(self):
        dfs = []
        for path in self.paths:
            df = pd.read_csv(path, sep=';')
            dfs.append(df)
        self.df = pd.concat(dfs, ignore_index=True)
        
    def show_menu(self):
        while True:
            print("Seleccione una opción:")
            print("1. Filtrar columnas")
            print("2. Restructurar DataFrame")
            print("3. Mostrar DataFrame reestructurado")
            print("4. Agregar columna de fecha")
            print("5. Limpiar y ordenar datos")
            print("6. Eliminar filas no válidas y ordenar")
            print("7. Mostrar estaciones y contaminantes")
            print("8. Obtener emisiones")
            print("9. Resumen de contaminantes")
            print("10. Resumen de contaminantes por distrito")
            print("11. Resumen de emisiones por estación y contaminante")
            print("12. Emisiones medias mensuales de un contaminante en un año")
            print("13. Medias mensuales de distintos contaminantes en una estación")
            print("0. Salir")

            option = input("Ingrese el número de la opción que desea ejecutar: ")

            if option == '1':
                self.filterColumns()
            elif option == '2':
                self.restructureDataFrame()
            elif option == '3':
                self.df_reestructurado()
            elif option == '4':
                self.agregar_columna_fecha()
            elif option == '5':
                self.limpiar_ordenar_datos()
            elif option == '6':
                self.eliminar_filas_no_validas_y_ordenar()
            elif option == '7':
                self.mostrar_estaciones_y_contaminantes()
            elif option == '8':
                self.obtener_emisiones()
            elif option == '9':
                self.resumen_contaminantes()
            elif option == '10':
                self.resumen_contaminantes_por_distrito()
            elif option == '11':
                estacion = int(input("Ingrese el número de estación: "))
                contaminante = int(input("Ingrese el número de contaminante: "))
                self.resumen_emisiones_estacion_contaminante(estacion, contaminante)
            elif option == '12':
                contaminante = int(input("Ingrese el número de contaminante: "))
                anio = int(input("Ingrese el año: "))
                self.emisiones_medias_mensuales_contaminante_anio(contaminante, anio)
            elif option == '13':
                estacion = int(input("Ingrese el número de estación: "))
                self.medias_mensuales_distintos_contaminantes(estacion)
            elif option == '0':
                print("Saliendo...")
                break
            else:
                print("Opción no válida")
        
    def filterColumns(self):
        self.df = self.df[['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + [f'D{str(day).zfill(2)}' for day in range(1, 32)]]
        print(self.df)
        
    def restructureDataFrame(self):
        self.df = pd.melt(self.df, id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA')
        print(self.df)
        
    def df_reestructurado(self):
        df_reestructurado = pd.melt(self.df, id_vars=["PROVINCIA", "MUNICIPIO", "ESTACION", "MAGNITUD", "PUNTO_MUESTREO", "ANO", "MES"],
                                    var_name="DIA", value_name="VALOR")
        df_reestructurado.to_csv('./Activities/Practice 10/CSV/datos_reestructurados.csv', index=False)
        
    def agregar_columna_fecha(self):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/datos_reestructurados.csv')

        def create_date(row):
            year = int(row['ANO'])
            month = int(row['MES'])
            day_str = str(row['DIA'])[1:]  # Eliminar el primer carácter (D) del nombre del día
            day = int(day_str)
            max_day = 31  # Asigna el valor máximo predeterminado
            if month in [4, 6, 9, 11]:  # Meses con 30 días
                max_day = 30
            elif month == 2:  # Febrero
                max_day = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
            if day > max_day:
                # Si el día excede el máximo para el mes, establece el día en el máximo
                day = max_day
            return datetime(year, month, day)

        datos_reestructurados['FECHA'] = datos_reestructurados.apply(create_date, axis=1)
        datos_reestructurados.to_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv')
        print(datos_reestructurados)
    
    def eliminar_filas_no_validas_y_ordenar(self):
        df = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv')
        df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')
        df = df.dropna(subset=['FECHA'])  # Eliminar filas con fechas no válidas
        df = df.sort_values(by=['ESTACION', 'FECHA'])  # Ordenar por estaciones contaminantes y fecha
        print(df)
    
    def mostrar_estaciones_y_contaminantes(self):
        print("Estaciones disponibles:")
        print(self.df['ESTACION'].unique())

        print("\nContaminantes disponibles:")
        print(self.df['MAGNITUD'].unique())
    
    def obtener_emisiones(self):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])

        contaminante = 1
        estacion = 4
        fecha_inicio = pd.to_datetime('2016-01-01')
        fecha_fin = pd.to_datetime('2016-01-31')

        filtro = (datos_reestructurados['ESTACION'] == estacion) & \
                (datos_reestructurados['MAGNITUD'] == contaminante) & \
                (datos_reestructurados['FECHA'] >= fecha_inicio) & \
                (datos_reestructurados['FECHA'] <= fecha_fin)
        emisiones_filtradas = datos_reestructurados.loc[filtro]

        serie_emisiones = emisiones_filtradas['VALOR']

        print("Emisiones de contaminante {} en la estación {} para el rango de fechas:".format(contaminante, estacion))
        print(serie_emisiones)
    
    def resumen_contaminantes(self):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])
        resumen = datos_reestructurados.groupby('MAGNITUD')['VALOR'].describe()
        print("Resumen descriptivo para cada contaminante:")
        print(resumen)

    def resumen_contaminantes_por_distrito(self):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])
        resumen = datos_reestructurados.groupby(['PROVINCIA', 'MAGNITUD'])['VALOR'].describe()
        print("Resumen descriptivo para cada contaminante por distrito:")
        print(resumen)

    def resumen_emisiones_estacion_contaminante(self, estacion, contaminante):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])

        filtro = (datos_reestructurados['ESTACION'] == estacion) & \
                (datos_reestructurados['MAGNITUD'] == contaminante)
        emisiones_filtradas = datos_reestructurados.loc[filtro]

        resumen = emisiones_filtradas['VALOR'].describe()
        print(f"Resumen descriptivo de las emisiones del contaminante {contaminante} en la estación {estacion}:")
        print(resumen)


    def emisiones_medias_mensuales_contaminante_anio(self, contaminante, anio):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])

        filtro = (datos_reestructurados['MAGNITUD'] == contaminante) & \
                (datos_reestructurados['ANO'] == anio)
        emisiones_filtradas = datos_reestructurados.loc[filtro]

        emisiones_filtradas['VALOR'] = pd.to_numeric(emisiones_filtradas['VALOR'], errors='coerce')
        emisiones_medias_mensuales = emisiones_filtradas.groupby('MES')['VALOR'].mean()
        print(f"Emisiones medias mensuales del contaminante {contaminante} para el año {anio}:")
        print(emisiones_medias_mensuales)


    def medias_mensuales_distintos_contaminantes(self, estacion):
        datos_reestructurados = pd.read_csv('./Activities/Practice 10/CSV/new_datos_reestructurados.csv', parse_dates=['FECHA'])
        
        filtro = (datos_reestructurados['ESTACION'] == estacion)
        emisiones_estacion = datos_reestructurados.loc[filtro]
        
        emisiones_estacion['VALOR'] = pd.to_numeric(emisiones_estacion['VALOR'], errors='coerce')

        valores_no_numericos = emisiones_estacion[emisiones_estacion['VALOR'].isna()]
        print("Valores no numéricos en la columna 'VALOR':")
        print(valores_no_numericos)
        
        # Calcular medias mensuales solo con valores numéricos
        medias_mensuales = emisiones_estacion.groupby(['MAGNITUD', 'MES'])['VALOR'].mean().unstack()
        print(f"Medias mensuales de los distintos contaminantes para la estación {estacion}:")
        print(medias_mensuales)
    
        
if __name__ == '__main__':
    emisiones = Emisiones([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])
    emisiones.show_menu()