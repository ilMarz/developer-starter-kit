---
name: dev-workflow
description: Avvia o riprendi una feature, un bugfix o un progetto usando il developer starter kit locale, collegando specifica, slice, implementazione e prove.
---

# Developer workflow

Leggi `AGENTS.md` applicabile e `docs/development/WORKFLOW.md` nel progetto.
Se non esistono, spiega che il kit deve essere importato; non inventare configurazioni.
Leggi `.devkit/project.json` per stato e comandi. La configurazione iniziale contiene
valori null: non sono verifiche superate. Per il primo avvio segui START-HERE.md.

Prima del primo cambiamento sostanziale segui la **scheda di lavoro** in
`docs/development/WORKING-AGREEMENT.md`: presenta il subset suggerito di skill,
convenzioni, tool, delega/loop e modelli effettivamente disponibili, poi lascia
all'utente la scelta. Le indicazioni già date nell'incarico valgono come scelta:
non chiedere una seconda approvazione. Una richiesta esplicita di andare direttamente
al codice o di non usare una skill prevale sul percorso suggerito qui sotto.
Leggi `.devkit/workflow.json` se presente, applicando prima gli override dell'utente
per l'incarico. È una preferenza letta dall'agente, non un controllo del runtime.

Suggerisci il percorso proporzionato alla richiesta, poi usa solo il subset scelto:

- Nuova feature con ambiguità: `grill-with-docs` solo sui punti aperti, poi `to-spec`.
- Specifica già approvata: riprendi quella; `to-tickets` se servono incrementi distinti.
- Slice pronta: piano operativo con `writing-plans` quando l'implementazione ha più passi;
  `using-git-worktrees` secondo il contesto e `subagent-driven-development` se la delega è disponibile e autorizzata.
- Bug: `diagnosing-bugs`, riproduzione osservata, correzione e regressione pertinente.
- Modifica piccola e chiara: esegui direttamente con verifica proporzionata.

Per test-first usa `tdd`; per decisioni sulle interfacce usa `codebase-design`.
Suggerisci review, `verification-before-completion` e, quando serve integrazione Git,
`finishing-a-development-branch`. L'utente può scegliere una verifica diretta senza
queste skill; riporta comunque cosa è stato verificato. Non duplicare le review SDD.
Non invocare indirettamente una skill esclusa tramite un'altra: segnala la dipendenza
e adatta il percorso. Esempio: senza `grilling`, chiarisci soltanto le ambiguità essenziali;
senza subagenti, non avviare SDD fingendo una review indipendente.

Le skill incluse sono in `.agents/skills/<nome>/SKILL.md`. Se il client non espone
un tool Skill, leggi il file e le sole risorse richieste. Il prefisso `superpowers:`
nei testi upstream indica il nome omonimo in questa directory; non richiede un
secondo plugin. `grill-with-docs` richiede anche `grilling` e `domain-modeling`.
I percorsi relativi interni alle skill si risolvono dalla directory della skill.
Non sostituire una skill locale con una globale omonima senza confrontare le versioni.

Per vincoli dei tool, conflitti fra procedure, registro durevole e importazioni
su progetti esistenti consulta `docs/development/COMPATIBILITY.md`.
Non delegare da un subagente implementatore: il coordinatore assegna review e task.
Il task corrente e le autorizzazioni già date prevalgono sulle convenzioni del kit.

Concludi ogni slice con criteri verificati, comandi realmente eseguiti, limiti,
commit o diff e prossimo passo nel registro `docs/progress.md`.
