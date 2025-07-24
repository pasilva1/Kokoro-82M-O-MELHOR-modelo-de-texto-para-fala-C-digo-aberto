import soundfile as sf
from IPython.display import Audio, display

from kokoro import KPipeline

pipeline = KPipeline(lang_code="p")
text = """
Explicando cada biblioteca que se precisa instalar: kokoro, uma
biblioteca do modelo de voz que estamos usando , sítense ou pipeline
de TTS, soundfile, para leitura e escrita de arquivos de audio, torch:
Pythorch, necessario para rodar a maior parte dos modelos de ML como kokoro.
"""
generator = pipeline(text, voice="af_heart")
for i, (gs, ps, audio) in enumerate(generator):
    print(i, gs, ps)
    display(Audio(data=audio, rate=24000, autoplay=i == 0))
    sf.write(f"{i}.wav", audio, 24000)
