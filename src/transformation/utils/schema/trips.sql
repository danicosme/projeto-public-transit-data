SELECT DISTINCT
    route_id::VARCHAR            AS id_linha,
    service_id::VARCHAR          AS id_servico,
    trip_id::VARCHAR             AS id_viagem,
    trip_headsign::VARCHAR       AS cabecalho_viagem,
    direction_id::VARCHAR        AS sentido,
    shape_id::VARCHAR            AS id_trajeto,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')