# 🏷️ Taxonomy

Every film and season gets one `core-domain` and a set of `domains` grouped by
facet. The folder on the card is the `core-domain`. The playlist uses every
domain as a view.

Machine shape: [`../../src/data/schema/playlist.schema.json`](../../src/data/schema/playlist.schema.json).
Registry: [`../../src/data/taxonomy.json`](../../src/data/taxonomy.json).

## The nine questions

| # | Question | Produces |
| --- | --- | --- |
| 1 | Where does most of the runtime happen? | `environment` |
| 2 | What is the protagonist's role? | `environment` |
| 3 | What do the characters argue about, pursue, or protect most? | core candidate |
| 4 | What does the protagonist become by the end? | core candidate |
| 5 | What are they explicitly trying to get? | `pursuit` — never the core |
| 6 | What blocks them? | `pursuit` / `method` |
| 7 | How do they fight it? | `method` |
| 8 | What is the tone? | `tone` |
| 9 | What is the final scene really about? | tie-break |

Use [`templates/work.md`](templates/work.md) for one title and
[`templates/batch.md`](templates/batch.md) for a download batch.

## Core rule

```text
1. Q4 transformation, when it names a domain
2. Q3 obsession, when it names a domain
3. Q9 final scene, when it names a domain
4. Q1 setting, only when the place is the subject
never Q5 goal
```

The transformation beats the plot goal. This is why `Oldboy` is `discipline`
(forced detox and routine) and not `revenge` (the goal), and why `The Founder`
is `business` (the empire) and not `kitchen` (the setting).

## Heuristics

| If... | Then... |
| --- | --- |
| the setting is interchangeable | core is the transformation |
| removing the setting destroys the work | setting is the core |
| the core is a tone word | wrong; pick the subject |
| the core would cover a fifth of the library | too broad |
| two works in one folder feel unrelated | wrong core |
| the work is named after the place or job | hint, not proof |

## Red flags

- `core-domain` is `drama`, `comedy`, `action`, or `sci-fi`
- `core-domain` is not present in `domains`
- `rehab` used as a core when the subject is discipline
- `documentary` used anywhere — it is a format, not a domain
- more than six tags
- empty `core-reason`
- placeholder `signals`

## Domain registry

<!-- domains:begin -->
| Domain | Facet | Core candidate | Definition |
| --- | --- | :---: | --- |
| `action` | tone | no | kinetic physical conflict: chases, fights, stunts |
| `ambient` | medium | yes | background video or soundscape; no narrative |
| `animation` | medium | yes | animated medium |
| `art` | environment | yes | visual craft and design practice |
| `business` | pursuit | yes | building, owning, or scaling an enterprise |
| `cartel` | environment | yes | the drug trade and its organizations |
| `comedy` | tone | no | comic tone |
| `competition` | pursuit | yes | contests, rankings, and the will to win |
| `crime` | method | yes | criminal work and its consequences |
| `discipline` | method | yes | routine, training, self-command |
| `drama` | tone | no | serious tone |
| `escaping` | pursuit | yes | finding a flaw in a confinement and getting out |
| `fantasy` | tone | yes | invented worlds and magic |
| `finance` | environment | yes | markets, money, and risk |
| `gaming` | environment | yes | video game industry, culture, and competition |
| `genius` | tone | no | exceptional ability and its cost |
| `heist` | pursuit | yes | planning and executing a theft |
| `jail` | environment | yes | life inside a prison or cell |
| `kitchen` | environment | yes | restaurant service and its operations |
| `law` | environment | yes | lawyers, courts, and legal strategy |
| `music` | environment | yes | musical performance and craft |
| `puzzle` | pursuit | yes | solving an abstract problem or mystery |
| `rabbit-hole` | tone | no | a reality that turns out to be constructed |
| `rehab` | method | yes | a program or confinement aimed at behavior change |
| `revenge` | pursuit | yes | retribution as the engine |
| `sci-fi` | tone | no | speculative technology or future |
| `serial-killer` | tone | no | predatory violence as the subject |
| `spiritism` | tone | yes | possession, hauntings, and the supernatural |
| `sports` | environment | yes | athletic competition and training |
| `superhero` | tone | yes | superpowered heroics |
| `tech` | environment | yes | engineering, software, and machines |
| `time-travel` | tone | yes | movement through time as the mechanism |
| `torture` | method | yes | inflicted suffering as the subject |
| `underworld` | environment | yes | organized crime and criminal power |
<!-- domains:end -->

## Facets

| Facet | Domains |
| --- | --- |
| `environment` | art, cartel, finance, gaming, jail, kitchen, law, music, sports, tech, underworld |
| `pursuit` | business, competition, escaping, heist, puzzle, revenge |
| `method` | crime, discipline, rehab, torture |
| `tone` | action, comedy, drama, fantasy, genius, rabbit-hole, sci-fi, serial-killer, spiritism, superhero, time-travel |
| `medium` | ambient, animation |

A domain may be a core or a tag depending on the work. `rehab` is usually a
method; it is a core only when the program itself is the subject.

## Worked examples

| Work | Core | Why |
| --- | --- | --- |
| Oldboy | `discipline` | the transformation is sobriety and routine; revenge is the goal |
| The Bear | `kitchen` | remove the restaurant and nothing remains |
| The Founder | `business` | kitchen is the setting; the subject is expansion |
| Whiplash | `discipline` | music is the arena; the subject is the routine |
| Prison Break | `escaping` | the flaw in the confinement is the engine |
| Squid Game | `competition` | winning the games is the subject |
| The Godfather | `underworld` | criminal power and succession |
| 28 Days | `rehab` | the program itself is the subject |
| Requiem for a Dream | `rehab` | addiction and failed recovery are the subject |
