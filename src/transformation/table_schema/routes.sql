SELECT
    route_id::VARCHAR            AS id_linha,
    agency_id::VARCHAR           AS id_agencia,
    route_short_name::VARCHAR    AS nome_curto_linha,
    route_long_name::VARCHAR     AS nome_longo_linha,
    route_type::INT              AS tipo_linha,
    route_color::VARCHAR         AS cor_linha,
    route_text_color::VARCHAR    AS cor_texto_linha,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')