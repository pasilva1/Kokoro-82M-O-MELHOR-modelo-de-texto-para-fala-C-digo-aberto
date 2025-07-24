import numpy as np
import soundfile as sf
from kokoro import KPipeline

# 🇺🇸 'a' => American English, 🇬🇧 'b' => British English
# 🇪🇸 'e' => Spanish es
# 🇫🇷 'f' => French fr-fr
# 🇮🇳 'h' => Hindi hi
# 🇮🇹 'i' => Italian it
# 🇯🇵 'j' => Japanese: pip install misaki[ja]
# 🇧🇷 'p' => Brazilian Portuguese pt-br
# 🇨🇳 'z' => Mandarin Chinese: pip install misaki[zh]
lang_code = "p"

pipeline = KPipeline(lang_code=lang_code)
text = """

Confira nossa news
Se você quer mais controle, clareza e decisões baseadas em dados reais
(não só feeling), essa edição da nossa newsletter foi feita pra você.
De crédito consignado à reforma tributária, passando por vendas e projeções
financeiras, o que não falta é assunto importante e prático.
Confira os temas mais acessados e que vão fazer diferença na sua gestão:
GESTÃO DE PESSOAS
Crédito consignado: como preparar seu RH
Com o novo e-Consignado, o RH assume um papel fundamental na validação
digital dos empréstimos com desconto em folha. De agora em diante, não
é só repassar informação, é garantir segurança jurídica em cada etapa.
De acordo com dados da Salaryfits, empresa do grupo Serasa Experian,
aproximadamente 40% dos colaboradores nas organizações possuem algum
tipo de empréstimo consignado ativo.

"""

# Você pode conferir outras vozes aqui:
# http://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
voice = "af_heart"
generator = pipeline(text, voice="pf_dora")

audio_chunks = []
for i, (gs, ps, audio) in enumerate(generator):
    print(i, gs, ps)
    audio_chunks.append(audio)

if audio_chunks:
    audio_completo = np.concatenate(audio_chunks)
    sf.write("audio_completo.wav", audio_completo, 24000)
    print(f"Arquivo salvo: audio_completo.wav")
