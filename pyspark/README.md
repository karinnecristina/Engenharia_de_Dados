<p align="center">
  <img src="imagens/pyspark-filter.png" >
</p>


## PySpark (Spark com Python)

PySpark é uma biblioteca Spark escrita em Python, e seu objetivo é permitir a análise interativa dos dados em um ambiente distribuído. Seu uso é extremamente importante quando o assunto é grande volume de dados, <ins>**BigData**</ins>, por conta do seu processamento eficiente de grandes conjuntos de dados.

[Documentação](https://spark.apache.org/)

### Data

Os dados para esse tutorial foram obtidos no  [Kaggle](https://www.kaggle.com/anninasimon/employee-salary-dataset), a base é pequena, então teoricamente utilizar o pyspark nesse caso seria "matar uma mosca com um canhão", mas como objetivo é explorar as principais funções, esse dataset vai nos atender bem.

###### Para fazer download desse conjunto de dados você precisa ter uma conta no kaggle.

### Tópicos

Vamos explorar as principais funções:

* Count
* Describe
* Select
* OrderBy
* WithColumnRenamed
* WithColumn
* When
* drop
* Filter
* Where
* GroupBy

### Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv ou com o conda e o arquivo `requirements.txt` para instalar os pacotes dependências
do projeto:

**Conda**  
```bash
$ conda create --name nameenv python
$ conda activate nameenv
$ pip install -r requirements.txt
```
**Virtualenv**
```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```
### Observação
Para executar o PySpark, você também precisa que o Java seja instalado.