# PLab-Site

Download de Arquivos:
```
wget https://github.com/plab-puc/PLab-Site/archive/master.zip
unzip master.zip
rm master.zip
cd PLab-Site-master
wget -O server.zip http://bit.ly/1E7nJyE
unzip server.zip
rm server.zip
```


Configurações
```
cd Pygmy*
gedit config.conf    (ou outro editor)
Alterar linha: "port = 8080" para "port = 8000" (SEM ASPAS)
Alterar linha: "wwwFolder = ../PLab-Site/www/" para "wwwFolder = ../www/" (SEM ASPAS)
Alterar linha: "allowedDirsAndSubdirs = ['../PLab-Site/www/']" para "allowedDirsAndSubdirs = ['../www/']" (SEM ASPAS DUPLAS, APENAS SIMPLES INTERNA)
Salve e retorne ao shell
```

Executar
```
python server.py -v 
```

Teste
```
Abra o navegador
Acesse: http://127.0.0.1:8000
```
