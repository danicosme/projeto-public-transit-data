SELECT
    trip_id::VARCHAR             AS id_viagem,
    start_time::VARCHAR          AS horario_inicio,
    end_time::VARCHAR            AS horario_fim,
    headway_secs::INT            AS intervalo_segundos,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')