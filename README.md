# 🎓 Sistema de Gerenciamento Acadêmico

Uma aplicação de interface de linha de comando (CLI) desenvolvida em Python para o registro, processamento e análise do desempenho acadêmico de estudantes. 

Este projeto foi arquitetado com foco em **Clean Code**, **Programação Defensiva** e **Modularização**, separando estritamente a lógica matemática (cálculos) da camada de apresentação (geração de relatórios).

---

## 🎯 Propósito do Projeto

O sistema automatiza a tomada de decisão institucional. Ele recebe os dados brutos dos estudantes, processa as médias aritméticas isolando possíveis anomalias (como a ausência de notas ou entradas inválidas) e emite um relatório tabular ordenado por desempenho, apontando o status de aprovação de cada aluno e as estatísticas gerais da turma.

**Principais Funcionalidades:**
* Processamento otimizado de médias acadêmicas ($O(n)$).
* Validação de regras de negócio flexíveis (nota de corte parametrizada).
* Geração de relatórios tabulares dinâmicos no terminal.
* Proteção contra falhas de tipagem e exceções matemáticas (ex: `ZeroDivisionError`).

---

## ⚙️ Pré-requisitos Lógicos e de Sistema

Para executar este projeto localmente, sua máquina precisará atender aos seguintes requisitos básicos:

* **Linguagem:** Python 3.10 ou superior (necessário devido ao uso de *Type Hints* modernos e operadores sintáticos atualizados).
* **Terminal:** Qualquer terminal de linha de comando (Git Bash, Windows Terminal, PowerShell ou terminal integrado da sua IDE).
* **Bibliotecas:** O projeto foi construído utilizando puramente a *Standard Library* do Python. Não é necessária a instalação de pacotes externos via `pip`.

---

## 🚀 Como Executar o Sistema (Produção)

1. **Clone o repositório ou baixe os arquivos:**
   ```bash
   https://github.com/fabiodmu-ux/Sistema-de-Gerenciamento-Acad-mico.git
   cd Sistema-de-Gerenciamento-Acad-mico
