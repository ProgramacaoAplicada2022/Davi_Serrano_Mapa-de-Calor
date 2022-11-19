import pandas as pd
'pip install openpyxl'
'pip install xlsxwriter'

localidades = 'brlocalidades.xlsx'
indicadores = 'indicadoressegurancapublicamunic.xlsx'

coordenadas = pd.read_excel(localidades)
coordenadas = coordenadas[['CD_GEOCODM','NM_MUNICIP','NM_UF','LAT','LONG']]

ocorrencias = pd.read_excel(indicadores)

writer = pd.ExcelWriter('combined_ocorrencias.xlsx',engine = 'xlsxwriter')
combined_ocorrencias = pd.DataFrame()

for sht in pd.ExcelFile(indicadores).sheet_names:
    df = pd.read_excel(indicadores, sheet_name=sht)
    combined_ocorrencias = combined_ocorrencias.append(df)
    combined_ocorrencias.to_excel(writer, sheet_name = "AllData", index = False)
writer.save()