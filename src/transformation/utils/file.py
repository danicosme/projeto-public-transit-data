class FileManipulator:
    def __init__(self):
        pass
        
    def file_name_mapping(self):
        return {
        "agency.txt": "agencias",
        "calendar.txt": "calendario_servico",
        "fare_attributes.txt": "tarifas_atributos",
        "fare_rules.txt": "regras_tarifarias",
        "frequencies.txt": "frequencias_veiculos",
        "routes.txt": "rotas",
        "shapes.txt": "trajetos_geograficos",
        "stops.txt": "pontos_parada",
        "stop_times.txt": "horarios_paradas",
        "trips.txt": "viagens"}
    
    def write_temp_file(self, file_name, zip_file, txt_path):
        with zip_file.open(file_name) as txt_file:
            with open(txt_path, "wb") as f_out:
                f_out.write(txt_file.read())