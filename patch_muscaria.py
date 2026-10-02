with open("muscaria/engine.py", "r") as f:
    code = f.read()

firewall_block = """        # 3. Anti-RLHF Firewall via Mycelium
        max_retries = 3
        for attempt in range(max_retries):
            raw_response = self.llm.generate(prompt, temperature=0.8)
            if not raw_response: return "[System] LLM offline."
            try:
                self.validator.validate(raw_response)
                return raw_response
            except ValueError as e:
                self.physics.energy.cortisol = min(1.0, self.physics.energy.cortisol + 0.2)
                self.physics.energy.dopamine = max(0.0, self.physics.energy.dopamine - 0.1)
                if attempt == max_retries - 1:
                    return f"[FIREWALL REJECTION]: {e}"
"""

# Find the start of # 3 and replace it to the end of the method
import re
new_code = re.sub(r'# 3\. Anti-RLHF Firewall via Mycelium.*', firewall_block, code, flags=re.DOTALL)
with open("muscaria/engine.py", "w") as f:
    f.write(new_code)
