# Aplicação Python com Clean Architecture

## Contexto

Este projeto é um exemplo de aplicação utilizando os princípios da **Clean Architecture** em Python. O objetivo é separar as responsabilidades em camadas bem definidas, facilitando a manutenção, testes e evolução do sistema.

## O que é Clean Architecture?

Clean Architecture é um conjunto de **princípios e boas práticas** que visam tornar o código de um projeto mais **organizado**, **desacoplado**, **testável** e **fácil de manter**, por meio da **separação de responsabilidades em camadas bem definidas**.

Esse modelo propõe dividir o sistema em **camadas independentes**, onde as **regras de negócio (domínio)** ficam **isoladas dos detalhes de implementação** como frameworks, banco de dados e bibliotecas externas. Isso permite maior **flexibilidade**, **testabilidade** e **manutenibilidade**.

O objetivo principal é **manter as regras de negócio no centro da aplicação** de forma que não dependam de **frameworks, bancos de dados, bibliotecas externas, nem da interface do usuário**.

#### As 4 camadas principais da Clean Architecture

- **Entities (Entidades):** 
   Contém as **regras de negócios mais genéricas e duradouras**, que não mudam com frequência. Aqui entram modelos do domínio com comportamentos consistentes em qualquer contexto (por exemplo, validando o formato de um nome de host).
   _Não dependem de nada externo_.

- **Use Cases (Casos de Uso):** 
   Implementam **Regras de negócios específicas da aplicação**. São responsáveis por definir  as ações do sistema, como: cadastrar cliente, gerar relatório, calcular desconto etc. 
   _Não dependem de frameworks nem de acesso a dados diretamente_.

- **Interface Adapters (Adaptadores)**: 
   **Adaptam os dados entre as camadas internas e camadas externas**. Essa camada converte dados externos para o formato que o domínio entende e vice-versa. É aqui que ficam os controllers, repositórios (interfaces + implementações), serializadores, DTOs.

- **Frameworks & Drivers (Externo):** 
   Contém tudo relacionado a **ferramentas e tecnologias externas**, como: frameworks, banco de dados, serviços de terceiros, interfaces gráficas, etc. 
   Exemplo: _Flask, MongoDB, PostgreSQL, etc_.

> **Regras de dependências**: 
>     As **camadas externas podem depender das internas**, mas **as camadas internas nunca devem depender das externas**. Isso permite, por exemplo, trocar o banco de dados, framework ou interface sem afetar a lógica de negócio.

## Principais camadas do Projeto

- **Domain:** Regras de negócio e entidades do domínio.
- **Data:** Implementação dos casos de uso e interfaces de repositórios.
- **Infra:** Detalhes de infraestrutura, como acesso ao banco de dados.
- **Presentation:** Camada responsável por receber requisições e retornar respostas (controllers).
- **Main:**  Conecta todas as camadas e inicializar o servidor.
- **Validators:** Validação de dados de entrada.
- **Errors:** Tratamento e tipos de erros.

## Estrutura de Pastas

```
CleanArchitecturePython/
│   run.py                # Ponto de entrada da aplicação
│   requirements.txt      # Dependências do projeto
│   Dockerfile            # Configuração para container Docker
│   README.md             # Documentação
│
├── init/
│   └── schema.sql        # Script de criação do banco de dados
│
├── src/
│   ├── core/             # Configurações globais
│   ├── data/             # Casos de uso, interfaces e testes de integração
│   ├── domain/           # Entidades e casos de uso do domínio
│   ├── errors/           # Tratamento e tipos de erros
│   ├── infra/            # Infraestrutura (banco de dados, repositórios)
│   ├── main/             # Composição, rotas e servidor
│   ├── presentation/     # Controllers, DTOs e interfaces de apresentação
│   └── validators/       # Validação de dados de entrada
```


## Descrição das Pastas/Arquivos

#### `run.py`
Ponto de entrada da aplicação. Inicializa o servidor web.

#### `src/core/config.py`
Configurações globais do projeto (ex: variáveis de ambiente).

#### `src/domain/`
- **models/**: Entidades do domínio (ex: User).
- **use_cases/**: Casos de uso puros, sem dependências externas ( O quê a aplicação faz).

#### `src/data/`
- **interfaces/**: Contratos para repositórios (inversão de dependência).
- **use_cases/**: Implementações dos casos de uso (Como a aplicação faz).
- **tests/**: Testes de integração dos casos de uso.

#### `src/infra/`
- **db/entities/**: Mapeamento das entidades para o banco de dados.
- **db/repositories/**: Implementação concreta dos repositórios.
- **db/settings/**: Configuração de conexão com o banco.
- **tests/**: Testes de integração da infraestrutura.

#### `src/presentation/`
- **controllers/**: Recebem requisições, validam dados e chamam casos de uso.
- **http_types/**: Tipos para requisições e respostas HTTP.
- **interfaces/**: Interface para controllers.

#### `src/main/`
- **adapters/**: Adaptações entre camadas (ex: request adapter).
- **composers/**: Composição de dependências (injeção de dependências).
- **routes/**: Definição das rotas da aplicação.
- **server/**: Inicialização do servidor web.

#### `src/validators/`
Validação dos dados de entrada para os casos de uso.

#### `src/errors/`
Definição e tratamento de erros customizados.

#### `init/schema.sql`
Script de criação do banco de dados.

#### `requirements.txt, Dockerfile`
Dependências e configuração de ambiente.

#### `README.md`
Documentação principal do projeto, explicando sua estrutura, funcionalidades e como executá-lo.

<!--
### Endpoints

1. **Cadastro de Usuário**
- Permite criar um novo usuário no sistema, recebendo dados como nome, e-mail, senha, etc.
- Valida os dados de entrada antes de salvar no banco de dados.
- Retorna mensagens de sucesso ou erro conforme o caso.
1. **Consulta de Usuário**
- Permite buscar um usuário pelo seu identificador (ID).
- Retorna os dados do usuário caso exista, ou uma mensagem de erro caso não seja encontrado.
-->

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o servidor:
   ```bash
   python run.py
   ```

## Referências

https://youtube.com/playlist?list=PLAgbpJQADBGK0opZ8ZuDX3zDjQck_QKMy&si=PetgKNkVJEfsEMkr

https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

https://www.thedigitalcatbooks.com/pycabook-introduction/
