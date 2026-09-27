# Metodo operativo

## Scegliere la quantità di processo

- Refuso/configurazione piccola e reversibile: diff mirato e verifica pertinente.
- Bug: riproduzione, causa verificata, correzione, originale e regressione.
- Feature con più passi: specifica, slice, piano operativo, implementazione e review.
- Decisione costosa o controversa: analisi delle alternative e ADR. Non creare ADR per routine.

## Dal problema al software

1. **Comprendere**: fatti dal codice e fonti; domande sulle sole decisioni aperte. Distinguere
   osservato, ipotizzato e proposto. Specifica con esempi, criteri negativi e fuori perimetro.
2. **Scegliere le interfacce di verifica**: comportamento osservabile e risultati attesi
   indipendenti dall'implementazione. Riutilizzare quelli già approvati.
3. **Slice verticali**: ciascuna attraversa i livelli necessari a un comportamento dimostrabile.
   Non costruire prima tutti i modelli, poi tutti i servizi, poi tutti i test.
   Le grandi migrazioni possono usare expand → migrazione → contract, mantenendo compatibilità.
4. **Piano**: derivare task dalle slice. Specifica = cosa e perché; piano = come e quali file.
   Verificare conflitti di interfacce/dipendenze prima di assegnare task. Usare intestazioni
   `### Task 1: ...` compatibili con task-brief SDD. Il template è in templates/plan.md.
5. **Esecuzione**: ambiente controllato, baseline, test significativi, cambi piccoli,
   loop definito in AGENTIC-LOOP.md. Niente subagenti obbligatori per lavoro minuscolo.
6. **Review**: controllare conformità ai criteri, correttezza, regressioni, sicurezza pertinente,
   migrazioni e operatività. Il reviewer deve poter contestare piano e implementazione con prove.
7. **Consegna**: verifiche sul risultato finale, limiti espliciti, documenti aggiornati,
   commit/diff e integrazione nella destinazione autorizzata. Nessun deploy implicito.

## Coerenza e convenzioni osservate

Prima di iniziare e prima di chiudere una feature, confrontare criteri della specifica,
slice/task e prove: ogni criterio richiesto deve avere una verifica identificabile; un
documento che lo cita non dimostra che il comportamento funzioni. Verificare anche
il percorso integrato quando più slice collaborano.

Nei progetti esistenti, registrare solo le convenzioni utili realmente osservate in un
indice `docs/standards.md`: ambito, file/simbolo di origine, motivazione ed eccezioni.
Crearlo quando emergono convenzioni da riusare, senza copiare interi manuali. Un pattern
esistente può essere un debito tecnico: non promuoverlo automaticamente a regola.

## Definition of ready

Obiettivo e criteri utilizzabili; dipendenze risolte o esplicite; superficie di test;
ambiente e permessi; budget e modalità concordati. Un task bloccato non è pronto.

## Definition of done

Comportamento richiesto osservato; casi originali, negativi e regressioni pertinenti;
review affrontata; errori residui e verifiche mancanti espliciti; docs/ADR aggiornati se
necessario; log senza segreti; destinazione e attivazione coerenti con le autorizzazioni.
Una feature non è done se manca una prova essenziale. Può essere candidata con limite dichiarato.

## Memoria e contesto

`docs/progress.md` conserva sintesi e link a prove, commit e decisioni. Il ledger SDD
in `.superpowers/sdd/` è scratch ignorato da Git: recupera il lavoro durante una sessione,
ma non è archivio sufficiente. Prima di pulizia/handoff trasferire le evidenze utili redatte
in `docs/reports/`. Non copiare transcript integrali o segreti nel repository.
