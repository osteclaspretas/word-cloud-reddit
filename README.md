# word-cloud-reddit

Usa praw e world_cloud https://github.com/amueller/word_cloud

Passos:

1) Configurar uma API no reddit
2) Colocar os dados dessa api num config.ini. Usar o config.ini.tmpl de template
3) Isso feito, chamar o comando da seguinte forma:

python load.py username

onde username é o usuario que você quer trazer os dados

o load.py tras apenas os comentarios do usuario num txt, que fica salvo dentro da pasta data

para gerar o cloud:

wordcloud_cli.py --text data/username --stopwords stopwords-pt.txt --width 800 --height 600  --no_collocations >png/username.png
