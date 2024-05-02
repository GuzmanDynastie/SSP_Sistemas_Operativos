import pandas as pd
import matplotlib.pyplot as plt

def diagrama_cotizaciones_cierre(file_path):
    df = pd.read_csv(file_path)

    df['Fecha'] = pd.to_datetime(df['Fecha'])

    for empresa, datos_empresa in df.groupby('Empresa'):
        plt.plot(datos_empresa['Fecha'], datos_empresa['Cierre'], label=empresa)

    plt.xlabel('Fecha')
    plt.ylabel('Precio de Cierre')
    plt.title('Cotizaciones de Cierre de Bancos')
    plt.legend()
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

diagrama_cotizaciones_cierre('./Activities/Practice 10/CSV/bancos.csv')