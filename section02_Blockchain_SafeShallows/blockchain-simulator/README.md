# Blockchain Simulator

Este projeto é uma aplicação que simula uma blockchain com funcionalidades básicas, desenvolvida em Python. Ele permite a criação de blocos, a realização de transações e a validação de uma blockchain simplificada, usando funções de hash e princípios básicos de segurança.

---

## Pré-requisitos

⚠️ Python (versão 3.6 ou superior)

O projeto não possui dependências externas além da biblioteca padrão da linguagem, sendo necessário apenas garantir que o Python esteja instalado e configurado corretamente.

## Configuração inicial
Para utilizar a aplicação, siga as etapas abaixo:

1. Clone o repositório remoto para a sua máquina local. Isso pode ser realizado através do comando:

```bash
git clone --branch section02_Blockchain_SafeShallows https://github.com/BeatrizWG/reports-and-projects.git

```
2. Após clonar o repositório, navegue até o diretório do projeto: 
   
```bash
cd reports-and-projects/section02_Blockchain_SafeShallows/blockchain-simulator

```

## Executando a aplicação

Após configurar o ambiente, você pode executar a aplicação diretamente no terminal.  Use o seguinte comando:

```bash
python blockchain.py
```
Ao fazer isso, o menu de opções será exibido, permitindo a interação com a blockchain.

---

## Funcionalidades
Esta aplicação oferece recursos para criar e gerenciar uma blockchain básica, realizar transações e validar o estado da blockchain. Abaixo está uma lista das principais funcionalidades desenvolvidas:

### Blockchain
- **Criação da blockchain (Genesis Block)**: A função `create_blockchain()` inicializa a blockchain, criando automaticamente o primeiro bloco (gênesis), onde 100 moedas são atribuídas ao primeiro usuário, Satoshi.
- **Exibição da blockchain**: A função `show_chain(chain)` permite visualizar todos os blocos da blockchain, incluindo os detalhes de cada transação contida em cada bloco.

### Transações
- **Criação de transações**: Ao adicionar um novo bloco, a função `create_transaction(chain)` é chamada, solicitando os dados da transação, como remetente, destinatário, IDs das moedas e o valor a ser transferido.
- **Adição de novos blocos**: Cada transação gera um novo bloco, que é adicionado à blockchain. O bloco contém um ID único, hash, timestamp, dados da transação e o hash do bloco anterior.
- **Validação de transações**: Antes de um bloco ser adicionado, a transação é validada automaticamente pela função `add_block(chain, block)`, que utiliza duas funções auxiliares:  `validate_coin_ownership(chain, block)`, que valida a propriedade das moedas listadas na transação, e `validate_transaction(chain, block)`, que garante que o remetente tem saldo suficiente.

### Validação da Blockchain
- **Verificação de Integridade**: A função `validate_blockchain(chain)` verifica se a blockchain permanece intacta, avaliando se os hashes de cada bloco estão corretos e se cada bloco contém o hash válido do bloco anterior, garantindo, assim, que não houve alterações.
 
---

## Exemplo de uso
Após iniciar a aplicação, o menu interativo exibirá as seguintes opções:

```plaintext
Options Menu:
1. Add a new block
2. Display the blockchain
3. Validate the blockchain
4. Exit
```

**1. Adicionando um bloco**

Ao escolher a opção "1. Add a new block", você será solicitado a fornecer as informações da transação, como nome do remetente, nome do destinatário, IDs das moedas e valor da transação. A transação será validada e, se aprovada, o novo bloco será adicionado à blockchain.

**2. Exibindo a blockchain**

Ao selecionar "2. Display the blockchain", será exibida uma listagem de todos os blocos, incluindo suas transações e informações de hash.

**3. Validando a blockchain**

Ao escolher "3. Validate the blockchain", o sistema verifica a integridade da blockchain e informa se ela está válida ou foi corrompida.

**4. Saindo do sistema**

Ao selecionar "4. Exit", o sistema será encerrado.