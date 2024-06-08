# Proiect Python: CFG, DFA și PDA

## Descrierea Proiectului

Acest proiect implementează trei concepte fundamentale din teoria limbajelor formale și a automatizărilor folosind Python: **Gramatica Independentă de Context (CFG)**, **Automatul Finit Determinist (DFA)** și **Automatul cu Stivă (PDA)**. Scopul este de a demonstra cum aceste structuri pot fi utilizate pentru a recunoaște și procesa limbaje formale. Un aspect deosebit al acestui proiect este utilizarea hash-urilor pentru procesarea datelor, datorită eficienței lor.

## Concepte Cheie

### Gramatica Independentă de Context (CFG)

O **Gramatica Independentă de Context** (Context-Free Grammar) este un sistem formal de reguli pentru generarea limbajelor independente de context. CFG-urile sunt esențiale pentru descrierea sintaxei limbajelor de programare și sunt utilizate în analiza sintactică.

- **Definiție:** O CFG este compusă din:
  - Un set de simboluri terminale.
  - Un set de simboluri non-terminale.
  - O mulțime de reguli de producție care descriu cum pot fi transformate simbolurile.
  - Un simbol de start.

**Exemplu de CFG:**
S → aSb | $

Aceasta CFG generează cuvinte care au un număr egal de 'a' și 'b'.

### Automatul Finit Determinist (DFA)

Automatul Finit Determinist (Deterministic Finite Automaton) este un model de calcul utilizat pentru a recunoaște limbaje regulate printr-un set de stări și tranziții determinate de simbolurile de intrare.

- **Definiție:** Un DFA este definit de:
  - Un set finit de stări.
  - O stare inițială.
  - Un set de stări acceptante.
  - O funcție de tranziție deterministă care mapează o pereche (stare curentă, simbol de intrare) la o stare următoare.

**Exemplu de DFA:**

Acest DFA recunoaște limbajul binar ce se termină în '1':

Stări: {q0, q1}
Stare inițială: q0
Stări acceptante: {q1}
Tranziții:
q0 → 0 → q0
q0 → 1 → q1
q1 → 0 → q0
q1 → 1 → q1

### Automatul cu Stivă (PDA)

Automatul cu Stivă (Pushdown Automaton) extinde DFA prin utilizarea unei stive, permițând recunoașterea limbajelor independente de context.

- **Definiție:** Un PDA este compus din:
  - Un set finit de stări.
  - O stare inițială.
  - Un set de stări acceptante.
  - O stivă pentru stocarea simbolurilor.
  - O funcție de tranziție care mapează o pereche (stare curentă, simbol de intrare, simbol de pe stivă) la o stare următoare și o manipulare a stivei.

**Exemplu de PDA:**

Acest PDA recunoaște limbajul `L = {a^n b^n | n ≥ 0}`:

Stări: {q0, q1, q2}
Stare inițială: q0
Stări acceptante: q2
Tranziții:
(q0, a, Z) → (q0, aZ)
(q0, a, a) → (q0, aa)
(q0, b, a) → (q1, $)
(q1, b, a) → (q1, $)
(q1, $, Z) → (q2, $)
## Utilizarea Hash-urilor

În cadrul acestui proiect, una dintre cele mai interesante abordări a fost utilizarea hash-urilor pentru procesarea datelor. Hash-urile oferă o modalitate eficientă și rapidă de gestionare și căutare a datelor, reducând complexitatea operațiunilor și accelerând accesul la informații.

**Beneficii ale utilizării hash-urilor:**
- **Rapiditate:** Operațiunile de inserare și căutare sunt foarte rapide, având o complexitate aproximativ constantă, $O(1)$.
- **Eficiență:** Permite gestionarea unui volum mare de date fără a compromite performanța.
