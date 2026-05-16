import numpy as np
import sounddevice as sd

def criar_nota(freq, duracao, volume=0.3):
    """Gera uma nota senoidal com um envelope ADSR simples para soar menos agressiva."""
    fs = 44100
    t = np.linspace(0, duracao, int(fs * duracao))
    
    # Onda principal (senoidal)
    onda = volume * np.sin(2 * np.pi * freq * t)
    
    # Envelope para evitar estalos (Fade in e Fade out)
    envelope = np.ones_like(t)
    fade_in = int(fs * 0.05)
    fade_out = int(fs * 0.1)
    envelope[:fade_in] = np.linspace(0, 1, fade_in)
    envelope[-fade_out:] = np.linspace(1, 0, fade_out)
    
    return onda * envelope

def tocar_devil_in_a_new_dress():
    fs = 44100
    
    # Frequências aproximadas das notas (Melodia principal)
    # Db4, Eb4, F4, Gb4, Ab4, Bb4, C5
    notas = {
        'Db4': 277.18,
        'Eb4': 311.13,
        'F4': 349.23,
        'Gb4': 369.99,
        'Ab4': 415.30,
        'Bb4': 466.16,
        'C5': 523.25,
        'Db5': 554.37,
        'pausa': 0
    }

    # Sequência da melodia (simplificada)
    # "I love it though..."
    melodia = [
        ('Ab4', 0.4), ('F4', 0.4), ('Gb4', 0.4), ('F4', 0.4),
        ('Eb4', 0.6), ('pausa', 0.1),
        ('Db4', 0.4), ('Eb4', 0.4), ('F4', 0.6),
        ('pausa', 0.2),
        ('Ab4', 0.4), ('Bb4', 0.4), ('Ab4', 0.6)
    ]

    musica_final = []

    for nota, tempo in melodia:
        if nota == 'pausa':
            musica_final.append(np.zeros(int(fs * tempo)))
        else:
            som_nota = criar_nota(notas[nota], tempo)
            musica_final.append(som_nota)

    som_completo = np.concatenate(musica_final)
    
    print("Reproduzindo: Devil In a New Dress (Melody Intro)...")
    sd.play(som_completo, fs)
    sd.wait()

# Executar
if __name__ == "__main__":
    tocar_devil_in_a_new_dress()