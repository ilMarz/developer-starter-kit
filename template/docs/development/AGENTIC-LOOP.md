# Agentic loop e modelli per ruolo

Il kit descrive un ciclo eseguito dall'agente nel client. Non contiene un servizio che gira
in background, un orchestratore API o un meccanismo tecnico per fermare una fattura.

```text
criteri approvati → slice pronta → piano/ambiente
 → implementazione → esecuzione osservata → review
 → [successo] report/integrazione autorizzata
 → [difetto correggibile + budget] diagnosi → patch → prove/regressioni → review mirata
 → [incertezza, budget o autorizzazione mancante] candidato + stop motivato
```

## Condizioni operative

Prima dell'esecuzione concordare scope, criteri, comandi, budget di tempo/tentativi e
costo se misurabile. Registrare autorizzazioni e destinazione. I valori in loop.json sono
proposte iniziali da confermare per incarico, non limiti già approvati dall'utente.
Il kit non incrementa budget e non cambia criteri per ottenere un pass.

Ogni iterazione conserva ID slice/task, modello effettivo, commit/diff, comandi, exit code,
evidenze, review, consumo noto e prossimo passo. Un errore del tool è un errore, non un pass.
Dopo un'interruzione riconciliare lo stato prima di ripetere azioni con effetti.

Stop: obiettivo verificato; budget esaurito; ripetizione senza nuova evidenza o miglioramento;
criterio incoerente/ambiguo; capacità essenziale mancante; effetto non autorizzato.
Il limite effettivo dei fix è il più restrittivo tra quello del progetto e quello della skill.
Non avviare una nuova iterazione quando la stima supera il budget residuo. Se consumo non
misurabile, dichiararlo e non promettere un tetto economico; concordare un limite alternativo
prima di chiamate a pagamento. Impostare limiti tecnici presso il provider quando necessari.

## Ruoli e modelli

`.devkit/models.json` contiene ruoli, ID opzionali e politica di fallback. Non è un file
nativo di configurazione Codex. Il coordinatore lo legge e traduce nei tool disponibili.

| Ruolo | Scelta di partenza | Quando usare più capacità |
| --- | --- | --- |
| planner | Modello capace di ragionamento progettuale | Requisiti ambigui, architettura, compromessi |
| implementer | Modello bilanciato | Integrazioni ampie e debugging difficile |
| reviewer | Modello bilanciato o forte, contesto separato | Sicurezza, concorrenza, migrazioni, review finale |
| debugger | Modello bilanciato | Ipotesi complesse e problemi intermittenti |
| researcher | Modello rapido per recupero circoscritto | Sintesi tecnica con fonti in conflitto |

Prima del dispatch verificare gli ID esposti dal client; fissarli per l'incarico e registrarli.
Modelli distinti per ruolo sono opzionali: due agenti con lo stesso modello possono comunque
avere contesti separati. Un modello diverso non garantisce indipendenza degli errori.
Nessun ID provider o nome 'latest' universale è incorporato nel kit.

Nel client che offre selezione per subagente, passare esplicitamente modello e reasoning
supportati. Con un modello già configurato dal client si può ereditarlo, ma va dichiarato:
non scrivere che è stato usato un modello diverso. Un fallback non autorizzato richiede scelta.
Il cambio del modello della chat principale può richiedere azione dell'utente nel client.
Usare provider esterni richiede runtime, credenziali e policy dati configurati; la scelta in JSON
non abilita da sola un altro provider e non autorizza invio di dati.

## Coordinamento

Un implementatore alla volta nel checkout condiviso. Ricerca/review indipendenti possono
procedere in parallelo quando il lavoro lo consente. Un brief include obiettivo, vincoli,
file/interfacce, prove attese e output; non tutta la cronologia della chat.
I limiti di concorrenza sono verificati nel client, non fissati universalmente dal kit.
Il coordinatore mantiene il registro; i subagenti non si assegnano review aggiuntive.

## Due loop diversi

Questo è il loop di sviluppo del software. Se il prodotto contiene a sua volta agenti,
il suo loop runtime richiede implementazione propria: stato persistente, autorizzazioni,
strumenti, timeout/retry, osservabilità ed eval. Non confondere il kit con quelle funzionalità.
