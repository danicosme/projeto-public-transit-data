SELECT DISTINCT
    fare_id::VARCHAR             AS id_tarifa,
    price::DOUBLE                AS preco,
    currency_type::VARCHAR       AS tipo_moeda,
    payment_method::INT          AS metodo_pagamento,
    transfers::INT               AS numero_transferencias,
    transfer_duration::INT       AS duracao_transferencia,
    '{extraction_date}'::DATE    AS data_extracao
FROM read_csv_auto('{txt_path}', delim=',')