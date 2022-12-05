# Davi_Serrano_Mapa-de-Calor
# Motivação
- Evitar passar por locais perigosos ao frequentar locais novos.

# Conceito
- Nosso aplicativo pega uma base de dados com índice de criminalidade e pinta um mapa de calor para destacar os locais perigosos.

# Funcionamento
- A idéia é popularmos um banco de dados com notícias e dados de várias fontes e deixá-lo disponível no google firestore. Após isso, o aplicativo consulta o banco de dados para gerar o mapa de calor, então seria uma estratégia para popular o banco de dados e o código que gera o mapa de calor.

# Grupo
- Davi Alcantara Pereira Lima (3º Ano Elétrica)
- Guilherme Malavazi Serrano (3º Ano Elétrica)

# Tutorial Mapas Folium

1. Passo 1
- Instalar python

2. Passo 2
- Instalar e importar bibliotecas:
'pip install folium'

'import folium'
'import pandas'
'from folium.plugins import HeatMap'

3. Passo 3
- Importar arquivo que será usado no mapa:

'pesos = pd.read_excel('pesos.xlsx')'
'coordenadas = pd.read_excel('coordenadas.xlsx')'
'final = pd.merge(pesos, coordenadas)'

- Estamos usando esse merge caso um arquivo contenha locais com coordenadas e o outro contenha os índices de criminalidade para cada coordenada, assim conseguimos unir as informações de pesos no mapa de calor juntamente com as localidades.

4. Passo 4
- Criar o mapa:

'mapa = folium.map(location=[lat,lng],zoom_start=z)'

- Aqui conseguimos criar o mapa, definir posição de início e zoom adequado, seria possível também já abrir o mapa orientado para a posição do usuário.

5. Passo 5
- Apresentar informações no mapa:

'HeatMap([[lat1,long1,weigth1],
[lat2,long2,weigth2],
[lat3,long3,weigth3], etc], radius=r).add_to(mapa)'

- Basicamente é uma lista com coordenadas e pesos, nesse exemplo estão listas mas a idéia é que já usaremos o dataframe "final" declarado anteriormente.

6. Passo 6
- Salvar mapa:
'mapa.save('nome.html')'

- Basicamente esse é o comando que gera o nosso mapa, usaremos essa biblioteca gráfica do tutorial para ser disponibilizada em um frameword de flask em um site que será acessado pelo usuário.

# Telas do aplicativo

### Mapa funcional
![Tela de login](tela_final.jpg)
![Mapa Funcional](tela_final2.jpg)


