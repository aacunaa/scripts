#Desde un archivo .csv extrae una columna que esté en formato .json, extrae la info y parsea los datos para que cada atributo sea una columna de un archivo .xlsx  
#Use example:
#python script.py ruta/al/archivo.csv nombre_de_la_columna ruta/al/salida.xlsx

import csv
import json
import argparse
from openpyxl import Workbook

def read_csv_column_as_json(csv_file_path, column_name):
    json_objects = []
    
    # Leer el archivo CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Iterar sobre cada fila del CSV
        for row in csv_reader:
            # Extraer el contenido de la columna específica
            json_content = row[column_name]
            
            # Convertir el contenido de JSON de texto a un objeto JSON
            try:
                json_object = json.loads(json_content)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
                continue
    
    return json_objects

def convert_json_values_to_str(json_object):
    for key, value in json_object.items():
        if isinstance(value, dict) or isinstance(value, list):
            json_object[key] = json.dumps(value, ensure_ascii=False)
    return json_object

def write_json_to_excel(json_objects, output_excel_path):
    # Crear un nuevo libro de trabajo de Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "JSON Data"
    
    # Obtener todas las claves únicas de los objetos JSON para los encabezados de las columnas
    all_keys = set()
    for json_object in json_objects:
        all_keys.update(json_object.keys())
    
    # Convertir el conjunto de claves a una lista y ordenarla (opcional)
    all_keys = sorted(list(all_keys))
    
    # Escribir los encabezados en la primera fila
    sheet.append(all_keys)
    
    # Escribir cada objeto JSON en una nueva fila
    for json_object in json_objects:
        json_object = convert_json_values_to_str(json_object)
        row = [json_object.get(key, None) for key in all_keys]
        sheet.append(row)
    
    # Guardar el libro de trabajo en el archivo especificado
    workbook.save(output_excel_path)

def main():
    parser = argparse.ArgumentParser(description='Convert JSON from a CSV column to an Excel file.')
    parser.add_argument('csv_file_path', type=str, help='Ruta del archivo CSV')
    parser.add_argument('column_name', type=str, help='Nombre de la columna que contiene el JSON')
    parser.add_argument('output_excel_path', type=str, help='Ruta del archivo Excel de salida')
    
    args = parser.parse_args()
    
    # Obtener la lista de objetos JSON
    json_objects = read_csv_column_as_json(args.csv_file_path, args.column_name)
    
    # Escribir los objetos JSON en un archivo Excel
    write_json_to_excel(json_objects, args.output_excel_path)
    
    print(f"El archivo Excel se ha guardado en: {args.output_excel_path}")

if __name__ == "__main__":
    main()
