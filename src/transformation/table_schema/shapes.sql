SELECT
    shape_id::VARCHAR            AS id_trajeto,
    shape_pt_lat::DOUBLE         AS latitude,
    shape_pt_lon::DOUBLE         AS longitude,
    shape_pt_sequence::INT       AS ordem_ponto,
    shape_dist_traveled::DOUBLE  AS distancia_percorrida,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')