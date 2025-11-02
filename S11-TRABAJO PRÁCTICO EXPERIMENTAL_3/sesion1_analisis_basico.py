# sesion1_analisis_basico.py
# Análisis básico de una secuencia (lectura manual + funciones simples)
# Requisitos: Python 3.x

def longitud(secuencia: str) -> int:
    """Devuelve la longitud total de la secuencia."""
    return len(secuencia)

def contar_bases(secuencia: str) -> dict:
    """Cuenta cuántas veces aparece cada base (A, T, C, G)."""
    seq = secuencia.upper()
    return {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'C': seq.count('C'),
        'G': seq.count('G'),
        'otros': sum(1 for ch in seq if ch not in 'ATCG')
    }

def porcentaje_gc(secuencia: str) -> float:
    """Calcula el porcentaje de G + C en la secuencia."""
    counts = contar_bases(secuencia)
    g_plus_c = counts['G'] + counts['C']
    total = len(secuencia)
    return (g_plus_c / total) * 100 if total > 0 else 0.0

def main():
    print("=== ANÁLISIS (SECUENCIA MANUAL) ===")
    # Copiar manualmente una secuencia desde el archivo fasta
    secuencia = "ATGCGTACGTAGCTAGCTAGCTA"  # <- reemplaza con la que elijas
    print("Secuencia (primeros 60 chars):", secuencia[:60])
    print("Longitud:", longitud(secuencia))
    counts = contar_bases(secuencia)
    print("Conteo bases:", counts)
    print(f"% GC: {porcentaje_gc(secuencia):.2f}%\n")

    print("=== LECTURA DEL ARCHIVO ls_orchid.fasta (primeros 500 caracteres) ===")
    try:
        with open("ls_orchid.fasta.txt", "r") as f:
            contenido = f.read()
            print(contenido[:500])
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'ls_orchid.fasta.txt'. Asegúrate de que esté en la misma carpeta.")

if __name__ == "__main__":
    main()
