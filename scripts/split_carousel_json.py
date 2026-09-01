import json
import os

INPUT_FILE = "carousel_ES.json"

def main():
    # Leer el archivo de entrada
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Verificar que es una lista
    if not isinstance(data, list):
        print("El archivo de entrada no contiene un array de objetos.")
        return

    for obj in data:
        # Obtener el id y el type para el nombre del archivo y carpeta
        obj_id = obj.get("id")
        obj_type = obj.get("type")
        if not obj_id or not obj_type:
            print("Objeto sin campo 'id' o 'type', se omite:", obj)
            continue

        # Crear la carpeta si no existe
        os.makedirs(obj_type, exist_ok=True)
        filename = os.path.join(obj_type, f"{obj_id}.json")
        # Escribir el objeto en un archivo individual
        with open(filename, "w", encoding="utf-8") as out_f:
            json.dump(obj, out_f, ensure_ascii=True, indent=4)

    print(f"Se han creado {len(data)} archivos JSON individuales en carpetas por tipo.")

if __name__ == "__main__":
    main()
