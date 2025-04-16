SELECT DISTINCT
    service_id::VARCHAR          AS id_servico,
    monday::INT                  AS segunda,
    tuesday::INT                 AS terca,
    wednesday::INT               AS quarta,
    thursday::INT                AS quinta,
    friday::INT                  AS sexta,
    saturday::INT                AS sabado,
    sunday::INT                  AS domingo,
    start_date::VARCHAR          AS data_inicio,
    end_date::VARCHAR            AS data_fim,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')