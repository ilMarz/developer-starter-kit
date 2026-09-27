# Raccordi fra skill e client

Le skill vendor sono conservate byte per byte. Queste sono convenzioni locali proposte
per il progetto: non dichiarano che le skill upstream siano state riscritte e non possono
superare istruzioni esplicite dell'utente o vincoli del client.

| Differenza | Regola del kit |
| --- | --- |
| Skill vendor prescrive un passaggio escluso dall'utente | Prevale il subset scelto; adattare la procedura o eseguire direttamente senza invocare skill escluse |
| Matt usa ticket di comportamento; SDD vuole task e file | Derivare un piano esecutivo dai ticket, mantenere ID e criteri; non cambiare la specifica |
| to-tickets usa .scratch di default | Usare il tracker configurato: docs/work, persistente e versionato |
| SDD decide ambiguità; l'utente approva requisiti | Decidere dettagli reversibili nel perimetro; chiedere per criteri, compromessi e ampliamenti |
| Conferme richieste più volte | Riutilizzare decisioni già date; chiedere solo su materiale nuovo non autorizzato |
| Finishing richiede sempre un menu | Eseguire la destinazione già autorizzata; se manca, preparare risultato reviewabile e chiedere |
| Cleanup SDD e worktree | Salvare prima sintesi/prove durevoli; usare strumenti nativi di archiviazione se presenti |
| Richiami superpowers:skill e tool Skill | Risolvere il nome nel file locale .agents/skills; leggere la skill se il client non ha un loader |
| executing-plans citata come alternativa | Non inclusa: usare percorso diretto coordinato del kit, dichiarando assenza di quella skill |
| Matt TDD rinvia refactoring alla review | Usare red/green per il comportamento; refactoring motivato dopo la verifica, con test verdi |
| Matt richiede accordo sulle interfacce di test | Riutilizzare accordo nella specifica; non bloccare per una conferma già registrata |
| Review duplicata | Review per task SDD copre requisiti e qualità; review finale copre integrazione, non ripete inutilmente |
| tdd rinvia alla skill Matt code-review | Quella skill non è inclusa: usare il reviewer di requesting-code-review/SDD per la stessa fase, senza dichiarare di averla eseguita |
| Default modelli della skill | Verificare disponibilità; configurazione ruoli è preferenza, client decide cosa può eseguire |
| Shell setup generici negli esempi | Usare manifest e lockfile reali; pyproject.toml non implica Poetry |

## Portabilità

Il kit non installa plugin, MCP server, credenziali, hook, scheduler o runtime applicativi.
Codex legge le skill locali; per altri client verificare discovery, permessi, tool e metadata.
Se subagenti non disponibili, non fingere separazione: implementare direttamente e riportare
che la review non è indipendente, oppure richiedere un reviewer umano per i rischi che lo esigono.
Se tool nativi per worktree sono disponibili, usarli; Git manuale è fallback.
Un worktree non è una sandbox di esecuzione. Bash/Git servono agli helper SDD.

Le copie omonime globali non sono eliminate. Specificare quelle del progetto quando si
invocano skill; gestire eventuali disabilitazioni globali solo su richiesta dell'utente.
