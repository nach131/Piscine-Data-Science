
# https://matplotlib.org/stable/gallery/index.html


```python
fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')
```
- **`fig, ax = plt.subplots(1, 1, ...)`**: Crea una figura (`fig`) y un conjunto de ejes (`ax`) con `subplots()`.
  - `1, 1`: Número de filas y columnas del layout (es un solo gráfico, por eso 1x1).
  - `figsize=(8, 8)`: Tamaño de la figura en pulgadas (ancho y alto), lo que controla el tamaño del gráfico.
  - `layout='constrained'`: Utiliza `layout='constrained'` para ajustar automáticamente los márgenes y el espaciado del gráfico, evitando superposición de elementos.

```python
ax.bar(range(0, len(sales)), sales.values.tolist(), zorder=3)
```
- **`ax.bar(...)`**: Crea un gráfico de barras en los ejes `ax`.
  - `range(0, len(sales))`: Define las posiciones en el eje X para cada barra, generando una secuencia de números de 0 a `len(sales) - 1`.
  - `sales.values.tolist()`: Valores en el eje Y para cada barra. Convierte los valores de la serie `sales` a una lista.
  - `zorder=3`: Controla el orden de superposición (profundidad) de los elementos del gráfico. `zorder` más alto indica que se dibujará "encima" de otros elementos con valores menores de `zorder`. Esto se usa para asegurar que las barras no queden detrás de otros elementos del gráfico, como la cuadrícula.

```python
ax.margins(x=0)
```
- **`ax.margins(x=0)`**: Ajusta el margen adicional alrededor de las barras en el eje X. Establecer `x=0` elimina cualquier margen adicional, lo que asegura que las barras estén justo al inicio y final del eje X.

```python
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
```
- **`ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))`**: Establece la escala del eje X para que se muestre un tick (marca) en cada mes.
  - `mdates.MonthLocator(interval=1)`: `MonthLocator` crea un tick cada `interval` meses. En este caso, el intervalo es 1, así que cada mes tiene un tick.

```python
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
```
- **`ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))`**: Formatea las etiquetas del eje X para mostrar el nombre abreviado del mes (por ejemplo, `Jan`, `Feb`, etc.).
  - `mdates.DateFormatter('%b')`: Define el formato de la fecha. `%b` es el formato para mostrar los nombres cortos de los meses en inglés.

```python
ax.set_xticks(range(0, len(sales)), ['Oct', 'Nov', 'Dec'])
```
- **`ax.set_xticks(range(0, len(sales)), ['Oct', 'Nov', 'Dec'])`**: Establece los valores del eje X y las etiquetas de estos ticks.
  - `range(0, len(sales))`: Posiciones en el eje X para los ticks. Es un rango de 0 a la longitud de `sales` menos 1.
  - `['Oct', 'Nov', 'Dec']`: Lista de etiquetas personalizadas para cada tick. En este caso, asigna las etiquetas `'Oct'`, `'Nov'`, y `'Dec'` a las posiciones en el eje X.

```python
ax.set_ylabel('total sales in millions')
```
- **`ax.set_ylabel('total sales in millions')`**: Añade una etiqueta para el eje Y que indica la unidad de medida de las ventas (`total sales in millions`).

```python
ax.grid(axis='y', zorder=0)
```
- **`ax.grid(axis='y', zorder=0)`**: Añade una cuadrícula en el eje Y.
  - `axis='y'`: Aplica la cuadrícula solo al eje Y (horizontalmente).
  - `zorder=0`: Establece la profundidad de superposición de la cuadrícula. Al tener `zorder=0`, la cuadrícula aparecerá "debajo" de las barras, porque las barras tienen `zorder=3` (un valor mayor).

### ¿Qué Hace Este Código?

1. **Crea un gráfico de barras**: El gráfico muestra las ventas totales (`sales`) en diferentes posiciones del eje X, correspondientes a los meses `Oct`, `Nov`, y `Dec`.
2. **Formatea el eje X**: Muestra las etiquetas con los nombres abreviados de los meses.
3. **Establece un layout ajustado**: Configura un `figsize` grande y utiliza `layout='constrained'` para ajustar el espaciado.
4. **Añade una cuadrícula horizontal**: La cuadrícula solo se aplica al eje Y, con `zorder` bajo para que no se superponga con las barras.

Con esto, tienes una visualización personalizada que muestra las ventas en millones para cada mes en un formato claro y bien estructurado. ¿Hay algún detalle específico que te gustaría profundizar más?


data =
 pd.read_sql_query("SELECT event_time, user_id, price, user_session from customers where event_type = 'purchase'", con=connection)