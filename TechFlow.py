🤖 FASE 2: Integração e Análise com Copilot Agent
(Nesta fase, você criará a base de dados e deverá escrever seus próprios prompts para orientar o Copilot Agent no GitHub Codespaces)

Etapa 3: Criação da Base de Dados e Elaboração do Prompt de Leitura
Criação manual do arquivo: Na raiz do projeto no Codespaces, crie o arquivo custos_cloud.csv com a tabela abaixo:
Snippet de código



Recurso, Custo
Servidor AWS, 180.00
Banco Postgres, 95.00
Backup Cloud, 50.00
Dominio SSL, 25.00
Desafio de Prompting (Você cria o prompt para o Agent): Abra o chat do Copilot Agent e elabore um prompt pedindo para ele adicionar o código de leitura no main.py.
Seu prompt deve conter obrigatoriamente as seguintes instruções para a IA:

Pedir para abrir o arquivo custos_cloud.csv em modo leitura ("r") com encoding="utf-8" usando with open().
Exigir que a leitura do cabeçalho e das 4 linhas de dados seja feita linha a linha utilizando .readline() em variáveis separadas.
Proibir explicitamente o uso de laços de repetição (sem for ou while).
Solicitar a exibição com print() no terminal de cada uma das linhas lidas.
⚠️ Atenção: Revise o código gerado antes de aceitar. Se o Agent usar laços (for), peça para ele refazer de forma sequencial com .readline(). Execute python main.py para testar.
Etapa 4: Elaboração do Prompt para Painel e Cálculo Final
Agora você deve instruir o Agent a consolidar as informações do sistema, relacionando a empresa com o espaço físico e calculando o gasto total.

Desafio de Prompting (Você cria o prompt para o Agent): Abra o chat do Copilot Agent e peça para ele gerar a seção de consolidação no final do main.py.

Seu prompt deve conter obrigatoriamente as seguintes instruções para a IA:

Recuperar o nome da empresa a partir do Dicionário startup criado na Etapa 1 e informar que ela ocupa a "Bancada N1".
Indicar que as linhas lidas do CSV são textos com vírgula e solicitar a conversão dos valores numéricos para o tipo decimal (float).
Solicitar a soma dos 4 custos de infraestrutura em uma variável de total.
Exibir um painel final no terminal contendo:
O nome da startup.
A bancada alocada (Bancada N1).
O valor total calculado de infraestrutura Cloud formatado com duas casas decimais.
⚠️ Atenção: Execute o script completo com python main.py e certifique-se de que o terminal exibe todas as etapas sem erros de execução ou tipo de dado.
 No espaço abaixo confirme seu repositório GitHUB
