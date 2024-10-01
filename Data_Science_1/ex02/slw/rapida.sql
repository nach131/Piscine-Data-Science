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



-- 147.88 segundos. 2,4 minutos