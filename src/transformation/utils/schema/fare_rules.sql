SELECT DISTINCT
    fare_id::VARCHAR             AS id_tarifa,
    route_id::VARCHAR            AS id_linha,
    origin_id::VARCHAR           AS id_origem,
    destination_id::VARCHAR      AS id_destino,
    contains_id::VARCHAR         AS id_contido,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')