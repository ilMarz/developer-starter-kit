# Manutenzione del Developer Starter Kit

Questa directory è un artefatto autonomo e generalista. Mantieni separati i dati e le regole dei progetti che lo adottano.
Il materiale importato nei progetti è in `template/` e `skills/`; il resto serve a mantenere il kit.
Non modificare snapshot vendor senza registrare esplicitamente provenienza e diff.
Esegui `python3 tools/verify.py` e `python3 -m unittest discover -s tests -v` dopo modifiche
al bootstrap. Testare in directory temporanee esterne al kit, mai su progetti dell'utente.
I test degli script non dimostrano efficacia delle skill: usare anche `evals/scenarios.md`.
Preserva i file dei progetti esistenti; nessun aggiornamento silenzioso o modifica globale.

Per ricercare novità e aggiornare questo kit usa `skills/update-devkit/SKILL.md`.
Il percorso di discovery `.agents/skills/update-devkit` punta alla stessa skill.
La modalità predefinita produce proposte motivate, comprese opportunità fuori dall'inventario.
