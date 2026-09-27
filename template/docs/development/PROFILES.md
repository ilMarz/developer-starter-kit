# Profili di progetto

Il profilo scelto è in .devkit/project.json. Applicare solo quello rilevante, usando
versioni correnti verificate al setup. Nessun framework obbligatorio.

| Profilo | Setup da completare |
| --- | --- |
| generic | Runtime, manifest/lockfile, comandi install/lint/test/build pertinenti, prima prova osservabile |
| python | Versione Python, ambiente virtuale, pyproject, gestore e lock coerenti, pytest o test runner esistente, lint/typecheck se utili |
| typescript | Runtime Node, package manager e lockfile, tsconfig, lint, test e build; browser/e2e se c'è UI |
| ai | Tutto quanto richiesto dallo stack, più rubriche, dataset separati, trace redatte, errori/non valutabile, prove live distinte dai double |

Per tutti: setup riproducibile da checkout pulito; controllo segreti e dipendenze;
CI con test adatti alla modifica; osservabilità e procedure di rilascio proporzionate al prodotto.
Blocchi CI e branch protection sono decisioni di progetto, non abilitate dal kit.
Per persistenza/migrazioni verificare compatibilità, dati di prova, backup/ripristino fattibile.
Per web includere accessibilità e stati vuoti/errore; per API contratti ed errori; per job
idempotenza, timeout, retry limitati e riconciliazione. Attivare questi controlli dove pertinenti.

Per prodotti AI: separare eval del prodotto dai test del software e dagli eval delle skill.
Usare casi positivi, negativi, incompleti e avversariali; sviluppo/calibrazione/test separati.
I grader semantici richiedono calibrazione e controlli umani; misurare falsi pass, errori,
copertura e costo totale. Non usare il testo 'completato' dell'agente come prova del risultato.
