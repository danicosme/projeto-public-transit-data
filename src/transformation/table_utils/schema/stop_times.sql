SELECT
    trip_id::VARCHAR             AS id_viagem,
    arrival_time::VARCHAR        AS horario_chegada,
    departure_time::VARCHAR      AS horario_partida,
    stop_id::VARCHAR             AS id_ponto,
    stop_sequence::INT           AS ordem_parada,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')