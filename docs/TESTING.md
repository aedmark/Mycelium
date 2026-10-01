# Testing Mycelium Network

## Verification structure
| Scope | Location | Confidence in | Misses | Speed |
| --- | --- | --- | --- | --- |
| Unit | `mycelium/tests/` | pure core functions | live LLM, UI | seconds |
| Module | `<mode>/tests/` | ui wrapper logic | live LLM | seconds |

## Commands
- Run all tests: `pytest`
- Run core tests: `pytest mycelium/tests/`

## Manual checks
The UI logic and Live Ollama firewalls must be tested manually by booting the FastAPI servers and injecting known slop:
1. Boot Spore: `uvicorn spore.api:app --host 127.0.0.1 --port 8000`
2. Input flowery language: "I hope this helps! Here is the architecture."
3. Observe the rejection in the terminal and the clean output in the UI.
