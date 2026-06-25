# 🎞️ expert-broll-bank

Banco público de **B-rolls reutilizáveis** da série de Reels da Expert — dark + âmbar, abstrato high-tech,
**9:16, ~5s, sem áudio**. A skill [`criar-reel-v3`](https://github.com/joaoludgerio/criar-reel-v3) consulta este
catálogo e baixa só os clips que fazem sentido, **em vez de gerar tudo no Kling** toda vez.

## Estrutura
- **`bank.json`** — catálogo: cada clip com `id`, `cat[]` (categoria), `desc`, `res`, `hd`, `thumb`, `url`.
- **`thumbs/`** — 1 miniatura por clip (pra escolha fina).
- **`sheets/`** — grades visuais (`ALL-1/2/3.jpg` e `_<tema>.jpg`) pra navegar.
- **`gallery.html`** — galeria clicável (abrir local).
- **Os vídeos (.mp4)** ficam no **[Release](../../releases)** (não no git) → URLs públicas diretas.

## Como a skill usa
```bash
python broll_bank.py --list                    # lista o catálogo
python broll_bank.py --list --cat servidor     # filtra por categoria
python broll_bank.py --thumb crm-03 tag-08      # baixa thumbs pra conferir
python broll_bank.py --get crm-03 tag-08 --out <reel>   # baixa como clip-01,02.mp4
```
URL do catálogo: `https://raw.githubusercontent.com/joaoludgerio/expert-broll-bank/main/bank.json`

## Categorias
robo · servidor · cerebro · video · documento · energia · rede · relogio · estrela · lupa · moeda · cristal · pessoas

## Crescer o banco
Clips novos gerados num reel → subir no Release (`gh release upload v1 novos/*.mp4`) e acrescentar as
entradas no `bank.json` (mesmo formato). Atualizar `thumbs/` e `sheets/` se quiser.
