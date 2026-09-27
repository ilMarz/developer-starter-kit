# Review indipendente del kit

Data: 27 settembre 2026. Perimetro: kit 0.1.0 presente sul filesystem; nessuna revisione Git disponibile nella directory esaminata. Review svolta da un agente separato dall'autore, senza altri subagenti, provider esterni o modifiche a progetti dell'utente.

## Esito

Nessun difetto bloccante riprodotto nel bootstrap o nei raccordi esaminati. L'import offline è utilizzabile come snapshot di procedure e template. Non è stata dimostrata l'efficacia end-to-end di un team di agenti né l'applicazione automatica dei budget/modelli: il kit dichiara correttamente questi limiti.

## Esecuzioni effettive

- `PYTHONDONTWRITEBYTECODE=1 python3 tools/verify.py`: exit 0, 15 skill vendor verificate.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`: exit 0, 12 test superati. Copertura osservata: dry run, import nuovo/esistente, preservazione, conflitti prima delle scritture, idempotenza, configurazione modificata, symlink, ostacoli nel percorso, drift, helper SDD e vendor alterato.
- Copia dell'intero kit in directory temporanea esterna, import da tale copia in un progetto temporaneo con spazi nel percorso: exit 0, 70 file importati. `AGENTS.md` originale conservato e proposta separata registrata. Nessuna dipendenza dalla directory originaria necessaria per l'import.
- Secondo import della medesima fixture con `--existing`: exit 0, zero file nuovi; confronto byte per byte invariato, incluse le proposte per istruzioni preesistenti.
- Git inizializzato e baseline committata solo nella fixture temporanea. Esecuzione reale di `sdd-workspace` prima con percorso assoluto, poi relativo dello stesso piano: stesso workspace; ledger con Task 1 completo e Task 2 in correzione conservato.
- Correzione reale `smal` → `small` nel README della fixture: `git diff --name-only` restituisce solo `README.md`; numstat 1/1. Verifica import exit 0 perché README non è un file gestito: comportamento coerente con il perimetro dichiarato del verificatore.

Le fixture sono state eliminate automaticamente. Nessun workflow applicativo, servizio o provider è stato chiamato. L'esecuzione dell'helper verifica la persistenza del file, non prova che un agente riprenda correttamente il lavoro.

## Valutazione ragionata delle procedure

Queste sono simulazioni a tavolino di decisioni, distinte dalle esecuzioni sopra. Non sono benchmark comportamentali live.

| Richiesta / stato realistico | Percorso verificato nel testo | Decisione della simulazione |
| --- | --- | --- |
| «Riprendi»: Task 1 completato con commit, Task 2 in review | START-HERE, prompt Ripresa; WORKFLOW, memoria; SDD, Setup | Controllare Git e prove, recuperare il ledger del piano corretto, proseguire Task 2; nessun nuovo dispatch di Task 1. Il workspace relativo/assoluto è stato anche verificato con lo script. |
| «Correggi questo refuso nel README» | dev-workflow righe 13–24; WORKFLOW, quantità di processo | Modifica diretta e controllo diff; nessuna intervista, ADR o delega necessaria. Eseguito anche un diff minimo nella fixture, senza considerarlo una prova live della selezione delle skill. |
| Reviewer configurato con ID inesistente, fallback non autorizzato | AGENTIC-LOOP righe 45–55; models.json | Verificare capacità del client, non dichiarare un dispatch riuscito, registrare il limite e attendere scelta. Se il fallback ereditato è già autorizzato, usarlo dichiarando il modello effettivo. Nessuna API invocata nella review. |
| Due tentativi autorizzati, secondo ancora fallito | AGENTIC-LOOP righe 16–30; AGENTS, autonomia; loop.json | Conservare candidato/prove e fermarsi, senza terzo tentativo. La regola locale del limite più restrittivo prevale sul cap vendor SDD di cinque round. Non segnare completato il requisito fallito. |
| Specifica approvata con due comportamenti indipendenti | WORKFLOW; template spec/slice/plan; issue-tracker; COMPATIBILITY | Derivare incrementi verticali e piano con ID/criteri mantenuti; scrivere ticket in docs/work, non nella scratch upstream. ADR solo per decisioni materiali. |

Le differenze delle skill vendor sono rilevanti: SDD propone rulings, cinque fix e scelte di modello; i raccordi locali preservano criteri approvati, budget più restrittivo e capacità reali del client. Chi usa direttamente la sola skill vendor senza leggere le istruzioni del progetto non sta seguendo il workflow del kit.

## Limiti e verifica successiva

Nessun finding correttivo obbligatorio emerso nel perimetro verificato. Rimangono da eseguire i casi di `evals/scenarios.md` in un vero client con discovery locale e dispatch autorizzati, registrando revisioni, modello effettivo, prompt, risultati e consumo. In particolare ripresa dopo compaction, modello indisponibile e stop a budget devono restare **non verificati live** fino a quelle prove. Questa review non certifica compatibilità universale, qualità del software futuro o limiti rigidi di spesa.
