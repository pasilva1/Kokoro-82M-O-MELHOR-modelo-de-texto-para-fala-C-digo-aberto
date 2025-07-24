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

Judas Iscariotes é um dos personagens mais controversos do Novo Testamento.
Ele foi um dos doze apóstolos escolhidos por Jesus Cristo.
O seu nome tornou-se sinônimo de traição e deslealdade.
Nas listas de discípulos nos Evangelhos, Judas aparece sempre por último.
Os evangelistas sempre fazem referência a ele como o traidor.
Pouco se sabe sobre sua origem, mas acredita-se que era de Queriote, na Judeia.
O sobrenome Iscariotes pode significar “homem de Queriote”.
Alguns estudiosos sugerem que Iscariotes também poderia ter outro significado.
As narrativas bíblicas mostram Judas como tesoureiro do grupo.
Ele era responsável pela bolsa de dinheiro usada pelos discípulos.
O Evangelho de João insinua que Judas era desonesto com os recursos.
Há uma passagem em que ele critica Maria por ungir Jesus com perfume caro.
João explica que Judas não estava preocupado com os pobres.
Segundo João, ele dizia isso porque era ladrão e roubava da bolsa.
Apesar disso, Jesus o manteve próximo e não o expulsou do grupo.
A relação entre Judas e Jesus é cercada de mistério.
Nos Evangelhos Sinópticos, Judas vai às autoridades judaicas.
Ele negocia a entrega de Jesus por trinta moedas de prata.
Esse valor tem simbologia no Antigo Testamento, em Zacarias.
A soma era o preço de um escravo ferido.
Os evangelistas parecem mostrar Judas como motivado por ganância.
Outras tradições apontam motivações políticas ou desilusões pessoais.
Alguns teólogos sugerem que Judas esperava um Messias guerreiro.
Ao ver Jesus pregando paz, teria se frustrado.
Essa hipótese tenta explicar seu ato sem reduzi-lo a pura ganância.
Mas a narrativa bíblica é clara sobre a traição.
Na Última Ceia, Jesus anuncia que um dos doze o trairá.
Os discípulos ficam aflitos e perguntam quem seria.
Jesus identifica Judas de forma sutil, oferecendo-lhe um pedaço de pão.
O ato simboliza hospitalidade, mas também entrega.
Judas sai da ceia para cumprir seu intento.
Os evangelhos dizem que Satanás entrou nele naquele momento.
Na noite do Getsêmani, Judas guia os soldados até Jesus.
Ele usa um beijo como sinal de identificação.
Esse beijo tornou-se símbolo de falsidade e traição.
Jesus pergunta: “Com um beijo trais o Filho do Homem?”.
A prisão de Jesus se segue imediatamente.
Judas, ao ver o desfecho, sente remorso.
Mateus relata que ele devolve as moedas aos sacerdotes.
Os sacerdotes recusam e Judas joga o dinheiro no templo.
Ele então se retira e se enforca.
O livro de Atos descreve a morte de Judas de forma diferente.
Segundo Atos, ele adquire um campo com o dinheiro.
E caindo de cabeça, rompe-se pelo meio.
Essas diferenças geram debates sobre a historicidade dos relatos.
Teólogos interpretam Judas de várias formas.
Alguns o veem como instrumento necessário ao plano divino.
Outros o consideram exemplo de livre-arbítrio mal exercido.
Na tradição cristã, Judas encarna a advertência contra a cobiça.
Seus atos são lembrados nas celebrações da Semana Santa.
Na liturgia, seu nome é citado como aviso.
A literatura também explora seu personagem.
Dante Alighieri o coloca no Inferno em A Divina Comédia.
Na última esfera, ele é devorado por Lúcifer.
Essa imagem consolidou Judas como o maior dos traidores.
No entanto, há correntes que buscam reinterpretá-lo.
O Evangelho de Judas, um texto gnóstico, traz outra visão.
Nele, Judas seria o discípulo mais próximo de Jesus.
Jesus lhe confia segredos e pede que o entregue.
Essa narrativa sugere Judas como obediente a um plano.
Esse evangelho apócrifo gerou polêmica entre estudiosos.
Alguns veem aí uma tentativa de reabilitar sua imagem.
Historicamente, Judas foi usado como figura negativa.
Infelizmente, a figura de Judas foi usada para alimentar o antissemitismo.
Muitos sermões antigos associaram seu ato ao povo judeu.
A Igreja moderna rejeita essas interpretações preconceituosas.
Judas deve ser visto como indivíduo e não como símbolo de um povo.
O estudo sobre Judas ensina sobre escolhas e consequências.
Ele tinha acesso ao próprio Cristo e mesmo assim se desviou.
A história mostra que a proximidade com o sagrado não garante fidelidade.
Cada um é responsável por suas decisões.
O ato de Judas não foi escondido nos Evangelhos.
Isso mostra a transparência das primeiras comunidades cristãs.
Elas não esconderam as falhas internas.
O nome de Judas virou sinônimo de traidor em várias línguas.
Na cultura popular, “beijo de Judas” significa falsa amizade.
Teatros e filmes retratam Judas como vilão.
Outros como vítima das circunstâncias.
Seu legado é ambíguo e instigante.
A traição de Judas foi um ponto de virada na narrativa da paixão.
Sem Judas, não haveria prisão, julgamento e crucificação.
Alguns enxergam isso como parte do plano divino.
Outros como um acidente histórico.
Teólogos continuam debatendo seu papel até hoje.
Psicólogos veem em Judas alguém dividido entre fé e frustração.
Artistas exploram seu drama interno em pinturas e músicas.
Em peças teatrais, Judas às vezes aparece arrependido.
Noutras, como conspirador frio.
Essa multiplicidade mostra a profundidade do personagem.
Estudar Judas é estudar as fragilidades humanas.
É refletir sobre lealdade e tentação.
Sobre dinheiro e espiritualidade.
Sobre coragem e covardia.
A figura de Judas transcende o texto bíblico.
Ela inspira debates filosóficos.
Gera meditações espirituais.
E permanece viva na memória coletiva.
Ao longo de dois milênios, seu nome continua a provocar discussões.
Sua história não é apenas sobre um homem.
É sobre as escolhas que moldam destinos.
É sobre como pequenas decisões têm grandes consequências.
Judas nos lembra que o coração humano é complexo.
Ele nos alerta sobre a importância da vigilância moral.
E nos convida a refletir sobre misericórdia e justiça.
No final, Judas permanece um enigma.
Um enigma que continua a desafiar a compreensão de teólogos, historiadores e artistas.
E assim, sua história segue sendo contada e reinterpretada ao longo do tempo.

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
