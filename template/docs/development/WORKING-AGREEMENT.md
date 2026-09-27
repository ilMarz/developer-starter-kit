# Scheda di lavoro e subset scelto dall'utente

Prima della prima implementazione o modifica sostanziale di un incarico, mostra
una proposta breve del metodo che intendi usare. È una scelta di lavoro, non
un'autorizzazione a effetti esterni. Durante preparazione e ricerca puoi leggere
codice, verificare fatti e preparare la proposta senza modificare il prodotto.

## Scheda suggerita

> **Obiettivo:** aggiungere i codici sconto al checkout.
> **Skill:** to-spec per i criteri ancora da chiarire; tdd per i test; requesting-code-review
> per una review separata. Nessuna intervista completa se la specifica è già approvata.
> **Convenzioni:** una slice verificabile; ADR solo se emerge una decisione significativa;
> aggiornamento del registro.
> **Tool:** lettura/ricerca file, terminale, Git e test runner esistente; browser solo se
> disponibile e necessario per verificare il checkout.
> **Esecuzione:** propongo loop limitato a implementazione, prove e correzioni con budget
> da concordare; un implementatore e un reviewer se autorizzi subagenti.
> **Modelli:** modello corrente oppure gli ID disponibili che propongo per ciascun ruolo.
> **Scelta:** procediamo così, modifichi il subset oppure preferisci implementazione diretta?

Adatta la scheda al task: non è un elenco obbligatorio di strumenti da eseguire.
Nomina soltanto tool e modelli disponibili verificati; per capacità mancanti indica
la proposta come da configurare. Un'etichetta 'modello forte' non è una selezione effettiva.

## Come si sceglie

L'utente può rispondere in linguaggio naturale, senza editare JSON:

- «Procedi così».
- «Salta to-spec: i requisiti sono già nel ticket».
- «Niente skill o subagenti, vai direttamente all'implementazione».
- «Usa il loop, ma fermati dopo due tentativi di correzione».
- «Usa [ID disponibile] per implementare e [altro ID] per la review».
- «Niente browser; verifica dalla CLI».
- «Questa volta non voglio ADR; conserva la motivazione nel report».

Se la richiesta iniziale contiene già le scelte e l'istruzione di procedere, riassumile
brevemente e lavora. Non introdurre una nuova attesa di conferma. Se chiede solo una
proposta, oppure non ha scelto come eseguire una modifica sostanziale, presenta la scheda
e attendi la scelta prima delle modifiche dipendenti. Silenzio o tempo trascorso non sono
un'accettazione. Per refusi e interventi minimi chiaramente richiesti basta una riga
di metodo proporzionato e l'esecuzione, senza questionario.

## Persistenza e precedenza

Le preferenze di progetto stanno in `.devkit/workflow.json`; i ruoli/modelli in
`.devkit/models.json`; i budget in `.devkit/loop.json`. I file iniziali sono proposte.
Registra le scelte dell'incarico nel piano o nel registro prima di eseguirle. Aggiorna
le preferenze permanenti solo se l'utente dice che valgono anche per gli incarichi futuri.
Una scelta per 'questa volta' non cambia automaticamente il default del progetto.

La gerarchia operativa è: istruzioni del client e autorizzazioni applicabili, richiesta
attuale dell'utente, preferenze già concordate, suggerimenti del kit. Il kit non può
rendere obbligatoria una skill rifiutata dall'utente. Non riaprire la stessa scelta a
ogni task, compaction o passaggio fra agenti; ricostruiscila dal registro.

La disattivazione di una skill elimina quella procedura, non permette di inventare
risultati. Se una scelta impedisce una verifica essenziale, spiega il limite e concorda
un'alternativa; non indebolire autonomamente il criterio di accettazione.
Senza loop, esegui il cambiamento e la verifica concordati e riporta l'esito; niente
cicli aperti di correzione/escalation. Senza subagenti, dichiara la review diretta.

## Dipendenze e cambi di metodo

Trasmetti ai subagenti anche esclusioni, modelli e budget. Un'istruzione vendor non
riattiva skill o tool esclusi. Se un workflow dipende da una skill disabilitata,
adattalo oppure proponi un'alternativa prima di eseguirlo.
Chiedi una nuova scelta solo per cambiamenti materiali: modello non disponibile senza
fallback concordato, nuovi effetti/tool, ampliamento dello scope o budget esaurito.
Il JSON non blocca tecnicamente tool o spesa: i vincoli devono essere rispettati
dall'agente e, quando necessario, configurati anche nel runtime.
