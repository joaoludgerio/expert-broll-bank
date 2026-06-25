# 🎞️ Banco de B-rolls — Expert (reutilizável)

**219 clips** de B-roll já gerados (Kling), reunidos pra **reciclar em vez de gerar do zero** toda vez.
Todos no mesmo estilo: **fundo escuro carvão + brilho âmbar/coral, abstrato high-tech, 9:16, ~5s, sem áudio.**
Visual coeso = dá pra alternar entre eles sem quebrar a identidade da série.

- `clips/` — os 219 vídeos, nomeados `<tema-origem>-NN.mp4` (ex: `crm-03.mp4`).
- `thumbs/` — 1 thumbnail por clip.
- `sheets/` — grades visuais: `_<tema>.jpg` (por reel de origem) e `ALL-1/2/3.jpg` (tudo). **Abra essas pra escolher.**
- `_manifest.tsv` — lista máquina (arquivo, origem, nº, resolução, duração).

**Resolução:** 74 clips em **1080×1920** (nítidos) + 145 em menor (768×1152, 720×1280, 704×1248). O
`compose_reel.py` força escala pra 1080×1920, então **todos servem** — os de 1080 ficam mais nítidos; os
menores, como ficam de fundo atrás do Eric, passam bem. Preferir os de 1080 quando o B-roll aparecer "limpo".

---

## 🔎 Categorias (pra casar com a fala) 

Use isto pra mapear o trecho do roteiro → tipo de B-roll → clip do banco. Nomes são exemplos; confira no
`sheets/ALL-*.jpg` pra escolher o melhor de cada categoria.

| Categoria | Quando usar (tema da fala) | Exemplos no banco |
|---|---|---|
| 🤖 **Robô / figura de IA** | "uma IA", "agente", "funcionário de IA", "assistente" | `claude-smb-04..07,10,11`, `goal-02`, `persona-03,07`, `tag-02,06`, `reuniao-*` |
| 🖥️ **Servidor / data center / rack** | "self-hosted", "servidor", "infraestrutura", "rodar local" | `claude-smb-08,09`, `crm-03,04,05` |
| 🧠 **Cérebro / conhecimento / grafo** | "segundo cérebro", "memória", "aprende", "conhecimento" | `segundo-cerebro-01,02,03,08,09`, `fantasma-01,02`, `revisor-*` |
| ▶️ **Vídeo / play / film strip** | "vídeo", "assistir", "YouTube", "Reels", "renderizar" | `assistir-01,03,04,05`, `remotion-01,06` |
| 📄 **Documento / tela / dashboard / card** | "documento", "contrato", "planilha", "CRM", "relatório" | `ai-slop-01,02,08`, `crm-03`, `revisor-01..06`, `privado-*` |
| ⚡ **Energia / partículas / código / streaks** | transição, "viralizou", "explodiu", "código", abertura | `desvio-fable-01..13`, `radar-08..11`, `remotion-02,03` |
| 🕸️ **Rede / nós / conexões** | "conecta", "integra", "time", "rede", "MCP" | `tag-10,11`, `segundo-cerebro-04,05` |
| ⏱️ **Relógio / tempo / ampulheta** | "5 minutos", "tempo", "rápido", "todo dia", "atraso" | `5-minutos-01,02,03`, `revisor-09` (ampulheta) |
| ⭐ **Estrela / burst / explosão** | "viralizou", "estrelas no GitHub", "milhões de views" | `crm-02`, `tag-08`, `5-minutos-08` |
| 🔍 **Lupa / busca / radar** | "pesquisa", "análise", "espionar", "monitorar", "vaza" | `privado-04`, `radar-01,02`, `assistir-11` |
| 💰 **Moeda / custo / dinheiro** | "custo", "mensalidade", "preço", "economia", "aluguel" | `quanto-custa-a-hora-01..07`, `crm-01` |
| 🔮 **Cristal / esfera âmbar** | "uma IA" abstrata, "poder", destaque genérico | `ai-slop-09`, `fantasma-01,02` |
| 👥 **Pessoas + IA / equipe** | "equipe", "time", "no Slack", "colaboração" | `tag-04,05,07`, `reuniao-*` |

---

## ♻️ Fluxo de reuso (regra nova da pipeline)

Antes de gerar QUALQUER clip novo no Kling:
1. Abrir o roteiro/cenas e listar os ~N trechos que precisam de B-roll.
2. Pra cada trecho, achar a **categoria** acima → escolher 1 clip do banco (olhando os `sheets/`).
3. **Alternar** entre clips diferentes (não repetir o mesmo seguido) e priorizar os 1080×1920.
4. **Só gerar no Kling o que NÃO existe** no banco (visual muito específico que o banco não cobre).
5. Copiar os clips escolhidos pra `<reel-novo>/` como `clip-01.mp4 ... clip-NN.mp4` na ordem da fala,
   e gerar só os faltantes. Depois `compose_reel.py` normal.

Isso derruba o custo do Kling a quase zero na maioria dos reels (o banco já cobre os temas comuns de IA/negócio).
Sempre que gerar clips novos, eles entram no banco depois (rodar de novo a montagem do banco ou copiar à mão).
