# 💱 Conversor de Moedas - Terminal

Este é o meu **primeiro projeto em Python**, feito totalmente com base no que aprendi até agora, **sem copiar e colar código**.  
O projeto é um **conversor de moedas** que roda no terminal e usa uma **API real (ExchangeRate-API)** para pegar os valores de câmbio em tempo real.

---

## 🧠 Funcionalidades

- Escolha de moeda de origem e destino entre 9 opções:
  - USD, EUR, GBP, JPY, CNY, ARS, CHF, CAD, BRL
- Validação de entradas
- Conversão de valores com cotação atual da moeda via API
- Loop de repetição para múltiplas conversões
- Exibe a data da última atualização da cotação

---

## 📦 Tecnologias usadas

- Python 3
- Biblioteca `requests`
- API pública [ExchangeRate-API](https://www.exchangerate-api.com/)

---

## ▶️ Como rodar o projeto

1. Instale o Python 3 se ainda não tiver
2. Instale a biblioteca `requests` (caso ainda não tenha):
   ```bash
   pip install requests
