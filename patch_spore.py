with open("spore/engine.py", "r") as f:
    code = f.read()

import re
code = code.replace("from mycelium.store import HalcyonStore", "from mycelium.store import HalcyonStore\nfrom mycelium.llm import OllamaInterface")
code = code.replace("self.store = HalcyonStore(db_path)", "self.store = HalcyonStore(db_path)\n        self.llm = OllamaInterface()")

# Modify process_input signature
code = code.replace("def process_input(self, text: str, mock_llm_response: str) -> str:", "def process_input(self, text: str) -> str:")

firewall_block = """        # 3. Anti-RLHF Firewall via Mycelium
        max_retries = 3
        for attempt in range(max_retries):
            raw_response = self.llm.generate(prompt, temperature=0.1)
            if not raw_response: return "[System] LLM offline."
            try:
                self.validator.validate(raw_response)
                return raw_response
            except ValueError as e:
                if attempt == max_retries - 1:
                    return f"[FIREWALL REJECTION]: {e}"
"""
code = re.sub(r'# 3\. Anti-RLHF Firewall via Mycelium.*', firewall_block, code, flags=re.DOTALL)

with open("spore/engine.py", "w") as f:
    f.write(code)
