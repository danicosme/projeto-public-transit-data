SELECT DISTINCT
    stop_id::VARCHAR             AS id_ponto,
    stop_name::VARCHAR           AS nome_ponto,
    stop_desc::VARCHAR           AS descricao_ponto,
    stop_lat::DOUBLE             AS latitude,
    stop_lon::DOUBLE             AS longitude,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')