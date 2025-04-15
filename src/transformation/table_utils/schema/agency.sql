SELECT 
    agency_id::INT                    AS id_agencia,
    agency_name::VARCHAR              AS nome_agencia,
    agency_url::VARCHAR               AS url_agencia,
    agency_timezone::VARCHAR          AS fuso_horario_agencia,
    agency_lang::VARCHAR              AS idioma_agencia,
    '{extraction_date}'::DATE         AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')
