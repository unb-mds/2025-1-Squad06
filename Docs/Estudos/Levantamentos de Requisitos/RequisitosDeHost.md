# 📋 Requisitos de Host – Aplicativo de Votação Local via UDP

## 🎯 Objetivo do Host

Hospedar uma aplicação de votação local que funcione em redes internas, com comunicação via protocolo **UDP**, sem dependência de internet.

---
## 🖥️ Requisitos Mínimos de Hardware

| Recurso       | Mínimo              | Ideal                 |
|---------------|---------------------|------------------------|
| CPU           | 1 núcleo (1.2 GHz)   | 2 núcleos (2.0+ GHz)   |
| RAM           | 1 GB                | 2–4 GB                |
| Armazenamento | 512 MB (SSD)        | 2 GB (para logs e backups) |
| Rede          | Interface Ethernet ou Wi-Fi local |


> ⚠️ O host pode ser um notebook, mini PC, Raspberry Pi ou servidor local.

---

## 💻 Requisitos de Software

- **Sistema Operacional**: Linux (Ubuntu Server recomendado) ou Windows (a definir)
- **Ambiente de Execução**: (a definir)
- **Bibliotecas UDP**: *(a definir, dependente da linguagem)*
- **Interface Gráfica**: *(a definir)*
- **Gerenciamento**: Interface de administração local (web ou desktop) *(a definir)*

---

## 📡 Requisitos de Rede

- Comunicação via **protocolo UDP** (ex: portas 5005, 5006)
- Conexão via **Wi-Fi ou cabo Ethernet**
- Rede local (LAN) sem necessidade de internet
- Possibilidade de criar **hotspot ou roteador local** para conectar os dispositivos

---

## 🔐 Requisitos de Segurança (Rede Local)

- Isolamento físico da rede (sem acesso externo)
- Registro de logs local
- Exportação de resultados (PDF/CSV) *(se necessário,  definir a necessidade)*
- Controle de acesso do administrador/master (login local simples) 

---

## 🧰 Funcionalidades Esperadas

- Envio de perguntas e controle da votação **(importante)**
- Registro de votos com três opções:
  - ✅ A favor
  - ❌ Contra
  - ⚪ Abstenção
- Visualização de resultados em tempo real **(importante)**
- Armazenamento local das votações realizadas **(importante)**

---

