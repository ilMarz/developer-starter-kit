# Primo avvio

1. Controlla `.devkit/import.json`: eventuali `pending_manual_merges` richiedono integrazione
   delle proposte in `.devkit/proposed/` con le istruzioni esistenti. Non sovrascriverle.
2. Apri la cartella progetto in Codex. Usa `dev-workflow` locale. Se esistono omonime globali,
   indica il percorso locale; il client potrebbe mostrare entrambe.
3. Spiega obiettivo, utenti, esempi di risultato, vincoli e ciò che è escluso. Per un repository
   esistente l'agente ispeziona prima implementazione, Git, istruzioni e test.
4. Scegli stack e versioni sulla base del progetto; leggi `PROFILES.md` per il profilo scelto.
   Crea manifest e lockfile adeguati e configura i comandi in `.devkit/project.json`.
   Il bootstrap non ha installato runtime o dipendenze applicative.
5. Se è un progetto nuovo, inizializza Git e registra una baseline quando il contenuto è pronto.
   Controlla diff e segreti prima del commit. Non aggiungere remote o pubblicare senza incarico.
6. Definisci criteri e prima slice, budget e limiti in `.devkit/loop.json`. Configura i ruoli
   in `.devkit/models.json` dopo aver verificato i modelli disponibili nel client.
7. Esegui la prima slice attraverso un comportamento reale, aggiungi i controlli necessari
   a una CI adatta allo stack e registra l'esito in `docs/progress.md`.

Prima del codice l'agente presenta la scheda in `WORKING-AGREEMENT.md`: puoi cambiare
skill, convenzioni, tool, loop, subagenti e modelli. Se hai già indicato cosa vuoi usare
e chiesto di procedere, non serve una nuova conferma. Le scelte del singolo incarico
non diventano automaticamente preferenze permanenti.

La skill `setup-matt-pocock-skills` è inclusa per riconfigurare tracker e layout: il bootstrap
ha già fornito i file locali minimi; non serve rifare il questionario se le convenzioni vanno bene.

## Prompt pronti

**Progetto nuovo**
> Usa $dev-workflow. Obiettivo: [...]. Vincoli: [...]. Risultato di riferimento: [...].
> Prepara specifica, criteri e prima slice. Chiarisci solo le decisioni non ricavabili dal contesto.

**Implementazione autorizzata**
> Implementa la slice [ID] usando $dev-workflow e subagenti. I criteri approvati sono in [file].
> Usa i budget concordati e aggiorna prove e registro. Prosegui fino a completamento o stop motivato.

**Ripresa**
> Riprendi da docs/progress.md. Controlla commit, diff e prove, recupera il piano e il ledger SDD
> se presenti, poi continua il primo task incompleto senza ripetere quelli già verificati.

**Bug**
> Usa $dev-workflow e diagnosing-bugs. Questo input [...] produce [...] ma deve produrre [...].
> Riproduci il caso, correggi entro [...] e verifica originale e regressioni.
