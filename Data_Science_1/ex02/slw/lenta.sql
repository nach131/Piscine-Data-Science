    WITH duplicates AS (
    SELECT ctid
    FROM (
        SELECT
        ctid,
        ROW_NUMBER() OVER (PARTITION BY user_id, event_time, user_session, product_id, price, event_type ORDER BY ctid) AS row_num
        FROM
        {table}
    ) subquery
    WHERE row_num > 1
    )
    DELETE FROM {table}
    USING duplicates
    WHERE {table}.ctid = duplicates.ctid;

-- 1747.49 segundos. 29 minutos