## Projeto de Análise de Dados com Python

Este projeto realiza a leitura de dados de um arquivo CSV, processando informações de pessoas como nome, e-mail, CEP, telefone e outros dados. O sistema valida os dados e realiza consultas externas (ex: via API do ViaCEP).

---

###  Funcionalidades

- Leitura de um arquivo `.csv` contendo dados pessoais.
- Validação e limpeza de CEPs.
- Consulta automática de endereço pelo CEP via [ViaCEP](https://viacep.com.br/).
- Geração de DDD com base no CEP.
- Formatação inteligente de números de telefone (incluindo DDD e dígito 9).
- Validação de CPF
- Buscador de gênero a partir do nome via API
- Geração de objetos JSON com os dados tratados.

---

### Estrutura do Projeto

```
analise_dados/
│
├── src/
│
│   ├── data/
│   │   └── lista_clientes.csv
│   │
│   ├── models/
│   │   ├── adress.py
│   │   ├── cpf.py
│   │   ├── people.py
│   │   └── phone.py
│   │
│   │── repo/
│   │   │── csv_repo.py
│   │   └──json_repo.py
│   │
│   │── services/
│   │   │── cpf_service.py
│   │   └── gender_service.py
│   │
│   │── tests/
│   │   │── test_cpf_service.py
│   │   │── test_gender_service.py
│   │   └── test_phone_service.py
│   │
│   │── main.py
│
└── README.md
```

---

###  Pré-requisitos

- Python 3.10+
- Biblioteca `requests` (para chamadas à API do ViaCEP e Genderize.io)

Para instalar as dependências:

```bash
pip install requests
```

###  Formato Esperado do CSV

O arquivo `.csv` deve conter as seguintes colunas (em ordem):

```
Nome completo, E-mail, Telefone com DDD, CPF, CEP, Interesse
```

Exemplo:

```
Carlos Ribeiro da Costa, carlos.ribeiro@mailinator.com, 92 934845633, 11111111111, 60862-730, Engenharia de Software
```

---

### Como Executar

No terminal, navegue até o diretório raiz do projeto e execute:

```bash
python -m src.main
```

- Substitua `src.main` pelo nome do arquivo que contém o loop `for` com leitura do CSV e geração do JSON final.

---

###  Próximas melhorias

- Tratamento de exceções.
- Testes unitários
- Organizar melhor as responsabilidades de cada módulo e utilizar módulos que não estão sendo utilizados no momento
- Gerar o arquivo Json
- Exibir as informações solicitadas no console
- Revisar a documentação
- limpar o código

