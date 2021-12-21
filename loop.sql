DO $$
    DECLARE
        dist_id   disipline.dist_id%TYPE;
        dist_name disipline.dist_name%TYPE;
    BEGIN
        dist_id := 6;
        dist_name := 'sport';
        FOR counter IN 1..10
            LOOP
                INSERT INTO disipline(dist_id, dist_name)
                VALUES (counter + disipline.dist_id, dist_name || counter);
            END LOOP;
    END;
$$