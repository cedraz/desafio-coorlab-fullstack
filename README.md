# Desafio CoorLab
Olá DEV, pronto para participar do nosso processo seletivo?

## Requisitos
- Noções de programação web
- Javascript
- HTML
- Python

## Desafio
(História fictícia) Uma empresa encomendou um sistema onde seus clientes com login e senha conseguem buscar viagens com duas opções principais, uma apresenta a viagem mais confortável e rápida, a outra a mais econômica. Por sorte, esse sistema é equipado com uma API REST que disponibiliza de forma estruturada todos os dados coletados das cotações de viagem. Tais informações estão modeladas da seguinte maneira:

```
[
  {
    "id": 1,                              <--- ID da viagem
    "name": "Expresso Oriente",           <--- Nome da empresa
    "price_confort": "R$ 205.10",         <--- Custo da viagem no modo conforto
    "price_econ": "R$ 121.50",            <--- Custo da viagem no modo economico
    "city": "São Paulo",                  <--- Cidade de destino
    "duration": "12h",                    <--- Duração da viagem
    "seat": "1A",                         <--- Poltrona (modo economico)
    "bed": "4D"                           <--- Leito (modo conforto)
  },
]
```

Implemente uma solução utilizando no frontend Vue.js e no backend python, com base nos requisitos descritos na história a seguir:


**História de Usuário: Calculadora de viagens**

Como cliente logado no sistema,
Eu desejo saber qual é o preço da viagem mais confortável e rápida e o preço da mais econômica,
Para tomar decisões mais assertivas e escolher a melhor viagem.


**Cenário: Exibição dos Melhores Preços de Viagem**

Dado que estou na página de busca por viagens,
Clicar em analisar sem preencher os dados, devo receber um aviso no modal que preciso preencher,
Quando inserir o destino,
E informar a data da viagem,
E clicar no botão "Buscar",
Então devo visualizar o nome da empresa, o tipo de leito, o tempo e custo total da viagem mais rápida,
E devo visualizar o nome da transportadora, o custo total, o leito e a duração da viagem mais econômica.


**Protótipo**

https://github.com/coorlab/coorlab-challenge_2/assets/12722903/478e86c1-a4de-4d41-9108-f76195bf3105

Caso não seja possível abrir o link anterior, o video do protótipo esta disponivel em ./doc/protype.mp4 .


**Logo do Desafio**
![Logo](./doc/logo.png)


A implementação da aplicação deve utilizar Vue.js (2 ou 3) e deve seguir os requisitos da história de usuário, cenário e protótipo.
Do ponto de vista de tecnologia utilizada para implementação, a única exigência é utilizar Vue.js (2 ou 3) no frontend e python no backend, outras bibliotecas, componentes e frameworks, podem ser utilizados, desde que sejam de código-aberto.


## Implementação
- Utilize python para implementar o backend.
- Utilize Vue.js (2 ou 3) para implementar o frontend.
- O frontend deverá se comunicar com o backend utilizando uma API REST.
- Implemente sua solução dentro do diretório "app".
- A API do backend deverá funcionar na porta 3000.
- O frontend devera operar na porta 8080.
- Utilize o arquivo "data.json" como base de dados para o backend.
- Tanto no frontend quanto no backend não é necessário implementar a autenticação do usuário.
- No arquivo "run.sh" adicione o script em bash para executar a sua aplicação, ou seja, instalar as dependências e executar o frontend e o backend.
- Utilizaremos o script de "run.sh" para realizar a correção deste desafio, ele será executado em um Ubuntu 22.04 com as seguintes dependências pré-instaladas:
    - python 3.8
    - pip
    - npm
    - yarn
    - wget
    - poetry
- Caso você necessite instalar qualquer outra dependência para sua aplicação, coloque esta ação para ser executada no "run.sh".
- No arquivo "RESULT.md", descreva como foi a sua implementação para o desafio proposto.
- Escreva o código em inglês, ou seja, variáveis, métodos, classes, logs, nomes de arquivos e qualquer outro elemento que componha o código da solução deverá estar em inglês.

## Avaliação
O que vamos avaliar:
- Atenção aos requisitos do projeto.
- Atenção as instruções que fornecemos.
- Lógica.
- Qualidade.
- Manutenibilidade.
- Organização.
- Design.
- Boas práticas.

Quais são os passos no processo de avaliação do desafio:
1. Análise da descrição da solução implementada, através da descrição fornecida pelo RESULT.md.
2. Execução da aplicação utilizando "run.sh" e validação se a solução liga e se esta acessível através das portas recomendadas.
3. Teste da solução implementada, para verificar se atende aos requisitos da história de usuário e cenário.
4. Análise do design, para verificar se a solução segue o protótipo proposto.
5. Análise do código.

## Instruções
Siga os seguintes passos para a execução do desafio:
1. Crie um repositório **público** no GitHub.
2. Faça o **clone** do repositório que você acabou de criar.
3. Extraia os arquivos do "desafio_coorlab.zip" na pasta que você fez o clone do repositório.
4. Faça o primeiro **commit** com apenas estes arquivos no seu repositório, desta forma fica mais simples avaliar o que você implementou.
5. Implemente o desafio.
6. Faça o **commit** da sua implementação, inclusive se você quiser criar um commit diferente para cada parte que você implementou, é uma prática que gostamos muito aqui na Coorlab.
7. Faça o **push** das suas alterações.
8. Após concluir os passos anteriores, preencha este [formulário](https://airtable.com/shrTjtwUrw7I1CuxE).

### Recomendações
- Não se esqueça de deixar o seu ***repositório público*** para podermos revisar o seu código, caso o repositório não esteja acessível, a solução não será avaliada.
- Garanta que o "run.sh" instale as dependências que sua solução precisa e inicia as aplicações do frontend e backend, soluções que não executam não serão analisadas.
- Iniciativa, ousadia, autonomia e proatividade são valores muito importante para nós. Acreditamos que é melhor pedir perdão do que permissão, então caso você queira adicionar alguma tecnologia para construção da solução além do que estamos propondo, ***JUST DO IT***. É só deixar indicado no RESULT.md, queremos ver o seu talento.
