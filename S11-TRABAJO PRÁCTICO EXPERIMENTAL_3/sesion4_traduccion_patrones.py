# sesion4_traduccion_patrones.py
# Traducción de secuencias DNA a proteínas y búsqueda de motivos
# Requisitos: biopython instalado (pip install biopython)

from Bio.Seq import Seq
from Bio import SeqIO

def traducir_secuencia(dna_seq):
    """Traduce la secuencia DNA a proteína."""
    seq_obj = Seq(dna_seq)
    proteina = seq_obj.translate()
    return str(proteina)

def buscar_motivos(dna_seq, motivos):
    """Busca posiciones de cada motivo en la secuencia."""
    resultados = {}
    seq_str = dna_seq.upper()
    for motivo in motivos:
        pos = []
        start = 0
        while True:
            idx = seq_str.find(motivo.upper(), start)
            if idx == -1:
                break
            pos.append(idx)
            start = idx + 1
        resultados[motivo] = pos
    return resultados

def main():
    fasta = "ls_orchid.fasta"
    motivos = ["ATG", "GCGG"]  # Motivos a buscar
    try:
        records = list(SeqIO.parse(fasta, "fasta"))
        if not records:
            print("No se encontraron secuencias en el archivo.")
            return
    except FileNotFoundError:
        print(f"No se encontró {fasta}. Coloca el archivo en la misma carpeta.")
        return

    # Analizamos la primera secuencia como ejemplo
    primer_record = records[0]
    dna_seq = primer_record.seq
    print(f"ID secuencia: {primer_record.id}")
    print(f"Secuencia (primeros 60 nucleótidos): {dna_seq[:60]}")

    # Traducción
    proteina = traducir_secuencia(dna_seq)
    print(f"\nProteína traducida (primeros 60 aa): {proteina[:60]}")

    # Búsqueda de motivos
    resultados_motivos = buscar_motivos(dna_seq, motivos)
    print("\nMotivos encontrados (posiciones base 0):")
    for motivo, posiciones in resultados_motivos.items():
        print(f"{motivo}: {posiciones}")

    # Guardar resultados en archivo
    with open("resultados_traduccion_motivos.txt", "w") as out:
        out.write(f"ID secuencia: {primer_record.id}\n")
        out.write(f"Secuencia (primeros 60): {dna_seq[:60]}\n")
        out.write(f"Proteína traducida (primeros 60): {proteina[:60]}\n")
        out.write("Motivos encontrados (posiciones base 0):\n")
        for motivo, posiciones in resultados_motivos.items():
            out.write(f"{motivo}: {posiciones}\n")

    print("\nSe guardaron los resultados en 'resultados_traduccion_motivos.txt'")

if __name__ == "__main__":
    main()
