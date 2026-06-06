"""
MÓDULO DE UTILITÁRIOS GEOMÉTRICOS v1.0
Desenvolvido para auxiliar em projetos de modelagem 3D industrial.
"""

def volume_cubo(lado: float) -> float:
    """Calcula o volume total de um cubo (Lado ao cubo)."""
    res = lado ** 3
    return res

# Teste local protegido
if __name__ == "__main__":
    v = volume_cubo(5.0)
    print(f"Teste local -> Volume para lado 5: {v}")