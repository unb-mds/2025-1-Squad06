Para manter nosso histórico limpo, rastreável e conectado com as issues do GitHub, siga estas orientações ao fazer commits.

---

## ✅ Como Referenciar uma Issue

Sempre mencione a issue na **mensagem do commit** usando:

- `refs #<número_da_issue>` → referencia a issue (o commit aparece na timeline da issue).
- `closes #<número_da_issue>` → fecha automaticamente a issue quando o commit (ou PR) for aceito.

### Exemplo:
- git commit -m "feat: Implementa servidor mobile com template Flet — refs #23"



---

# 🚀 Tipos de Commit

| Tipo      | Uso                                                    |
|-----------|---------------------------------------------------------|
| feat      | Nova funcionalidade                                     |
| fix       | Correção de bug                                         |
| docs      | Mudanças em documentação (MDs, READMEs, atas, etc)      |
| refactor  | Refatoração de código (sem mudar comportamento)         |
| test      | Adição ou correção de testes                            |
| chore     | Outras tarefas (builds, configs, scripts)               |
| style     | Mudanças que não afetam a lógica (ex: formatação, lint) |

---

# 🎯 Exemplos de Mensagens de Commit

- `feat: Implementa servidor mobile com template Flet — refs #23`
- `docs: Atualiza ata da sprint 28/04/2025 — refs #23`
- `fix: Corrige bug na tela de votação para mobile — closes #24`
- `chore: Atualiza dependências do projeto — refs #25`
- `refactor: Melhora estrutura do backend para integração com frontend — refs #26`

- ESSE COMMIT ESTÁ NA ISSUE [#25](https://github.com/unb-mds/2025-1-Squad06/issues/25)
