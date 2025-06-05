# Projeto Uninove

###  turma 50 

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Giovanna Siqueira Batista</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Fernando Borges Granzotti de Jesus</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Felipe Gabriel</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Jeniffer de Andrade Batista </a> 



## 👩‍🏫 Professores:
 <a href="https://www.linkedin.com/company/inova-fusca">Joao Vagner Pereira Da Silva</a>

# Sistema de Gestão Agrícola 🌱
 
Este sistema foi desenvolvido para auxiliar agricultores em todo o ciclo de planejamento agrícola, desde o cadastro do plantio até a previsão de custos. Seu grande diferencial é a integração automática entre:
 
- *Cálculo da área plantada*  
- *Estimativa de gastos com insumos*
 
Isso possibilita uma visão financeira precisa *antes mesmo do plantio*, permitindo ao produtor tomar decisões mais embasadas.

 
# - Funcionalidades Principais
 
### 1. Cadastro Inteligente de Plantio
- 📐 *Cálculo automático da área* (em hectares) a partir do formato de plantio:  
  - Quadrado  
  - Retângulo  
  - Triângulo  
  - Hexágono  
  - Linhas paralelas  
- *Registro da época ideal de plantio* para cada cultura  
- *Visualização centralizada* de todos os plantios cadastrados  
 
### 2. Gestão de Insumos com Cálculo de Custos
- *Cálculo automático da quantidade de insumos necessários* (com base na área)  
- *Estimativa de custo por tipo de insumo* (por exemplo: Fertilizante, Defensivos, Sementes)  
- *Cálculo do custo total agregado* para cada plantio  
- *Relatórios claros* mostrando, por cultura, a relação “kg/ha → kg total → custo total”
 
### 3. Assistente Virtual (Chatbot)
- Integração de um *Chatbot* para atendimento instantâneo  
- Permite ao usuário tirar dúvidas sobre:  
  - Dosagem de insumos (ex.: “Quantos kg de NPK para 2 ha de soja?”)  
  - Época de plantio (ex.: “Quando plantar milho na minha região?”)  
  - Cálculo financeiro (ex.: “Qual o custo estimado de insumos para 3 ha de café?”)  
- *Respostas contextuais*, com base nos dados já cadastrados no sistema.


## 📦 Estrutura do Projeto
📂 gerenciador-culturas:  

─ 📄 cadastro.py = Funções para cadastrar culturas  

─ 📄 cultura.py = Classe Cultura e cálculos de área/insumos  

─ 📄 plantio.py = Função para adicionar dados de plantio  

─ 📄 menu.py = Menu principal do programa  

─ 📄 mediaDesvio.R = Calculo da media e desvio em R  

─ 📄 README.md = Documentação do projeto 


## 📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o **Python 3** instalado na sua máquina.  

Você pode verificar a versão instalada com o comando:
```  
python --version
````

## 📌 Exemplo de Uso


--- Menu Principal ---
1. Cadastrar cultura
2. Adicionar dados de plantio
3. Ver culturas cadastradas
4. Excluir cultura
5. Sair