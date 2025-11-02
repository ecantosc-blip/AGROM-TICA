# sesion2_lectura_masiva.py
# Lee todas las secuencias de ls_orchid.fasta usando Bio.SeqIO y calcula estadísticas básicas.
# Requisitos: biopython instalado (pip install biopython)

from Bio import SeqIO
import statistics

def resumen_secuencias(fasta_path="ls_orchid.fasta"):
    longitudes = []
    ids = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        ids.append(record.id)
        longitudes.append(len(record.seq))

    total = len(longitudes)
    if total == 0:
        return {
            'total': 0,
            'longitudes': [],
            'promedio': 0,
            'maxima': 0,
            'minima': 0,
            'ids': []
        }

    promedio = statistics.mean(longitudes)
    maxima = max(longitudes)
    minima = min(longitudes)
    indice_max = longitudes.index(maxima)
    id_max = ids[indice_max]

    return {
        'total': total,
        'longitudes': longitudes,
        'promedio': promedio,
        'maxima': maxima,
        'minima': minima,
        'id_max': id_max,
        'ids': ids
    }

def main():
    fasta = "ls_orchid.fasta"
    try:
        resumen = resumen_secuencias(fasta)
    except FileNotFoundError:
        print(f"Error: no se encontró {fasta}. Coloca el archivo en la misma carpeta.")
        return

    print("=== RESUMEN DE SECUENCIAS ===")
    print("Número total de secuencias:", resumen['total'])
    if resumen['total'] > 0:
        print("Longitud promedio: {:.2f}".format(resumen['promedio']))
        print("Secuencia más larga (id):", resumen['id_max'])
        print("Longitud más larga:", resumen['maxima'])
        print("Longitud mínima:", resumen['minima'])

        # Guardar longitudes en un archivo txt
        with open("longitudes.txt", "w") as out:
            out.write("id\tlongitud\n")
            for id_, l in zip(resumen['ids'], resumen['longitudes']):
                out.write(f"{id_}\t{l}\n")
        print("Se guardó 'longitudes.txt' con la lista de longitudes.")

if __name__ == "__main__":
    main()
