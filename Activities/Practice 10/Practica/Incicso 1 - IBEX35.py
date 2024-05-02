import pandas as pd

path = './Activities/Practice 10/CSV/cotizacion.csv'

class IBEX35():
    def __init__(self, path):
        self.path = path
        self.dataCSV()
        self.min_dataFrame()
        self.med_dataFrame()
        self.max_dataFrame()
    
    def dataCSV(self):
        IBEX35 = pd.read_csv(self.path, sep=';')
        self.IBEX35 = IBEX35
        
    def min_dataFrame(self):
        self.min = self.IBEX35.loc[self.IBEX35['Mínimo'].idxmin()]
        print('Informacion del mínimo: ')
        print(self.min)
        
    def med_dataFrame(self):
        self.med = self.IBEX35['Final'].str.replace(',', '.').astype(float).mean()
        print('\nInformacion de la media: ')
        print('{:.2f}'.format(self.med))
        
    def max_dataFrame(self):
        self.max = self.IBEX35.loc[self.IBEX35['Máximo'].idxmax()]
        print('\nInformacion del máximo: ')
        print(self.max)
        
        
if __name__ == '__main__':
    IBEX35 = IBEX35(path)