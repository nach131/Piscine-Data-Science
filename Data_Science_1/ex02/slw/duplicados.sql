SELECT 
    a.user_id,
    a.event_type,
    a.event_time AS current_event_time,
    b.event_time AS previous_event_time,
    EXTRACT(EPOCH FROM a.event_time - b.event_time) AS time_difference_in_seconds
FROM 
    customers a
JOIN 
    customers b ON a.event_type = b.event_type
WHERE 
    a.event_time > b.event_time
    AND EXTRACT(EPOCH FROM a.event_time - b.event_time) >= 1
ORDER BY 
    a.event_type, a.event_time;
