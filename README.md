# Paper E: Dohad | Apriori


## 📌 Overview


> This implementation uses Kmeans and PCA to cluster data into possible risk groups. Association rules are then created based on each group using Apriori. This methodology allows for extraction of valuable information about characteristics that may lead to worse prenatal outcomes.


**"Características maternas e aspectos das assistências pré-natal e parto associados aos desfechos neonatais desfavoráveis em mulheres negras brasileiras: uma abordagem baseada em regras de associação com o algoritmo Apriori"**


Authors: Alves, Yasmin C. S. et al.
Accepted at: [Dohad](https://www.dohad2025.com.ar/) 2025, waiting presentation date and publication.


## 🚀 Setup


To ensure reproduction of results, requirements are listed on [pyproject](pyproject.toml) file. [Poetry](https://python-poetry.org/) can be used to download requirements listed and run [main.py](main.py) with the following commands respectively:


```bash
poetry install
```


```bash
poetry run python main.py
```


## 🔮 Methodology

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark_Dohad.png">
  <source media="(prefers-color-scheme: light)" srcset="light_Dohad.png">
  <img alt="Methodology image" src="light_Dohad.png">
</picture>


## ✨ Dataset

The dataset used corresponds to year 2023. It was initially download from [OpenDataSUS](https://opendatasus.saude.gov.br/) throught an [ETL pipeline](https://github.com/GOPAD-Datasus/ETL-SINASC). 

## 📝 License
[LGNU](LICENSE) | © GOPAD 2025
