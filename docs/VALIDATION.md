# Verifica del kit

Verificato il 27 settembre 2026 su macOS con Python locale.

- `python3 tools/verify.py`: PASS, 15 snapshot vendor corrispondono agli hash registrati.
- `python3 -m unittest discover -s tests -v`: PASS, 12 test. Import in directory con spazi,
  dry-run senza scritture, conservazione file utente, proposte di merge, blocco preventivo
  dei conflitti, idempotenza, symlink interni rifiutati, drift e vendor alterato rilevati.
- Esecuzione reale dell'helper SDD task-brief sul template del piano in un repository Git
  temporaneo: PASS, task estratto e scratch escluso da Git.
- Controllo strutturale di nome/descrizione frontmatter e directory sulle 17 skill: PASS.
- Il validatore ufficiale quick_validate.py è stato tentato ma non eseguito: PyYAML assente
  nei due runtime Python disponibili. Nessuna installazione globale effettuata. Il controllo
  strutturale sopra è più limitato e non viene presentato come equivalente.
- Review indipendente: nessun difetto bloccante riprodotto; ulteriori prove di trasferibilità,
  repeat import e conservazione ledger. Vedi `INDEPENDENT-REVIEW.md` per il protocollo.

Durante i test è stato corretto un rifiuto improprio dei percorsi temporanei macOS:
la radice scelta viene risolta, mentre i symlink interni alla destinazione sono rifiutati.

## Limiti

Le prove di ripresa, modello indisponibile e budget esaurito includono valutazioni ragionate
documentate, non una certificazione del comportamento live degli agenti. La suite in `evals/`
resta da eseguire sistematicamente su progetti reali e con misure comparabili.
Nessun provider chiamato; nessuna prova end-to-end di un prodotto generato. Nessuna garanzia
di supporto ad altri client. La CI GitHub ha superato verifica snapshot e 12 test su Linux con Python 3.11 e 3.13
alla revisione `08698acd31f5f6bd48404a78bb901e3657e6549c`: [run verificata](https://github.com/ilMarz/developer-starter-kit/actions/runs/36317957804).
L'import è progettato per una singola esecuzione alla volta: non fornisce transazioni
filesystem o protezione da processi concorrenti che cambiano i percorsi durante la copia.
Modelli e budget JSON sono istruzioni operative, non enforcement tecnico di spesa o permessi.

## Aggiornamento 0.2.0

Ripetuti con esito positivo i 12 test e la verifica dei 15 snapshot vendor dopo il
trasferimento nella directory autonoma. Le due skill originali sono dev-workflow e
update-devkit. Il collegamento relativo .agents/skills/update-devkit è presente.
Il README documenta i parametri reali del bootstrap e separa comandi terminale da
prompt in chat. La scelta del subset prima delle modifiche è descritta nel working
agreement; la sua efficacia operativa resta da valutare con agenti su casi reali.
