[![author](https://img.shields.io/badge/author-KarinneCristina-red.svg)](https://www.linkedin.com/in/karinnecristinapereira/) [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/karinnecristina/Engenharia_de_Dados)

## Pipeline de Dados: Da coleta à visualização

O projeto será desenvolvido com base no conhecimento adquirido no bootcamp de engenharia de dados da [How](https://howedu.com.br/).

<br></br>

<p align="center">
  <img src="imagens/logo.jpg" >
</p>




## 📝 Etapas

- [x] Web Scraping de [Fundos imobiliários](https://www.fundsexplorer.com.br/ranking) com solicitações HTTP através da biblioteca **Requests**
- [x] Automatização da coleta com **Airflow** 
- [x] Armazenamento dos dados na nuvem - (Data Lake)  **AWS**
- [ ] Processamento de dados com **Spark**

#### Amostra dos dados:

|Data             |Códigodo fundo|Setor              |Preço Atual |Liquidez Diária  |Dividendo |DividendYield |DY (3M)Acumulado |P/VPA|DYPatrimonial|VariaçãoPatrimonial|Rentab. Patr.no Período |Rentab. Patr.Acumulada |VacânciaFísica|VacânciaFinanceira|QuantidadeAtivos
|:---             |:---          |:---               |:---        |:---             |:---      |:---          |:---             |:--- |:---         |:---               |:---                    |:---                   |:---          |:---              |:---
|28/12/2021 20:32 |VINO11        |Lajes Corporativas |R$ 56,82    |39070.0          |R$ 0,55   |0,99%         |2,95%            |98.0 |0,95%        |-0,43%             |0,52%                   |4,04%                  |7,90%         |NaN               |9
|28/12/2021 20:32 |HGCR11        |Títulos e Val. Mob.|R$ 105,95   |16411.0          |R$ 0,95   |0,93%         |2,57%            |104.0|0,93%        |0,95%              |1,88%                   |5,68%                  |NaN           |NaN               |0
|28/12/2021 20:32 |MXRF11        |Híbrido            |R$ 9,93     |465266.0         |R$ 0,08   |0,80%         |2,49%            |98.0 |0,79%        |0,72%              |1,52%                   |8,90%                  |NaN           |NaN               |0
|28/12/2021 20:32 |XPLG11        |Logística          |R$ 97,04    |37276.0          |R$ 0,64   |0,70%         |1,96%            |92.0 |0,60%        |-3,33%             |-2,74%                  |2,40%                  |9,80%         |1,20%             |13
|28/12/2021 20:32 |HGRU11        |Híbrido            |R$ 115,21   |34826.0          |R$ 0,72   |0,67%         |1,95%            |97.0 |0,61%        |0,84%              |1,45%                   |7,21%                  |0,00%         |0,00%             |16

---

## ⚙️ Passo a passo para reproduzir o projeto
#### Instalação do docker:
[Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) -
[Windows](https://docs.docker.com/desktop/windows/install/)
#### Instalação do poetry (windows / linux):
[poetry](https://python-poetry.org/docs/)

#### Configurando o ambiente:
```bash
# Cria a pasta do projeto no terminal/cmd
$ mkdir Projeto
```
```bash
# Acesse a pasta do projeto no terminal/cmd
$ cd Projeto
```
```bash
# Faça download dos arquivos no link
https://github.com/karinnecristina/Engenharia_de_Dados/tree/main/Projeto
```

```bash
# Ative o ambiente virtual
$ poetry env use python3
```
```bash
# Instale as dependências
$ poetry install
```
#### Rodando a aplicação:

```bash
# Na pasta do projeto inicie o airflow
$ docker-compose up airflow-init
```
```bash
# Execute a aplicação
$ docker-compose up
```