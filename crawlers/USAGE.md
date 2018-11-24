
# Desafio 2: Crawlers

Existem 2 modos de uso: CLI e Telegram bot.

No modo CLI, é exibido na linha de comando uma tabela com os dados extraídos dos
subreddits, além de prover um arquivo output.txt com os dados.

No modo Telegram bot, além de exibir a saída do modo CLI, as mensagens são
enviadas através do bot de Telegram.

### CLI

Para executar o modo CLI, na pasta `<repo>/desafios/crawlers/reddit`, execute:

```bash
scrapy crawl subreddit -a subreddits="<list>"
```

Essa lista deverá ser a lista de subreddits, separados por ponto-e-vírgula.

Exemplo:
```bash
scrapy crawl subreddit -a subreddits="cats;soccer;brazil"
```

### Telegram bot

Para deixar o bot de Telegram no ar, aguardando por um comando, na pasta
`<repo>/desafios/crawlers/reddit`, execute:

```bash
python3 bot.py
```

No chat com o respectivo bot do Telegram, execute o comando:

```
/NadaPraFazer <list>
```

Essa lista deverá estar no mesmo format do modo CLI.

Exemplo:
```
/NadaPraFazer cats;memes;madagascar
```
