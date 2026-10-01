# Roadmap

## Phase 1: Core Sporulation (Completed)
Goal: Extract the core engine from BoneAmanita into a generic Mycelium network.
- [x] P1-01 Extract `mycelium/` components (Lexicon, Physics, Composer, Store).
- [x] P1-02 Implement `lichen/` Adventure MUD wrapper.
- [x] P1-03 Implement `muscaria/` Creative wrapper.
- [x] P1-04 Implement `spore/` Technical wrapper.

## Phase 2: Web UIs (Completed)
Goal: Replace the CLI experience with interactive Bio-Terminal interfaces.
- [x] P2-01 FastAPI backend and HTML frontend for Lichen.
- [x] P2-02 FastAPI backend and HTML frontend for Muscaria.
- [x] P2-03 FastAPI backend and HTML frontend for Spore.
- [x] P2-04 FastAPI backend and HTML frontend for Mycelium Core.

## Phase 3: Live LLM Integration (Completed)
Goal: Wire the generic engines to a local Ollama instance.
- [x] P3-01 Build `OllamaInterface` hitting `localhost:11434`.
- [x] P3-02 Integrate Live Anti-RLHF retry loops into the engines.

## Phase 4: Future Agent Expansions
Goal: Integrate advanced agentic behaviors into the Mycelium pipeline.
- [ ] P4-01 Build a unified launcher or dashboard to manage the fruiting bodies.
- [ ] P4-02 Add multi-modal inputs (e.g. vision support for Muscaria).
