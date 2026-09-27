# Developer Starter Kit

Versione **0.2.0** · ricerca del 27 settembre 2026.
Kit autonomo per sviluppare con agenti AI: 17 skill, template per specifiche/ADR/slice,
loop di sviluppo, scelta del subset e dei modelli, importazione conservativa e verifiche.
Repository autonomo: puoi spostare questa cartella. Non dipende da altri progetti.

## 1. Apri il terminale nella cartella del kit

Per scaricarlo su un altro computer con GitHub già autenticato:

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git
cd developer-starter-kit
```

Il repository è privato: l’account usato deve avere accesso. Se hai già il kit in locale,
non clonarlo di nuovo.

Tutti i comandi Python sotto partono dalla cartella che contiene questo README.
Se sei nella directory che contiene il kit:

```bash
cd developer-starter-kit
```

Controlla che Python sia disponibile e leggi i parametri supportati:

```bash
python3 --version
python3 tools/bootstrap.py --help
```

Serve Python **3.9 o successivo**. Per gli helper di sviluppo Superpowers servono anche
Git e Bash. Il bootstrap usa soltanto la libreria standard di Python: niente `pip install`
o `npm install` necessari per importare il kit.

## 2. Importa il kit

Gli esempi usano `$HOME/Progetti/…`: il terminale espande `$HOME` alla tua cartella utente.
Puoi sostituire la destinazione con un altro percorso. Mantieni le virgolette se contiene spazi.
La destinazione deve essere esterna alla cartella del kit.

### Nuovo progetto — stack ancora da scegliere

Prima guarda cosa verrebbe copiato, senza scrivere nulla:

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-progetto" --name mio-progetto --profile generic --dry-run
```

Poi importa davvero:

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-progetto" --name mio-progetto --profile generic
```

La cartella viene creata se manca. Deve essere vuota o inesistente per questo comando.
Vengono copiati skill, template e configurazioni; nessuna applicazione è ancora implementata.

### Nuovo progetto Python

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-backend" --name mio-backend --profile python --dry-run
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-backend" --name mio-backend --profile python
```

### Nuovo progetto TypeScript

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-ecommerce" --name mio-ecommerce --profile typescript --dry-run
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-ecommerce" --name mio-ecommerce --profile typescript
```

### Nuovo prodotto che usa modelli AI a runtime

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-assistente" --name mio-assistente --profile ai --dry-run
python3 tools/bootstrap.py --target "$HOME/Progetti/mio-assistente" --name mio-assistente --profile ai
```

`ai` riguarda il prodotto che stai costruendo. Lo sviluppo assistito da AI è disponibile
in tutti i profili.

### Progetto già esistente

Sostituisci `ecommerce-esistente` con la cartella reale del tuo progetto:

```bash
python3 tools/bootstrap.py --target "$HOME/Progetti/ecommerce-esistente" --name ecommerce-esistente --profile generic --existing --dry-run
python3 tools/bootstrap.py --target "$HOME/Progetti/ecommerce-esistente" --name ecommerce-esistente --profile generic --existing
```

`--existing` permette una destinazione non vuota, **non autorizza sovrascritture**.
I file di istruzioni preesistenti restano intatti; le integrazioni proposte vengono salvate
in `.devkit/proposed/`. Il programma elenca quelle da unire prima di usare il workflow.
Altri file differenti in conflitto bloccano l'import prima delle scritture. File identici
vengono riutilizzati. Il codice applicativo esistente viene conservato.

### Tutti i parametri di bootstrap

| Parametro | Obbligatorio | Default | Significato |
| --- | --- | --- | --- |
| `--target PERCORSO` | Sì | — | Cartella del progetto destinatario; relativa alla directory corrente o assoluta |
| `--name NOME` | Sì | — | Nome registrato nella configurazione; non rinomina la cartella |
| `--profile generic` | No | `generic` | Nessuno stack ancora scelto / stack diverso |
| `--profile python` | No | — | Indica un progetto Python |
| `--profile typescript` | No | — | Indica un progetto TypeScript |
| `--profile ai` | No | — | Indica un prodotto con modelli AI a runtime |
| `--existing` | No | Disattivato | Consente l'importazione conservativa in una cartella non vuota |
| `--dry-run` | No | Disattivato | Verifica e mostra il piano di copia senza creare cartelle o file |
| `--help` / `-h` | No | — | Mostra l'aiuto del comando |

Scegli **un solo valore** di `--profile`. Il profilo viene registrato in `.devkit/project.json`:
serve all'agente per scegliere la guida al setup. **Le skill copiate sono le stesse**;
non installa runtime, framework, dipendenze o servizi e non configura da solo i test.

Il bootstrap non inizializza Git, non crea commit/remote/PR e non esegue workflow applicativi.
Un secondo import identico con `--existing` è consentito. Dopo personalizzazioni può
fermarsi per conflitti: non usarlo come comando per aggiornare un progetto alla nuova versione.

## 3. Apri il progetto in Codex

Apri la cartella indicata in `--target`, non la cartella del kit. I messaggi seguenti
vanno nella **chat di Codex**, non nel terminale.

### Partire da un'idea

```text
Usa $dev-workflow. Voglio realizzare un ecommerce per prodotti artigianali.
Verifica l'ambiente, chiarisci i requisiti mancanti e prepara la prima slice verificabile.
Prima del codice proponi skill, convenzioni, tool, loop/subagenti e modelli che useresti.
```

### Modificare un progetto esistente

```text
Usa $dev-workflow. Voglio aggiungere codici sconto percentuali con scadenza.
Integra eventuali proposte di istruzioni del kit con quelle già presenti senza sostituirle.
Studia checkout e test esistenti, preserva lo stack e proponi criteri e subset di lavoro.
Non modificare la produzione.
```

### Accettare il metodo proposto

```text
Procedi con il subset proposto per questa slice. Usa i criteri approvati e il budget concordato.
```

### Cambiare skill, convenzioni, loop e modelli

```text
Per questo incarico salta to-spec: i requisiti sono già nel ticket.
Non usare subagenti né agentic loop: implementa direttamente e fai la verifica concordata.
```

```text
Usa il loop con massimo due tentativi di correzione. Prima del dispatch mostrami i modelli
realmente disponibili e proponi quale usare per implementazione e review.
```

```text
Per implementare usa [ID modello disponibile] e per la review usa [altro ID disponibile].
Non usare la skill [nome]. Questa preferenza vale solo per questo incarico.
```

Le parentesi quadre sono valori da sostituire: il kit non fissa nomi di modelli universali.
Se hai già scelto metodo e chiesto di procedere, l'agente non richiede una seconda conferma.
Puoi anche chiedere «vai direttamente al codice, senza skill». Le esclusioni valgono anche
per i subagenti e le dipendenze indirette; l'agente riporta comunque le verifiche reali e i limiti.

### Riprendere il giorno dopo

```text
Usa $dev-workflow. Riprendi da docs/progress.md, controlla codice, commit e prove.
Mantieni le scelte già concordate e continua il primo task incompleto.
```

### Correggere un bug

```text
Usa $dev-workflow e diagnosing-bugs. Il checkout perde lo sconto quando cambio quantità.
Riproduci il problema e proponi una correzione con verifica del caso originale e delle regressioni.
```

## 4. Cercare novità e aggiornare il kit

Apri **la cartella del kit** in Codex e scrivi in chat:

```text
Usa $update-devkit. Cerca aggiornamenti e nuove skill, strumenti e convenzioni che
potrebbero migliorare questo kit. Proponi cosa integrare, perché e come verificarlo.
```

La ricerca include novità fuori dall'inventario attuale. Salva proposte con ID in
`docs/updates/`; in questa modalità non cambia le skill operative o le dipendenze.
Può anche suggerire di rimuovere procedure inutili oppure concludere che non ci sono
novità abbastanza utili. Non serve nominare una tecnologia in anticipo.

Dopo aver letto il report, seleziona in chat la proposta e il suo percorso reale:

```text
Usa $update-devkit. Applica U-01 del report [percorso del report].
Mantieni le personalizzazioni, esegui le verifiche pertinenti e lascia U-02 rimandata.
```

Non esiste un comando shell di auto-update: la skill coordina la ricerca e le modifiche
attraverso i tool dell'agente. Non è un monitoraggio in background. I progetti già importati
non cambiano da soli; per ciascuno si confronta e si integra il delta autorizzato.

La skill nel repository è esposta da `.agents/skills/update-devkit`, link relativo a
`skills/update-devkit`. Se non appare nel client, chiedi:

```text
Leggi skills/update-devkit/SKILL.md e applicala per cercare novità utili a questo kit.
```

Nei progetti importati le skill sono directory normali in `.agents/skills/`. Se hai copie
globali omonime, il client potrebbe mostrarle entrambe: indica la copia del progetto.

## 5. Comandi di verifica — nel terminale del kit

Controllare che le 15 skill esterne corrispondano alle snapshot registrate:

```bash
python3 tools/verify.py
```

Eseguire i test del bootstrap:

```bash
python3 -m unittest discover -s tests -v
```

Vedere quali file sono cambiati in un progetto rispetto alla copia importata:

```bash
python3 tools/verify.py --project "$HOME/Progetti/mio-progetto"
```

Aiuto del verificatore:

```bash
python3 tools/verify.py --help
```

| Parametro/esito | Significato |
| --- | --- |
| Nessun parametro | Verifica gli hash delle skill esterne distribuite nel kit |
| `--project PERCORSO` | Confronta i file registrati in `.devkit/import.json` con il progetto attuale |
| `--help` / `-h` | Mostra l'aiuto |
| Exit code `0` | Controllo completato senza differenze rilevate |
| Exit code `1` | Il progetto contiene file modificati o mancanti rispetto all'import |
| Exit code `2` | Controllo/import non eseguibile, conflitti oppure integrità vendor fallita |

**Integrità** significa confronto delle impronte digitali dei file: conferma che sono le
copie previste, non che siano buone o sicure. Il **drift** segnala differenze dopo l'import:
spesso sono personalizzazioni intenzionali. Il verificatore non le corregge e non prova
che l'applicazione funzioni. I test della tua applicazione saranno configurati al setup.

## Cosa configuriamo nel progetto

| File importato | Contenuto |
| --- | --- |
| `.devkit/project.json` | Nome, profilo e comandi setup/lint/typecheck/test/build/e2e da verificare |
| `.devkit/workflow.json` | Preferenze su skill, convenzioni, tool, esecuzione e scheda iniziale |
| `.devkit/models.json` | Modelli e reasoning per ruolo, da scegliere fra quelli disponibili |
| `.devkit/loop.json` | Budget e condizioni di stop; valori iniziali proposti, non già approvati |
| `AGENTS.md` | Istruzioni brevi per l'agente |
| `CONTEXT.md` | Glossario del dominio |
| `docs/progress.md` | Stato durevole, prove, limiti e prossimo passo |
| `docs/development/templates/` | Specifica, ADR, slice, piano, report ed eval da usare quando necessari |

Puoi esprimere preferenze in chat: non devi editare JSON a mano. Le scelte del singolo
incarico non diventano permanenti se non lo chiedi. Questi file sono letti dall'agente:
non sono un runtime, non abilitano un provider e non impongono da soli limiti di spesa.

## Contenuto e documentazione

- **Matt Pocock (9):** grilling, domain-modeling, grill-with-docs, to-spec, to-tickets,
  codebase-design, tdd, diagnosing-bugs, setup-matt-pocock-skills.
- **Superpowers (6):** using-git-worktrees, writing-plans, subagent-driven-development,
  requesting-code-review, verification-before-completion, finishing-a-development-branch.
- **Originali (2):** dev-workflow, update-devkit.

Le copie esterne e le licenze sono conservate con hash in `skills.lock.json`. Le quattro
snapshot locali Superpowers non hanno un commit upstream attribuito: la provenienza è esplicita.
Le skill del client skill-creator/skill-installer/openai-docs non sono dipendenze del kit.

- [Guida di primo avvio](template/docs/development/START-HERE.md)
- [Scheda e scelta del subset](template/docs/development/WORKING-AGREEMENT.md)
- [Agentic loop e modelli](template/docs/development/AGENTIC-LOOP.md)
- [Raccordi fra procedure](template/docs/development/COMPATIBILITY.md)
- [Fonti e pratiche](docs/SOURCES.md)
- [Confronto Spec Kit, BMAD, GSD e Agent OS](docs/ECOSYSTEM.md)
- [Verifiche effettive e limiti](docs/VALIDATION.md)
- [Changelog](CHANGELOG.md)
- [Licenze e provenienza](THIRD_PARTY_NOTICES.md)

La CI in `.github/workflows/check-kit.yml` è predisposta per il futuro repository GitHub;
non è stata eseguita sul servizio. Non sono impostati remote, pubblicazioni o licenza del
prodotto che creerai. Usa il bootstrap per importare solo il materiale necessario, anziché
copiare tutto il repository del kit dentro una nuova applicazione.
