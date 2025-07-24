from kokoro import KPipeline
import pyaudio
import numpy as np
import soundfile as sf
import io

pipeline = KPipeline(lang_code='p')
pyaudio_instance = pyaudio.PyAudio()

def stream_kokoro_local():
    stream = pyaudio_instance.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=24000,
        output=True
    )
    
    print("Iniciando streaming do Kokoro local...")
    
    texto = """
    Confira nossa news
    Se você quer mais controle, clareza e decisões baseadas em dados reais (não só feeling), essa edição da nossa newsletter foi feita pra você.

    De crédito consignado à reforma tributária, passando por vendas e projeções financeiras, o que não falta é assunto importante e prático.

    Confira os temas mais acessados e que vão fazer diferença na sua gestão:
    GESTÃO DE PESSOAS
    Crédito consignado: como preparar seu RH 
    Com o novo e-Consignado, o RH assume um papel fundamental na validação digital dos empréstimos com desconto em folha. De agora em diante, não é só repassar informação, é garantir segurança jurídica em cada etapa.
    De acordo com dados da Salaryfits, empresa do grupo Serasa Experian, aproximadamente 40% dos colaboradores nas organizações possuem algum tipo de empréstimo consignado ativo.

    """
    #generator = pipeline(texto, voice='pm_santa')
    generator = pipeline(texto, voice='pf_dora')
    
    audio_chunks = []
    for gs, ps, audio in generator:
        audio_chunks.append(audio)
    
    if audio_chunks:
        audio_completo = np.concatenate(audio_chunks)
        print(f"Reproduzindo áudio: {len(audio_completo)} samples")
        stream.write(audio_completo.tobytes())
    
    stream.stop_stream()
    stream.close()
    pyaudio_instance.terminate()
    print("Streaming concluído!")

if __name__ == "__main__":
    stream_kokoro_local() 