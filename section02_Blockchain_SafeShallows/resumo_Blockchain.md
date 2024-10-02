# BLOCKCHAIN E BITCOIN

## BITCOIN
* Moeda digital que serve como meio de troca, com seus próprios protocolos de transferência.
* Funciona por meio da criptografia da blockchain, redes descentralizadas e da engenharia do incentivo.

## BLOCKCHAIN

* Conjunto de blocos de informações conectados, onde cada bloco contém dados e a referência ao bloco anterior e que qualquer alteração em um bloco modifica toda a cadeia subsequente.
* Utiliza função Hash, que gera uma saída de tamanho fixo a partir de uma entrada. 
* Uso do protocolo de fofoca para divulgar as informações na rede.
* Qualquer computador conectado à rede é um nó, que pode ser de dois tipos:
  * **Full nodes**: validam todas as transações e garantem a consistência da rede.
  * **Lite nodes**: armazenam apenas parte da blockchain, dependendo de outros nós para dados completos.
* Ataques de 51%: se um minerador ou grupo controlar mais de 51% da rede, podem tentar modificar transações.

**PRINCIPAIS CARACTERÍSTICAS:**
* **Transparência**: registros visíveis para todos.
* **Imutabilidade**: uma vez incluído na cadeira, um bloco não pode ser alterado.
* **Segurança aprimorada**: uso de criptografia.
* **Descentralização**: sem uma autoridade central.
* **Irreversibilidade**: transações não podem ser desfeitas.
* **Liquidações rápidas**: processos de confirmação ágeis.

|                      **RECOMENDAÇÕES DE USO:**                      |                           **QUANDO NÃO USAR:**                           |
|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
|         Gerenciamento e proteção de relacionamentos digitais        |                 Se o processo envolver dados confidenciais               |
|                 Uso adequado da rede descentralizada                |                     Se precisar de transações rápidas                    |
|         Quando não há confiança entre as partes envolvidas          |         Se as regras de transações forem alteradas com frequência        |
|         Registro seguro de transações entre vários parceiros        |           Quando houver muito armazenamento de dados estáticos           |
| Necessidade de rastreamento correto de dados que não são constantes | Quando for necessário usar serviços externos para armazenamento de dados |

---

A tecnologia blockchain é composta por diversos elementos que trabalham em conjunto para garantir a segurança, transparência e eficiência das transações e as operações na rede. Abaixo, serão detalhados os principais componentes da blockchain:

**1. FUNÇÕES HASH CRIPTOGRÁFICAS**
* Fácil de computar: tem um processamento eficiente.
* Livre de colisões: duas entradas diferentes geram saídas diferentes.
* Unidirecional: impossível deduzir a entrada a partir da saída.
* Puzzle Friendly: pequenas alterações na entrada resultam em grandes modificações na saída.

**2. BLOCO**

* É um conjunto de transações que foram verificadas e registradas. Cada bloco contém:
  * Dados sobre as transações.
  * Um hash do bloco anterior.
  * Um nonce (um número aleatório usado no processo de mineração).
  * O hash do bloco gerado a partir das informações do bloco e do nonce.

**3. ASSINATURAS DIGITAIS**
* Toda transação precisa ser assinada digitalmente.
* A assinatura é única para cada transação e somente o dono de uma chave privada pode assinar.
* Garantem a autenticidade e a integridade das transações. 
* A assinatura pode ser verificada com a chave pública, garantindo que não houve alteração.

**4. MINERADORES**
* Mineradores são responsáveis por validar novas transações e criar os novos blocos, os adicionando à blockchain.
* Eles competem para adicionar o próximo bloco à cadeia (usando Proof of Work) e, em troca, são recompensados com novas criptomoedas.
* Ajudam a manter a integridade e a segurança da rede.

**5. TRANSAÇÕES** 
* Uma transação na blockchain envolve a transferência de criptomoedas (ou outro ativo digital) de um endereço para outro.
* Cada transação é registrada de forma permanente na blockchain, sendo validada pelos mineradores.
* As transações são agrupadas em blocos, podendo ser de dois tipos:
  * **De pagamento**: envio de valores e pagamento aos mineradores, com a diferença sendo enviada como troco.
  * **De criação de moedas**: chamada de Coinbase Transaction, gera novas moedas para o minerador que criam o bloco. O valor da recompensa é reduzido pela metade a cada quatro anos.      

**6. PROF OF WORK**

* É um processo no qual os mineradores precisam resolver um problema matemático complexo, utilizando o nonce.
* Deve ser gerado um Hash que atende aos critérios (número específico de zeros no início).
* A difilcudade do cálculo é ajustada conforme a demanda, para que seja possível encontrar um novo bloco a cada 10 minutos.
* O método envolve tentativa e erro (força bruta).
* É uma medida de segurança contra ataques, pois demanda um grande poder computacional.
  
**7. CARTEIRAS**
* O saldo é calculado a partir da quantidade de moedas em uma determinada chave pública, a carteira automatiza esse processo.
* Armazenam as chaves públicas e privadas necessárias para realizar transações na blockchain.
 
|  Tipo  |                                                           Descrição                                                         |
|:------:|:---------------------------------------------------------------------------------------------------------------------------:|
|  Papel |                              Simples; Inconveniente para transações frequentes; Imune a hackers                             |
|Hardware|                               Extremamente seguras; Permitem recuperação de moedas; Alto custo                              |
|Software|  Múltiplos pares de chaves; Recuperação de moedas; Dependem da segurança do aparelho; Adaptadas a mais de um tipo de moeda  | 
| Online |        Armazenamento na nuvem; Múltiplos pares de chaves; Vulnerável a ataques de hackers; Vários serviços embutidos        |

**8. EXCHANGES**

* São plataformas onde os usuários podem comprar, vender ou trocar criptomoedas.
* Os preços são determinado pelo mercado.
* Riscos incluem falta de reservas, controle de investimentos e ausência de garantia de crédito.
* Cobram taxas pelas transações.
* Exchanges são alvos frequentes de ataques de hackers, tornando a segurança uma preocupação constante.

---

## ETHEREUM

* Altcoin é um termo que se refere a qualquer criptomoeda alternativa ao Bitcoin, sendo o Ethereum um dos principais exemplos.
* Difere do Bitcoin no conceito e capacidade de processamento.
* Moeda nativa: Ether.
* Suporta Smart Contracts e aplicações descentralizadas (DApps).
* Utiliza *mineração memory hard*, em que o processamento depende da memória.
* Utiliza a linguagem Solidity.
* Ethereum Virtual Machine é o ambiente de execução responsável por manter a blockchain do Ethereum em funcionamento. 

A seguir, serão apresentados os componentes fundamentais dessa aplicação. 

**1. Gas**
* Taxa paga para o processamento de transações no Ethereum.
* O preço varia de acordo com a demanda da rede. Transações mais complexas consomem mais Gas.
* Servem como incentivo para produção de códigos mais eficientes e para evitar Denial of Service Attack (Ataques de negação de serviço).
* Operações executadas pode ser finalizadas normalmente, mas podem parar ao atingir o Gas Limit ou usar todo o Gas criado na transação.

**2. Smart Contracts**
* São contratos digitais que rodam na blockchain do Ethereum, escritos em código computacional.
* Eles contêm regras e condições que, uma vez atendidas, executam automaticamente ações predefinidas.
* Uma vez implantados, não podem ser revertidos, a menos que tenham cláusulas para permitir alterações.
* Os programas são autoexecutáveis, aplicando a lógica sem a necessidade de intermediários.

**3. DApps**

* São aplicações open-source que rodam em redes blockchain.
* São descentralizados, sem intermediários e sem pontos centrais de falha.
* A lógica do aplicativo é programada nos contratos, que são autoexecutáveis e imutáveis.