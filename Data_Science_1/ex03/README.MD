
### 1. **Agregar nuevas columnas a la tabla `customers`**
```sql
ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(255),
ADD COLUMN brand VARCHAR(255);
```

- **Objetivo**: Este comando `ALTER TABLE` modifica la estructura de la tabla `customers` añadiendo tres nuevas columnas:
  1. `category_id` de tipo `BIGINT`.
  2. `category_code` de tipo `VARCHAR(255)` (cadena de caracteres con una longitud máxima de 255).
  3. `brand` de tipo `VARCHAR(255)`.

- **¿Por qué agregar columnas?**: Estas columnas están siendo añadidas para almacenar más información sobre los productos en la tabla `customers`, que actualmente no existía en dicha tabla.

### 2. **Actualizar la tabla `customers` con datos de `items`**
```sql
UPDATE customers c
SET
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM items i
WHERE c.product_id = i.product_id;
```

- **Objetivo**: Este comando `UPDATE` se utiliza para llenar las nuevas columnas `category_id`, `category_code` y `brand` en la tabla `customers` usando datos de otra tabla llamada `items`.

#### Detalles del comando `UPDATE`:
1. **`UPDATE customers c`**: Se especifica que se va a actualizar la tabla `customers` y se le asigna un alias `c` para simplificar la referencia a la tabla en el resto de la consulta.

2. **`SET category_id = i.category_id, category_code = i.category_code, brand = i.brand`**: 
   - Indica qué columnas de la tabla `customers` se van a actualizar (`category_id`, `category_code` y `brand`) y con qué valores.
   - `i.category_id`, `i.category_code`, y `i.brand` son los valores provenientes de la tabla `items` (que también se referencia con un alias `i`).

3. **`FROM items i`**: 
   - Se especifica la tabla `items` que se usará para tomar los datos de actualización.
   - Esta tabla contiene la información adicional que queremos fusionar con la tabla `customers`.

4. **`WHERE c.product_id = i.product_id`**:
   - Esta es la condición de unión entre las dos tablas.
   - Se asegura de que solo se actualicen las filas de `customers` donde el `product_id` coincide con el `product_id` de `items`.
   - De esta manera, los valores `category_id`, `category_code` y `brand` de la tabla `items` se asignan a las filas correspondientes en la tabla `customers` que tienen el mismo `product_id`.

### 3. **Ejemplo para visualizar**
Imagina que tienes la siguiente estructura y datos en ambas tablas:

**Tabla `customers`** (antes de agregar columnas):

| customer_id | product_id |
|-------------|------------|
| 1           | 1001       |
| 2           | 1002       |

**Tabla `items`**:

| product_id | category_id | category_code | brand    |
|------------|-------------|---------------|---------|
| 1001       | 200         | electronics   | Sony    |
| 1002       | 201         | appliances    | Samsung |

Después de ejecutar el comando `ALTER TABLE`, la tabla `customers` tendrá las nuevas columnas con valores `NULL`:

**Tabla `customers`** (después de agregar columnas):

| customer_id | product_id | category_id | category_code | brand |
|-------------|------------|-------------|---------------|-------|
| 1           | 1001       | NULL        | NULL          | NULL  |
| 2           | 1002       | NULL        | NULL          | NULL  |

Después de ejecutar el comando `UPDATE`, la tabla `customers` se actualizará con los valores de `items` para las filas que tengan el mismo `product_id`:

**Tabla `customers`** (después del `UPDATE`):

| customer_id | product_id | category_id | category_code | brand  |
|-------------|------------|-------------|---------------|--------|
| 1           | 1001       | 200         | electronics   | Sony   |
| 2           | 1002       | 201         | appliances    | Samsung|

