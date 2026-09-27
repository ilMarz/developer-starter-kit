# Ricerca e scelte del kit

Consultazione: 27 settembre 2026. Pratiche selezionate, non una pretesa di coprire
ogni stack o ogni best practice. I link web possono evolvere; skill fissate in skills.lock.json.

| Fonte primaria | Indicazione rilevante | Applicazione nel kit |
| --- | --- | --- |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Compito preciso, caricamento progressivo; skill di repository in .agents/skills; omonime non fuse | Copie locali e router breve; selezione esplicita del percorso |
| [OpenAI: Best practices](https://learn.chatgpt.com/guides/best-practices) | Contesto del repository e verifiche concrete | AGENTS breve, comandi verificati nel setup |
| [OpenAI, 11 settembre 2026: Rethinking skills](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Rivedere istruzioni e descrizioni troppo estese o sovrapposte | Caricare soltanto la procedura pertinente; percorso leggero per piccoli cambiamenti |
| [Michael Nygard: ADR](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Decisioni brevi con contesto, stato e conseguenze | Template ADR; storico superseded conservato |
| [Matt Pocock](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills) | Slice verticali, dipendenze esplicite, test alle interfacce, glossario | to-tickets, tdd, domain-modeling; distinte specifica e piano |
| [Anthropic: Long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Incrementi e artefatti per riprendere tra sessioni | Registro durevole e handoff; nessuna fiducia nel solo riassunto della chat |
| [Anthropic, 24 marzo 2026: Harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Pianificazione, generazione e valutazione con criteri concreti | Ruoli separati, feedback dalle esecuzioni; beneficio da misurare |
| [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Distinguere trace dal risultato reale; valutazioni ripetibili | Template eval con outcome, errori, costo e casi negativi |
| [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Delega circoscritta, configurazione modelli, attenzione alle scritture concorrenti | Un implementatore per checkout, brief e reviewer; fallback esplicito |
| [Superpowers](https://github.com/obra/superpowers) | Piano, isolamento, review e verifica | Quattro copie locali più due snapshot upstream; raccordo documentato |

## Proposte nostre, da misurare

Il router unico, l'import offline, il registro a due livelli e i profili modelli sono scelte
del kit, non standard prescritti da queste fonti. L'efficacia va verificata su progetti diversi.
Nessun modello, soglia economica, tempo massimo o provider universale viene dichiarato migliore.
Aggiornare le fonti prima di cambiare procedure sostanziali, API o modelli; confrontare almeno
un uso piccolo, una feature completa, un bug e una sessione ripresa.
