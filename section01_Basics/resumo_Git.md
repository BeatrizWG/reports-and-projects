# GIT E GITHUB

Git é um sistema e controle de versão distribuído. 

GitHub é um serviço e hospedagem na nuvem, para projeto que utilizam o Git.

---

### PRINCIPAIS COMANDOS

|    Comando    |                      Descrição                       |
| :-----------: | :--------------------------------------------------: |
|   git init    |            Inicia um novo repositório Git            |
|  git status   |      Verifica o estado dos arquivos e mudanças       |
|    git add    |      Adiciona arquivos ao índice *staging area*      |
|    git rm     |            Remove arquivos do repositório            |
| git commit -m |           Cria um commit com uma mensagem            |
|   git diff    |         Mostra as diferenças entre arquivos          |
|  git restore  |       Restaura arquivos para o estado anterior       |
|    git log    |             Exibe o histórico de commits             |
|   git reset   | Modifica a posição do *HEAD* para um commit anterior |
|   git push    |    Envia commits locais para o repositório remoto    |
|   git pull    |    Baixa e mescla mudanças do repositório remoto     |

---

### BRANCH

Branch é uma ramificação do código-fonte original, onde são feitas cópias sem modificar o histórico principal. Ele é utilizado para implementar grandes alterações, desenvolver novas funcionalidades ou corrigir bugs, permitindo que o time trabalhe de forma independente sem interferir no código principal. 

|  Comando   |                Descrição                |
| :--------: | :-------------------------------------: |
| git branch |   Gerencia as branches no repositório   |
| git switch |      Muda para um branch diferente      |
| git merge  | Combina mudanças de diferentes branches |

---

### ESPECIFICAÇÕES DE COMMITS

Os commits devem seguir um padrão que facilita a compreensão e rastreamento das mudanças no código, sendo o formato recomendado:

```
<tipo> [escopo opcional]: <descrição>
[corpo opcional]
[rodapé opcional]
```

A tabela a seguir apresenta os tipos de commit com suas respectivas descrições:

| Tipo |                        Descrição                         |
| :-------: | :----------------------------------------------------------: |
|   init    |   Inicialização do repositório ou adição de conteúdo base    |
|   feat    |  Adição de uma nova funcionalidade ou mudança significativa  |
|    add    |    Adição de algo novo, mas sem grande impacto funcional     |
|   docs    |             Alterações ou adições à documentação             |
|    fix    |            Correções de erros ou pequenos ajustes            |
| refactor  |       Reorganização do conteúdo sem alterar a essência       |
|   chore   | Tarefas rotineiras, como renomear arquivos ou organizar pastas |
|   style   |   Alterações de formatação ou estilo sem afetar o conteúdo   |
|  remove   |      Remoção de conteúdo desnecessário ou desatualizado      |
|  update   |   Atualização de conteúdo existente com pequenas melhorias   |
|  revert   |                Reverter uma mudança anterior                 |

  