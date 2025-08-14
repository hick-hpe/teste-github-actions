# GitHub Actions

O GitHub Actions é uma plataforma de integração contínua e entrega contínua (CI/CD) que permite automatizar a sua compilação, testar e pipeline de implantação. É possível criar fluxos de trabalho que criam e testam cada pull request no seu repositório, ou implantar pull requests mesclados em produção em máquinas virtuais do Linux, Windows e MacOS.

## Componentes do GitHub Actions

- `workflows`: processo automatizado configurável que executará um ou mais trabalhos. Inicia sua execução após um evento ser disparado (ex: push). Toda sua configuração é definida em um arquivo YAML.

- `events`: atividade específica em um repositório que dispara a execução de um fluxo de trabalho. Exemplos:
    - push
    - pull_request
    - workflow_dispatch
    - schedule
    - release
    - issues

- `jobs`: onjunto de etapas em um fluxo de trabalho executadas no mesmo executor.

- `runner`: servidor que executa seus fluxos de trabalho. Disponíveis no GitHub:
    - Linux
    - Windows
    - MacOS

## Criar o seu primeiro fluxo de trabalho

Este workflow exibirá 'Hello, World', através de um terminal Linux
- Criar a pasta `.github/workflows`
- Criar o arquivo `hello-world.yml` dentro da pasta `.github/workflows`
- Dentro do arquivo:
    ```yaml
    # define o nome do workflow
    name: Hello World

    # define os listeners
    on:
      # ouvindo o evento de `push`
      push:
        # as branches que executaram o workflow
        branches:
          - main

    # definição dos jobs
    jobs:
      # job `hello`
      hello:
        # servidor que irá executar
        runs-on: ubuntu-latest
        # etapas
        steps:
            # nome da etapa
            # - name: Clonar repositório
            # clonar o repositório com variáveis configuradas
            # uses: actions/checkout@v4

            # nome da etapa
          - name: Dizer "Hello"
            # comando a executar
            run: echo "Hello, World!"

    ```
## Visuaizando execução

- Realizar o commit:
    ```
    git commit -m "feat: Exemplo simples de workflow" 
    ```
- Enviar para o repositório:
    ```
    git push
    ```
- Após o `commit`, acessar o repositório no navegador
- Acima das pastas, notará um símbolo amarelo:
    ![Imagem](assets/img/sinal.png)
    Isso indica que o workflow está executando.

- Acessar a aba `Actions`, podemos ver todos os workflows criados
    ![Imagem](assets/img/aba-actions.png)

- Workflows
    ![Imagem](assets/img/image.png)

    Podemos ver os detalhes de cada etapa.

## Exercícios

1. Crie um workflow para ...
2. Crie um workflow para ...


