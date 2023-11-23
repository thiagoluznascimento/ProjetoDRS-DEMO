# Teste prático – Para processo seletivo bolsista desenvolvedor Python CCM-ITA

## Descrição do desafio
Esse teste prático tem como objetivo verificar skills de programação em Python considerando
o escopo de projeto que será desenvolvido ao longo do projeto DRS:DEMO

1. Existe um bico de jateamento com abertura lbico centrado no ponto b, localizado nas
coordenadas (xb, yb);
2. O bico gira ao redor de b no ângulo θ, sendo mantido o centro em posição constante;
3. A geometria que será tratada pelo processo de jateamento é representada pela curva
y = 10 * cos (x), no intervalo de 0 ≤ x ≤ pi;
4. A granalha do jateamento atinge a geometria durante o processo na zona ljateado;
5. A granalha sai sempre perpendicular à abertura do bico
6. A zona jateada varia de acordo com o ângulo θ.

## Objetivo do programa
Encontro da curva entre comprimento instantâneo da zona jateada
ljateado em função do ângulo θ, com θ variando entre 0 e 360°.

1. Não é necessário estabelecer a relação matemática (regressão, por exemplo) entre
ljateado e θ. Apenas o gráfico é considerado como resultado.
2. Deverá ser possível a alteração da coordenada do ponto b (xb, yb) pelo usuário. Ao
alterar, o resultado anterior deverá ainda estar visível no gráfico, estando claro para o
usuário qual é a simulação antiga e qual é a simulação atual.

## Preparação do ambiente de desenvolvimento
Para executar o projeto é necessário ter o Python 3.7 instalado e seguir os passos:


1. Clonar o repositório:
``` bash
git clone https://github.com/thiagoluznascimento/ProjetoDRS-DEMO.git
```

2. Crie um ambiente virtual
```bash
virtualenv venv -p python3.7
```
3. Comando para ativar o ambiente virtual
```bash
source venv/bin/activate
```
4. Instale as bibliotecas  numpy e matplotlib :
```bash
pip install numpy matplotlib
```

5. Instale os requirements.txt
```bash
pip install -r requirements.txt
```

## Execute o Flake8
6. Comando para executar o flake8.
```bash
flake8 src/main.py 
```

## Execute o programa
7. Comando para executar o programa pelo terminal
```bash
Ctrl + f5
```
## Observações:
8. Este programa foi desenvolvido utilizando o Ubuntu 22.04.3 LTS e como IDE Visual Studio Code (VS Code)

## Dificuldades
De início, uma das dificuldades que eu tive foi entender o problema proposto. Busquei soluções recorrendo ao meu professor de cálculo no Instituto Federal (IFNMG). Após superar essa etapa, enfrentei o desafio de estudar as bibliotecas utilizadas (numpy e matplotlib), nas quais estou aprofundando meus conhecimentos.
