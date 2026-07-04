# Padrões do perfil @ericluciano

Última análise: 2026-07-04
Fontes: 5 hits coletados manualmente (Apify, com vídeo baixado e transcrição Whisper) + 3 posts recentes de baixa performance (flops) do research_data.json de 2026-07-04. Views = videoPlayCount.

| Shortcode | Data | Views | Comentários | Tema | Palavra CTA |
|---|---|---|---|---|---|
| DYxZ4sAxuTL | 2026-05-25 | 168.060 | 63 | Context rot: por que o Claude fica lento e caro em conversa longa + 3 hacks (/clear com resumo, /re, /btw) | nenhuma (CTA foi "salva e me segue") |
| DZDkqD1x68E | 2026-06-01 | 41.534 | 744 | Alucinação: prompt de 6 regras nas instruções personalizadas pro Claude parar de inventar | nenhuma no vídeo ("comenta se já caiu nessa"); prompt inteiro no caption |
| DZYbrMvRQYM | 2026-06-09 | 59.759 | 5.129 | Conselho de LLMs (skill do Olly Lemon sobre o conselho do Karpathy): mata a bajulação em decisão cara | conselho |
| DZYTRiexKPt | 2026-06-09 | 538.083 | 36.782 | MarkItDown da Microsoft: converter PDF em Markdown corta até 70% dos tokens | markdown |
| DZaDN7YO_zN | 2026-06-10 | 57.467 | 1.917 | 3 comandos do Claude Code que passaram batido (/ultraplan, /powerup, /insights) | comandos |

Engajamento por view (likes + comentários / views):
- DYxZ4sAxuTL: 3,65% (comentários por view: 0,04%)
- DZDkqD1x68E: 3,89% (comentários por view: 1,79%)
- DZaDN7YO_zN: 7,01% (comentários por view: 3,34%)
- DZYTRiexKPt: 10,71% (comentários por view: 6,84%)
- DZYbrMvRQYM: 12,39% (comentários por view: 8,58%)

## Hooks que funcionaram

Texto literal falado (transcrição Whisper), primeiras 1-2 frases de cada hit:

- DYxZ4sAxuTL: "Você já notou que o Claude começa inteligente e depois de meia hora de conversa vai ficando lento, confuso e estourando o limite? Tem um motivo. E quase ninguém te conta."
- DZDkqD1x68E: "O Claude mente pra você com confiança, todo dia. Ele não avisa quando não sabe, inventa dados, cria fontes que não existem e afirma coisas com certeza total."
- DZYbrMvRQYM: "Você pergunta pro Claude se a sua ideia é boa, ele monta um argumento lindo provando que é genial. Aí você pergunta se a mesma ideia é uma furada, ele prova que é péssima com a mesma firmeza."
- DZYTRiexKPt: "Se você joga PDF dentro do Claude, você tá queimando token à toa. E a Microsoft resolveu isso de graça faz tempo. Só que quase ninguém sabe."
- DZaDN7YO_zN: "Enquanto todo mundo fala do modelo novo da Anthropic, o Claude Code ganhou 3 comandos que passaram batido. E um deles analisa seus últimos 30 dias de uso e te mostra exatamente onde você está perdendo tempo."

O padrão: toda abertura acusa em segunda pessoa um dano que o espectador já está sofrendo AGORA com o Claude (fica lento, mente, bajula, queima token) e emenda um gancho de segredo ("quase ninguém te conta", "quase ninguém sabe", "passaram batido"). Nenhum hit abre com notícia, promessa de produtividade ou pergunta abstrata.

## Temas campeões vs temas fracos

Campeões (hits, 41K a 538K views):
- Dor operacional universal de quem usa Claude no dia a dia: custo/limite de token (538K), alucinação (41K), bajulação em decisão (59K), lentidão em conversa longa (168K), recursos escondidos (57K).
- Todos entregam solução com artefato de autoridade externa: ferramenta da Microsoft, comandos oficiais da Anthropic, conselho do Karpathy, prompt pronto pra colar.
- Todos têm número chocante no diagnóstico: 98,5% dos tokens relendo histórico, precisão caindo de 92% pra 78%, 2 a 3 mil tokens por página de PDF, corte de 70%, 140 mil estrelas no GitHub.

Fracos (flops recentes, 844 a 2.328 views):
- DZgVzp9R-Lr (2.328 views): "AI slop" no design de sites feitos com IA. Dor de nicho (designer/marca), não do usuário comum de Claude.
- DZdaK24Rymw (844 views): CLAUDE.md como memória. Hook abstrato de matemática de tempo ("você perde 10 minutos por dia"), promessa de produtividade futura em vez de dano presente.
- DZ-8_FZx548 (1.350 views): Remotion, "o Claude matou os editores de vídeo". Abre desmentindo uma manchete ("calma, isso é meio exagero"), formato notícia + caso de uso de nicho (vídeo em escala).

A diferença não está no CTA (os flops usam a mesma fórmula de palavra-chave) e sim no par hook + tema: hit fala do prejuízo imediato e universal do espectador com a ferramenta; flop fala de novidade de ferramenta pra um nicho ou de ganho abstrato.

## CTA e conversão em comentário

Campeão de taxa: DZYbrMvRQYM, 5.129 comentários em 59.759 views (8,58% por view). O que ele fez de diferente:
- A palavra é o nome da própria solução e um substantivo comum da vida real: "comenta conselho". Zero esforço cognitivo, e a palavra já foi repetida várias vezes no vídeo (a skill se chama Conselho).
- A entrega prometida é específica: "o guia pra instalar hoje", e o caption remove o atrito na hora: "(sem terminal, sem código)". Quem não é dev perde o medo de pedir.
- Condicional de desejo em vez de ordem: "Se você quiser o guia pra instalar hoje, comenta conselho".

Segundo lugar (DZYTRiexKPt, 6,84%) segue a mesma fórmula: palavra simples do tema (markdown) + passo a passo prometido no direct + "o setup leva uns dois minutos" desarmando o atrito.

Contra-exemplo dentro dos próprios hits: DYxZ4sAxuTL fez o maior alcance (168K) com CTA de "salva e me segue", mas gerou só 63 comentários (0,04%). Sem palavra-chave não há conversa no direct nem lead.

## Duração

Faixa dos hits: 44 a 79 segundos (ffprobe: 44,5s / 51,8s / 58,7s / 65,9s / 79,4s). Os dois campeões de comentário por view ficaram em 51,8s e 65,9s. Mira: 50 a 66 segundos.

## 3 regras acionáveis pro próximo roteiro

1. Abra acusando em segunda pessoa um prejuízo que o espectador já sente hoje usando o Claude (token queimado, resposta inventada, bajulação, lentidão) e feche a primeira ou segunda frase com o gancho de segredo no padrão "quase ninguém sabe" / "quase ninguém te conta". Proibido abrir com notícia, desmentido de manchete, teste hipotético ou conta abstrata de minutos economizados: foi exatamente assim que os 3 flops abriram.

2. Nos primeiros 20 segundos, entregue o diagnóstico com pelo menos um número específico e chocante (nos hits: 98,5% dos tokens relendo histórico, 2 a 3 mil tokens por página, corte de 70%, 140 mil estrelas no GitHub) e batize o problema ou a solução com um nome próprio memorável (context rot, alucinação, Conselho, MarkItDown), de preferência apoiado em autoridade externa (Microsoft, Anthropic, Karpathy).

3. Feche SEMPRE com CTA de palavra-chave única, que seja um substantivo simples já repetido no vídeo e ligado ao tema (markdown, conselho, comandos; nunca jargão novo tipo SLOP ou nome de marca desconhecida tipo REMOTION), prometendo uma entrega concreta no direct (guia, passo a passo) e removendo o atrito na mesma frase ("sem terminal, sem código", "o setup leva 2 minutos"). Nunca troque a palavra-chave por "salva e me segue": isso rendeu 63 comentários em 168 mil views. Duração alvo do vídeo: 50 a 66 segundos.
