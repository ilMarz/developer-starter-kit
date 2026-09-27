# Confronto con kit pubblici

Ricerca del **27 settembre 2026**. Scopo: individuare pratiche riutilizzabili per questo
starter, mantenendo Matt Pocock per specifiche, slice, TDD e debugging, Superpowers
locale per esecuzione isolata/review e il bootstrap conservativo del kit.
Non è una classifica di efficacia: stelle e attività mostrano diffusione e manutenzione,
non correttezza, sicurezza o produttività misurata.

## Snapshot verificata

Metadati letti dalle API GitHub: `GET /repos/{owner}/{repo}` e
`GET /repos/{owner}/{repo}/commits/{default_branch}`. Le date sono quelle del committer
del commit in testa al branch predefinito, in UTC; non sono date di release.
Conteggi mutevoli, osservati durante questa ricerca. I link ai commit fissano il codice;
i link API restano dinamici.

| Repository / API primaria | Stelle | Licenza verificata | Ultimo commit osservato | Stato |
| --- | ---: | --- | --- | --- |
| [github/spec-kit](https://api.github.com/repos/github/spec-kit) | 139.060 | MIT | [c00dc055](https://github.com/github/spec-kit/commit/c00dc0551583428a10a94443c58c6a41e5e0138c), 25 settembre 2026 | Non archiviato |
| [bmad-code-org/BMAD-METHOD](https://api.github.com/repos/bmad-code-org/BMAD-METHOD) | 53.535 | MIT con avviso separato sui marchi¹ | [5e33d3c0](https://github.com/bmad-code-org/BMAD-METHOD/commit/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb), 25 settembre 2026 | Non archiviato |
| [gsd-build/get-shit-done](https://api.github.com/repos/gsd-build/get-shit-done) | 64.450 | MIT (API) | [bdcaab2c](https://github.com/gsd-build/get-shit-done/commit/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815), 31 maggio 2026 | **Archiviato**, README rimanda a GSD Core |
| [open-gsd/gsd-core](https://api.github.com/repos/open-gsd/gsd-core) | 9.893 | MIT | [84ed9b84](https://github.com/open-gsd/gsd-core/commit/84ed9b843d9c383e46144931328676fef929a34c), 27 settembre 2026 | Successore indicato, non archiviato |
| [buildermethods/agent-os](https://api.github.com/repos/buildermethods/agent-os) | 5.452 | MIT (API) | [475b0cac](https://github.com/buildermethods/agent-os/commit/475b0cac4c7c5cf2336ad5a663b691a6d3415e05), 29 agosto 2026 | Non archiviato |

¹ L'API BMAD restituisce `NOASSERTION`; il [testo LICENSE letto](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/LICENSE)
contiene MIT e un avviso sui marchi. Non dedurre la licenza solo dal badge o dal campo API.

## Cosa offrono e cosa selezionare

Le capacità sotto sono documentate nelle fonti, non provate eseguendo i framework.
Conflitti e scelte di adozione sono valutazioni nostre.

| Sistema | Evidenza e punto forte | Cosa adottare nel kit | Sovrapposizione da evitare |
| --- | --- | --- | --- |
| **Spec Kit** | Distingue specifica, piano, task e convergenza; offre anche percorsi separati per bug e valutazione di idee. L'analisi confronta requisiti, piano e task, cercando ambiguità, incoerenze e buchi di copertura. [README](https://github.com/github/spec-kit/blob/c00dc0551583428a10a94443c58c6a41e5e0138c/README.md), [analyze](https://github.com/github/spec-kit/blob/c00dc0551583428a10a94443c58c6a41e5e0138c/templates/commands/analyze.md) | Una verifica esplicita requisito → slice/task → evidenza prima della chiusura; distinguere copertura documentale da comportamento verificato. | Installare l'intero sistema aggiungerebbe un secondo router, artefatti e ciclo di implementazione sopra Matt + Superpowers. La sua “constitution” non deve diventare una seconda autorità concorrente con AGENTS e criteri approvati. |
| **BMAD Method** | Pianificazione proporzionata: modifica piccola, sessione Build, epic o progetto. Documenti di prodotto e architettura servono quando occorre coordinare più parti; le unità implementate vanno verificate insieme. [README](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/README.md), [planning path](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/docs/plan/choose-a-planning-path.md) | Attivare ruoli e documenti solo per una lacuna concreta; aggiungere un controllo integrato alla fine di più slice. | Un PRD completo e molti ruoli per ogni fix costerebbero contesto e interazioni senza beneficio dimostrato. Il suo backlog e loop duplicano quelli del kit. |
| **GSD / GSD Core** | Il [vecchio README](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md) rimanda a `open-gsd/gsd-core`. Il [README del successore](https://github.com/open-gsd/gsd-core/blob/84ed9b843d9c383e46144931328676fef929a34c/README.md) descrive fasi Discuss/Plan/Execute/Verify/Ship, contesti separati e stato durevole (`STATE.md`, `CONTEXT.md`). | Brief compatti per esecutore/reviewer e ripresa da stato ed evidenze, già coerenti con l'impostazione locale. Misurare la qualità della ripresa. | Non sommare il suo orchestratore e le sue ondate parallele a SDD locale. Le dimensioni di contesto dichiarate nel README non garantiscono quelle del runtime disponibile. Il README richiede l'installer per adattare i runtime: copiare singoli comandi non certifica compatibilità. |
| **Agent OS** | Estrae convenzioni specifiche dal codice, le documenta in modo breve e carica quelle pertinenti tramite indice. [README](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/README.md), [discover-standards](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/commands/agent-os/discover-standards.md), [inject-standards](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/commands/agent-os/inject-standards.md) | Un indice leggero delle convenzioni osservate, con origine nel codice, motivazione ed eccezioni. Caricamento per pertinenza. | Non trasformare ogni pattern esistente in regola obbligatoria. I comandi letti assumono `AskUserQuestion` e percorsi specifici: non sono skill Codex portabili senza adattamento. Evitare un secondo archivio di standard parallelo ad ADR e contesto del progetto. |

## Decisione per questo starter

Conservare **un solo workflow di ingresso**. Questi sistemi sono alternative complete o
fonti di pratiche, non dipendenze da impilare. Preferire tre miglioramenti circoscritti:

1. Controllare la coerenza tra requisiti, slice e prove, ispirandosi a Spec Kit.
2. Dimensionare il processo al rischio e verificare l'integrazione fra slice, come suggerisce BMAD.
3. Mantenere contesto breve, durevole e selettivo, prendendo spunto da GSD e Agent OS.

Sono raccomandazioni, non dichiarazioni di funzionalità già implementate. Un'eventuale
importazione di codice o testo richiede snapshot, licenza, diff e prove come le altre
dipendenze del kit. In questa ricerca non sono stati installati né eseguiti framework,
installer, hook o istruzioni contenute nelle fonti.

Per decidere se una pratica migliora davvero il kit, confrontare il workflow attuale e
quello modificato su modifica piccola, feature con più slice, bug e ripresa di sessione:
stessi criteri, difetti sfuggiti, interventi richiesti, tempo/costo e integrità del repository.
Non selezionare un framework in base al solo numero di stelle.
