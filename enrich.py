# -*- coding: utf-8 -*-
# Enriquece bank.json com descricao por-clip. Roda no fim (depois de preencher DESC).
import json

DESC = {
# ---- remotion (prompts exatos) ----
"remotion-01":"mao de robo IA tocando uma claquete de cinema que se desfaz em particulas",
"remotion-02":"streams de codigo ambar fluindo numa tela escura (rio de codigo)",
"remotion-03":"linhas de codigo virando uma timeline de edicao de video",
"remotion-04":"explosao de particulas formando grafico de crescimento viral",
"remotion-05":"timeline de edicao com marcadores de corte e tesoura",
"remotion-06":"caneta de luz desenhando sozinha um quadro de video (video que se escreve)",
"remotion-07":"planilha de luz virando grafico de barras 3D animado",
"remotion-08":"dezenas de cards de video se multiplicando numa grade (videos personalizados em massa)",
"remotion-09":"cerebro de IA montando blocos de codigo que viram um video polido",
"remotion-10":"motor/engrenagem de luz gerando quadros de video",
"remotion-11":"guia/livro de luz aberto com passos surgindo das paginas",
"remotion-12":"mesa de criador com monitor renderizando um video abstrato",
"remotion-13":"dashboard de dados com graficos e motion graphics flutuando",
"remotion-14":"abertura de marca: formas geometricas de luz se acendendo",
"remotion-15":"faisca correndo num circuito ate um botao de play (final)",
# ---- crm ----
"crm-01":"calendario com moedas ambar escorrendo todo mes (assinatura cara/aluguel)",
"crm-02":"estrela open-source explodindo num ceu com constelacao (estrelas do GitHub)",
"crm-03":"dashboard de CRM moderno com cards de contato e funil",
"crm-04":"rack de servidor com escudo de luz (self-hosted, o dado e seu)",
"crm-05":"servidor barato rodando uma rede enorme de contatos (usuarios infinitos)",
"crm-06":"cerebro de IA remodelando os paineis de um CRM (customizacao)",
"crm-07":"blocos modulares (funil, automacao, campo) se encaixando num CRM",
"crm-08":"maos de luz instalando um servidor com chave de fenda (setup)",
"crm-09":"guia/livro de luz com passos de instalacao",
"crm-10":"balao de fala saindo de um chat (enviar/comentar)",
"crm-11":"duas colunas de luz comparando custo (uma escorrendo moedas, outra estavel)",
"crm-12":"globo de nos de contato pulsando (rede de clientes)",
"crm-13":"cadeado abrindo um cofre de dados (seu dado e seu)",
"crm-14":"faisca correndo num circuito ate um icone de CRM (final)",
# ---- assistir ----
"assistir-01":"olho de IA abrindo dentro de um botao de play (IA que assiste video)",
"assistir-02":"link/corrente de video sendo puxado pra dentro de uma esfera de IA",
"assistir-03":"cerebro de IA absorvendo quadros de video e virando linhas de texto (transcrever/aprender)",
"assistir-04":"botao de play irradiando ondas sobre uma grade de thumbnails (plataforma de video)",
"assistir-05":"film strip longo comprimindo num card de resumo (2h em 2min)",
"assistir-06":"plugue de conector encaixando numa esfera de IA (conector MCP)",
"assistir-07":"quatro tokens de dados fluindo de um site pra uma IA (setup, 4 dados)",
"assistir-08":"link conectando uma conta a uma esfera de IA (vincular conta)",
"assistir-09":"checkmark dentro de um toggle de permissao (sempre permitir)",
"assistir-10":"guia/livro com cards de passo a passo (prints)",
"assistir-11":"lupa sobre o video de um concorrente (analisar estrategia)",
"assistir-12":"sala de aula de luz, IA ensinando conceitos (aprender e ensinar)",
"assistir-13":"faisca correndo num circuito ate um botao de play (final)",
# ---- tag ----
"tag-01":"arroba @ se acendendo num chat de equipe escuro (lancamento)",
"tag-02":"robo de IA amigavel sentando entre baloes de chat (novo colega de time)",
"tag-03":"mao de luz tocando a tag @ num colega de IA num thread (delegar)",
"tag-04":"robo de IA trabalhando enquanto silhueta de pessoa sai pra outra tarefa (trabalho paralelo)",
"tag-05":"dois cenarios: resumo de reuniao e card de lead organizados por uma IA",
"tag-06":"robo de IA como colega de verdade numa mesa (nao bot escondido)",
"tag-07":"trabalhador de IA disponivel num hub de chat pulsando (sempre on)",
"tag-08":"explosao de particulas formando grafico de views (post viral)",
"tag-09":"guia/livro com passos de ativacao",
"tag-10":"painel de controle com toggles de acesso a canais/ferramentas (permissao)",
"tag-11":"rede de membros do time conectada a uma IA central no chat",
"tag-12":"faisca correndo num circuito ate a arroba @ (final)",
}

if __name__ == "__main__":
    b = json.load(open("bank.json", encoding="utf-8"))
    n = 0
    for c in b["clips"]:
        if c["id"] in DESC:
            c["desc"] = DESC[c["id"]]; n += 1
    json.dump(b, open("bank.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"descricoes precisas aplicadas: {n}/{len(b['clips'])}")
