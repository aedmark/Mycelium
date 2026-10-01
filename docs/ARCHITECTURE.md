# Architecture

The Mycelium Network is a biological architecture for Language Model agents, isolating the generic math/physics from the mode-specific interaction layer.

## Boundaries and rules

- **Core independence:** `mycelium/` knows nothing of text adventures, creative writing, or coding modes. It only understands tokens, vectors, and stamina.
- **Lore delegation:** Each fruiting body (`lichen/`, `muscaria/`, `spore/`) defines its own `lore/` (dictionaries and system prompts) which override the baseline physics interactions.
- **Live LLM:** Interactions pipe directly into the local Ollama node.

## Components

| Component | Responsibility | Found in |
| --- | --- | --- |
| Lexicon | Maps raw text into physical vectors (`narrative_drag`, `flow`, `tension`) | `mycelium/lexicon.py` |
| Physics | Tracks somatic energy (Stamina) and neurochemistry (Dopamine/Cortisol) | `mycelium/physics.py` |
| Composer | Builds system prompts dynamically based on physical constraints | `mycelium/composer.py` |
| Store | Halcyon SQLite database for persisting memory | `mycelium/store.py` |
| Fruiting Body | A web UI that loads a specific lore and connects Mycelium to the user | `lichen/`, `muscaria/`, `spore/` |

## Data flow

1. User sends text to the FastAPI backend.
2. The Engine calculates the physical cost of the text via the localized Lexicon.
3. The Physics packet updates Stamina and Neurochemistry.
4. The Prompt Composer generates a state-aware prompt.
5. `OllamaInterface` queries the local `mistral-nemo` model.
6. The Firewall parses the response against `style_crimes.json`. If it fails, Cortisol spikes and the request retries.
7. The valid response and biological vitals are sent to the frontend.
