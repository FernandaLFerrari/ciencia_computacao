from fpdf import FPDF
from datetime import datetime, timedelta
import os
import pandas as pd

'''importar arquivo de metadados para as informações principais'''

df = pd.read_csv("C:/Users/Usuario/Downloads/JLL828-003_GRCh37.csv", sep=";")

df