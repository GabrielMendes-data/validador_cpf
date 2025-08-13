# Validador de CPF em Python

Este projeto é um script simples em Python que realiza a **validação de um CPF** (Cadastro de Pessoas Físicas) com base nas regras oficiais da Receita Federal do Brasil.  
O programa solicita o CPF ao usuário, formata, limpa e aplica as fórmulas matemáticas para verificar se o número informado é válido.

---

## 📋 Funcionalidades

- Solicita ao usuário um CPF (apenas números).
- Valida se contém apenas dígitos e se tem no máximo 11 caracteres.
- Formata o CPF no padrão `XXX.XXX.XXX-XX`.
- Calcula e valida os **dígitos verificadores** de acordo com a regra oficial.
- Exibe se o CPF é **válido** ou **inválido**.

---

## 🔢 Regras de Validação

### 1º dígito verificador
1. Multiplica cada um dos **9 primeiros números** por uma sequência regressiva de 10 a 2.  
2. Soma todos os resultados.  
3. Multiplica a soma por 10 e calcula o **resto da divisão por 11**.  
4. Se o resultado for **maior que 9**, o dígito é **0**; caso contrário, é o próprio resultado.

### 2º dígito verificador
1. Utiliza os **10 primeiros números** (incluindo o 1º dígito verificador calculado).
2. Repete o mesmo processo, agora com a sequência regressiva de 11 a 2.

---

## 📦 Como usar

1. **Clone o repositório ou copie o script**:
   ```bash
   git clone https://github.com/GabrielMendes-data/validador_cpf
