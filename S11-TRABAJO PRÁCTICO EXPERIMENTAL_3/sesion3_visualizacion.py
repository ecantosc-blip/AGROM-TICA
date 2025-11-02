# sesion3_visualizacion.py
# Visualizaciones: barras de longitudes y pastel de proporciones A,T,C,G para una secuencia.
# Requisitos: biopython, matplotlib (pip install biopython matplotlib)

from Bio import SeqIO
import matplotlib.pyplot as plt
import os

def plot_longitudes(fasta_path="ls_orchid.fasta", top_n=10, outfile="longitudes_bar.png"):
    ids = []
    longitudes = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        ids.append(record.id)
        longitudes.append(len(record.seq))

    if len(ids) == 0:
        print("No hay secuencias en", fasta_path)
        return

    # Tomamos las primeras top_n secuencias (o todas si hay menos)
    ids_plot = ids[:top_n]
    long_plot = longitudes[:top_n]

    plt.figure(figsize=(10,6))
    plt.bar(range(len(ids_plot)), long_plot)
    plt.xticks(range(len(ids_plot)), ids_plot, rotation=90)
    plt.ylabel("Longitud")
    plt.title("Longitud de secuencias (primeras {})".format(len(ids_plot)))
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()
    print(f"Guardado gráfico de barras: {outfile}")

def plot_composicion_pastel(sequence, outfile="composicion_pastel.png"):
    seq = sequence.upper()
    counts = [seq.count(b) for b in ("A","T","G","C")]
    labels = ["A","T","G","C"]
    if sum(counts) == 0:
        print("Secuencia vacía para el pastel.")
        return

    plt.figure(figsize=(6,6))
    plt.pie(counts, labels=labels, autopct="%1.1f%%")
    plt.title("Proporciones A/T/G/C")
    plt.savefig(outfile)
    plt.close()
    print(f"Guardado gráfico de pastel: {outfile}")

def main():
    fasta = "ls_orchid.fasta"
    if not os.path.exists(fasta):
        print(f"Archivo {fasta} no encontrado. Coloca el FASTA en la carpeta.")
        return

    # 1) gráfico de barras con primeras 10 longitudes
    plot_longitudes(fasta_path=fasta, top_n=10, outfile="longitudes_bar.png")

    # 2) tomar la primera secuencia para el pastel de proporciones
    first = None
    for record in SeqIO.parse(fasta, "fasta"):
        first = str(record.seq)
        print("Usando secuencia:", record.id)
        break

    if first:
        plot_composicion_pastel(first, outfile="composicion_pastel.png")
    else:
        print("No se encontró ninguna secuencia para graficar el pastel.")

if __name__ == "__main__":
    main()
