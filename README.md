### Real-Time Architecture and Machine Learning Model for Credit Card Fraud Detection
API - Bank Virtual 

### Projeto de Engenharia de Dados: Detecção de anomalias em transações de cartão de crédito através de uma API de um banco de dados MongoDB utilizando Machine Learning

## Introdução

Dentro do escopo de atividades de um engenheiro de dados, a disponibilização ou recebimento de dados por meio de uma API é uma prática comum. Essa API pode ser consumida por diferentes aplicações, alinhando-se com as vantagens associadas à filosofia de microsserviços. Dentre outras como melhoria da segurança, a abstração eficiente de dados, e a flexibilidade de manutenção.

Nesse contexto, este projeto tem como objetivo o desenvolvimento de uma API capaz de realizar detecções de anomalias em transações de cartão de crédito utilizando machine learning em um banco de dados MongoDB hospedado na Nuvem da Amazon Web Services (AWS).   

Nesse contexto, este projeto tem como objetivo o desenvolvimento de uma API capaz de realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados MySQL hospedado no Cloud SQL, dentro do ambiente de nuvem da Google (GCP). Ao longo do desenvolvimento, serão incorporadas boas práticas de Integração Contínua e Entrega Contínua (CI/CD). Isso incluirá o provisionamento da infraestrutura como código, utilizando o Terraform, e a implementação de pipelines automatizadas de código. Essas práticas serão integradas ao GitHub, permitindo a execução automática em ambientes de produção ou desenvolvimento sempre que houver mudanças no repositório.

# Tecnologias Utilizadas
  - MongoDB: Sistema de banco de dados NoSQL orientado a documentos, que oferece flexibilidade e escalabilidade, ideal para lidar com grandes volumes de dados e estruturas de dados variáveis.
  - FastApi: Framework em Python utilizado para o desenvolvimento da API. Oferece desempenho eficiente e facilidade de desenvolvimento, possibilitando a criação de endpoints eficazes.
  - Python: Linguagem de programação utilizada no projeto, integrada ao framework FastAPI para a implementação da lógica da API.
  - Docker: Utilizado para criar imagens com as bibliotecas necessárias que serão empregadas no CloudRun.
  - Uvicorn: Servidor ASGI leve e rápido para Python, utilizado para hospedar a aplicação FastAPI, proporcionando alto desempenho e capacidade de lidar com conexões assíncronas.
  - AWS (Amazon Web Services): Utilizada para hospedar aplicações, gerenciar bancos de dados (como o MongoDB), e fornecer recursos computacionais, armazenamento, e outros serviços essenciais para a operação e escalabilidade da sua API e outras componentes do sistema.
  - Pandas: Biblioteca de Python para manipulação e análise de dados, oferecendo estruturas de dados e ferramentas robustas para manipular tabelas e séries temporais.
  - Scikit-learn: Biblioteca de Python para aprendizado de máquina, proporcionando uma gama de algoritmos para classificação, regressão, clustering e redução de dimensionalidade.
  - SciPy: Conjunto de ferramentas de Python para matemática, ciência e engenharia, abrangendo módulos para otimização, álgebra linear, integração, e mais.
  - Joblib: Biblioteca utilizada para serialização de objetos Python, especialmente útil para salvar e carregar modelos de aprendizado de máquina.
  - NumPy: Biblioteca fundamental para computação científica em Python, oferecendo suporte a arrays multidimensionais e ferramentas para operações matemáticas complexas.
  - Pydantic: Biblioteca para validação e gerenciamento de dados em Python, usada especialmente para criar modelos de dados com tipos fortemente tipados.

## Machine Learning Architecture

![ml_2](https://github.com/robsonsants/Credit_Card_Fraud_Detection/assets/32533017/1f17fb2d-f36f-4396-a74a-0b4148417842)

## Project Architecture

![ap1_vesta](https://github.com/robsonsants/Credit_Card_Fraud_Detection/assets/32533017/ff1a70b4-9bde-4538-8e7e-c10492d2a496)

## Etapas do Projeto

1. Conjunto de Dados
    
  Este trabalho utiliza o conjunto de dados denominado IEEE-CIS Fraud Detection ´´ https://www.kaggle.com/competitions/ieee-fraud-detection ´´, o qual foi elaborado para possibilitar a construção e a avaliação de sistemas de detecção de fraudes em comércio eletrônico. Esse conjunto de dados é formado por duas tabelas principais: a tabela de transações e a tabela de identidades. Na tabela de transações estão contidas informações cruciais sobre cada transação, incluindo o valor da transação, o cartão de crédito utilizado, a data e a hora da operação, além de outros atributos relevantes. Na tabela de identidades são fornecidos dados adicionais sobre os indivíduos envolvidos nas transações, incluindo características demográficas e informações sobre os dispositivos utilizados pelos usuários.

  O conjunto de dados IEEE-CIS Fraud Detection inclui 434 atributos, dos quais 400 são anonimizados (V1 a V339), a fim de proteger a privacidade de usuários e instituições. Cada linha da tabela de transações representa uma determinada transação eletrônica. Cada transação possui um rótulo, o qual pode assumir dois valores indicando: transação legítima ou transação fraudulenta. Neste sentido, o conjunto de dados pode ser utilizado para construir classificadores binários. Como o conjunto de dados é bastante grande e desbalanceado, utilizamos apenas uma parte dos dados, mais precisamente um subconjunto formado pelo train_identity e o train_transaction, formando assim um novo conjunto de dados, o qual será utilizado nas etapas subsequentes deste trabalho.

2. Criação da Imagem Docker

   Para facilitar a implementação da API, desenvolveu-se um Dockerfile. Esse documento inclui uma imagem do Python, incorporando todas as bibliotecas essenciais para o projeto, assim como o código-fonte completo da aplicação. Uma vez estabelecido o container, procedeu-se com a execução de um comando para estabelecer um serviço usando Uvicorn em uma porta designada, a qual permite o acesso à API.
   Utilizamos Docker para garantir um ambiente de execução consistente e repetível. Essa ferramenta permite que o software seja executado de forma confiável em diferentes ambientes, simplificando o desenvolvimento, teste e implantação.

3. Criação das Máquinas na AWS

   O sistema foi implementado em instâncias de máquinas virtuais do tipo t2.medium, com 2 vCPUs e 4 GB de RAM, na região de São Paulo da nuvem da Amazon Web Service (AWS). Para cada serviço foi alocada uma máquina virtual, além de uma máquina virtual para o Locust. Cada serviço foi executado em um único container Docker.  
  Foi dada ênfase especial aos dados mantidos na parte da Vesta, para replicar a funcionalidade de uma aplicação bancária autêntica. A finalidade disso foi garantir a melhor simulação possível de uma aplicação bancária real na execução dos testes.
  Todos esses elementos trabalham juntos para apoiar a aplicação, permitindo que todo o sistema seja iniciado, parado e gerenciado de maneira conveniente, proporcionando uma alta eficiência e portabilidade.

4. Experimentos
   Para avaliar o desempenho e capacidade máxima de atendimento do sistema, realizamos experimentos utilizando a ferramenta Locust ´´ https://locust.io/ ´´, uma estrutura de teste de carga de código aberto que permite simular ações simultâneas de múltiplos usuários em um serviço web. Durante os experimentos, Locust foi empregado para capturar métricas críticas, tais como o tempo de resposta de cada requisição e o número total de requisições atentidas. Além disso, um registro detalhado foi mantido, incluindo a duração exata que cada serviço levou para processar e concluir uma transação e o consumo de CPU e memória das máquinas virtuais utilizadas. Com isso, foi possível obter uma visão abrangente do desempenho do sistema sob carga, identificando potenciais gargalos e identificando oportunidades de melhorias para trabalhos futuros.
    
  A aplicação foi submetida a experimentos que variaram o número de clientes iniciais e a taxa de geração (i.e., quantidade de clientes iniciados por segundo). Foram executados 6 experimentos com configurações diferentes: utilizando 10 clientes e taxa de geração de 5 clientes/s; 20 clientes com taxa de 10 clientes/s, 30 clientes e taxa de 15, 40 clientes e taxa de 20, 50 clientes e taxa de 25 e, por fim, 60 clientes e 30 iniciados por segundo. O tempo de duração do experimento foi mantido em 3 minutos nas 6 configurações.

  Para questões de análise, foram removidas 10% das requisições iniciais em todos os experimentos por ser uma fase de warm up do sistema.

