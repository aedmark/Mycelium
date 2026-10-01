# Mycelium Network

The extracted biological core and its specialized fruiting bodies (Lichen, Muscaria, Spore), isolated from the BoneAmanita monolith. It provides a generalized AI engine driven by semantic drag, stamina (ATP), and neurochemistry (cortisol/dopamine).

## Practices and expectations
- Default branch: `main`.
- Working branch pattern: `feature/<topic>`.
- Commit format: standard conventional commits (e.g., `feat:`, `fix:`, `refactor:`).
- Release/version scheme: Semantic versioning based on major biological evolutions.
- **Writing:** Keep instructions concise and maintain a biological metaphor where applicable.
- **Code comments:** Explain the *why* of physical interactions, especially in physics-to-prompt translations.
- **Asking vs. doing:** Perform refactors independently, but confirm before altering the core `PhysicsPacket` or `HalcyonStore` schemas.
- **Reporting:** Show test pass rates and output logs when changing the engine.

## Authority and strictness
| File | Maintenance rule | Owner |
| --- | --- | --- |
| `AGENTS.md` | Do not edit | Maintainer-owned content |
| `mycelium/store.py` | Schema changes must be backward-compatible | Engine |

## Terminology
| Term | What it names | Old name or nearby concept |
| --- | --- | --- |
| Mycelium | The core biological library | BoneAmanita Core |
| Fruiting Body | A mode-specific application wrapper | Game Mode |
| Lichen | Adventure Mode UI & Logic | Spatial / MUD Mode |
| Muscaria | Creative Mode UI & Logic | Brainstorming Mode |
| Spore | Technical Mode UI & Logic | Coding / Kernel Mode |
| Halcyon | SQLite persistent memory layer | Database |

## Structure
| Path | What it owns |
| --- | --- |
| `mycelium/` | The core Python library (lexicon, physics, composer, store). |
| `lichen/` | FastAPI backend and UI for the Adventure fruiting body. |
| `muscaria/` | FastAPI backend and UI for the Creative fruiting body. |
| `spore/` | FastAPI backend and UI for the Technical fruiting body. |

## Invariants and guardrails
- Python 3.10+ standard. FastAPI for web interfaces.
- Supported platforms: Local Linux/Mac.
- Core Invariant: `mycelium/` must *never* import from the fruiting bodies. It remains a strict dependency.
- Local SQLite (`.db`) files must not be tracked in Git.

## Environment context
| Context | Environment | Limits |
| --- | --- | --- |
| Local development | Local Ollama (`mistral-nemo:latest`) | Port 11434 must be open |

## Commands
- Setup: `pip install -r requirements.txt`.
- Run: `uvicorn lichen.api:app --host 127.0.0.1 --port 8000` (substitute `lichen` with `muscaria` or `spore`).
- Fast checks: `pytest`
