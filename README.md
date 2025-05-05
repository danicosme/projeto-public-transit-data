# 🚍 Projeto Public Transit Data

Projeto de engenharia de dados para coleta, transformação e armazenamento de dados públicos de transporte, com foco em AWS, DuckDB e Terraform.

---

## 📁 Estrutura de Pastas

```
projeto-public-transit-data/
├── infra/                    # Terraform
│   ├── main.tf
│   ├── variables.tf
│   └── modules/
│       └── s3_bucket/
│           ├── main.tf
│           └── variables.tf
├── src/                      
│   ├── ingestion/            # Etapa de ingestão na camada RAW
│   └── transformation/       # Etapa de transformação e ingestão na camada PROCESSED
├── .gitignore
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- **Python** – Scripts de ingestão e transformação de dados
- **DuckDB** – Consultas SQL e transformação
- **AWS S3** – Armazenamento de dados em camadas (`raw/`, `processed/`)
- **Terraform** – Infraestrutura como código
- **Boto3** – Cliente Python para interação com serviços da AWS

---

## 🔧 Como Executar

1. **Clone o projeto**

```bash
git clone https://github.com/danicosme/projeto-public-transit-data.git
cd projeto-public-transit-data
```

2. **Configure suas credenciais AWS**

As credenciais devem estar em (`~/.aws/credentials`) para que o Terraform e o Boto3 funcionem corretamente.

3. **Provisionar infraestrutura com Terraform (⚠️Em construção)**

```bash
cd infra
terraform init
terraform apply
```

4. **Executa local**

Acesse a pasta `src/ingestion/` ou `src/processing/` e execute o script main.

---

## 💻 Funcionalidades

- Baixa e descompacta arquivos `.zip` da SPTrans
- Lê arquivos `.txt` e transforma usando SQL com DuckDB
- Salva dados em formato `.parquet` no S3 particionado por data

---

## ✅ Próximos Passos

- [ ] Continuar a criação dos recursos utilizando Terraform: funções Lambda, tabelas no Athena, integrações com SNS/SQS etc.
- [ ] Adicionar testes unitários.