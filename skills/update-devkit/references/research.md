# Ricerca per aggiornamenti e opportunità

Parti dagli obiettivi e dalle difficoltà del kit corrente. Se manca un problema osservato,
dichiara il beneficio come ipotesi. Considera manutenzione, capacità nuove e riduzione
delle istruzioni; non premiare il numero di skill installate.

## Fonti iniziali, non una lista chiusa

- Origini effettive in `skills.lock.json` e documenti SOURCES/ECOSYSTEM.
- [Matt Pocock](https://github.com/mattpocock/skills) e [Superpowers](https://github.com/obra/superpowers):
  release, codice delle skill e risorse referenziate. Le versioni locali possono divergere.
- [OpenAI skills](https://learn.chatgpt.com/docs/build-skills),
  [subagenti](https://learn.chatgpt.com/docs/agent-configuration/subagents) e
  [changelog](https://learn.chatgpt.com/docs/changelog): verificare tool e client reali.
- [Anthropic Engineering](https://www.anthropic.com/engineering): harness, eval e contesto;
  distinguere risultati del loro ambiente da garanzie sul nostro.
- Repository mantenuti e fonti primarie di nuove proposte. Cataloghi come
  [skills.sh](https://skills.sh/) sono strumenti di scoperta, non certificazioni.

Ricerca anche fuori da questi nomi: debugging, test comportamentali, valutazione degli
agenti, sicurezza delle esecuzioni, memoria, routing dei modelli, costi, CI e compatibilità.
Non forzare ogni categoria in ogni aggiornamento: seleziona quelle pertinenti.

## Evidenze da raccogliere

URL e data della consultazione; data della release/evento; versione/commit;
file/simboli letti; licenza e manutenzione osservate; dipendenze e strumenti richiesti;
cambiamenti rispetto all'adozione attuale; limiti della lettura statica.
Uno screenshot del README o il numero di stelle non prova compatibilità o efficacia.

## Sperimentazione proporzionata

Confronta il workflow attuale e la proposta sullo stesso problema con criteri concordati.
Osserva correttezza, problemi sfuggiti, lavoro da rifare, costo/tempo e interventi richiesti.
Per giudizi semantici servono casi di riferimento, negativi e non valutabili; per proprietà
esatte preferisci verifiche deterministiche. Se un servizio richiede dati o costi nuovi,
specifica prima come testarli nel perimetro autorizzato.

Un esito debole può suggerire di migliorare domanda, contesto o decomposizione; registra
l'esperimento senza forzare l'adozione. Un'opportunità utile può essere anche rimuovere
un passaggio ridondante o sostituire due skill sovrapposte con una sola.
