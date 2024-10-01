
```sql
WITH duplicates AS (
    SELECT 
        ctid,  -- ctid se usa para identificar filas únicas en PostgreSQL
        event_time,
        event_type,
        product_id,
        LEAD(event_time) OVER (PARTITION BY event_type, product_id ORDER BY event_time) AS next_event_time
    FROM 
        customers
)
DELETE FROM customers
USING duplicates
WHERE 
    customers.ctid = duplicates.ctid
    AND duplicates.next_event_time IS NOT NULL  -- Asegurar que haya un siguiente evento
    AND duplicates.event_type = customers.event_type
    AND duplicates.product_id = customers.product_id
    AND EXTRACT(EPOCH FROM (duplicates.next_event_time - duplicates.event_time)) <= 1;
```


1. **CTE `duplicates`**:
   - Crea una tabla temporal que selecciona las columnas `ctid`, `event_time`, `event_type`, y `product_id`.
   - Usa la función `LEAD(event_time)` para obtener el `event_time` del siguiente registro en la tabla, dentro del mismo grupo de `event_type` y `product_id` (`PARTITION BY event_type, product_id`).
   - `ORDER BY event_time` asegura que la comparación se haga de manera cronológica.

2. **DELETE**:
   - El `DELETE` elimina los registros de `customers` que coincidan con las filas duplicadas en el CTE `duplicates`.
   - `customers.ctid = duplicates.ctid` garantiza que se elimine la fila correcta de la tabla.
   - La condición `EXTRACT(EPOCH FROM (duplicates.next_event_time - duplicates.event_time)) <= 1` se asegura de que se eliminen solo las filas que tengan una diferencia de `event_time` de 1 segundo o menos con el siguiente evento.

3. **Condiciones adicionales**:
   - `duplicates.next_event_time IS NOT NULL` se asegura de que se realice la comparación solo si existe un siguiente evento.
   - `duplicates.event_type = customers.event_type` y `duplicates.product_id = customers.product_id` se aseguran de que los eventos a comparar sean del mismo tipo y producto.

### ¿Cómo funciona?

Si tienes dos eventos consecutivos para el mismo `event_type` y `product_id` con los siguientes valores:

```
event_time               | event_type          | product_id 
-------------------------|---------------------|-------------
2022-10-01 00:00:32      | remove_from_cart    | 5779403
2022-10-01 00:00:33      | remove_from_cart    | 5779403
```

La consulta:

1. Detectará que estos eventos tienen la misma combinación de `event_type` y `product_id`.
2. Calculará la diferencia de tiempo (`EXTRACT(EPOCH FROM (duplicates.next_event_time - duplicates.event_time))`), que en este caso será `1` segundo.
3. Como la diferencia es igual o menor a `1` segundo, se eliminará uno de estos eventos duplicados.

