import json, yaml, os
from .lexicon import LinguisticAnalyzer
from .physics import PhysicsPacket
from .composer import PromptComposer, ResponseValidator
from .store import HalcyonStore
from .llm import OllamaInterface

class MyceliumEngine:
    def __init__(self):
        self.lore_dir = os.path.join(os.path.dirname(__file__), "lore")
        with open(os.path.join(self.lore_dir, "style_crimes.json")) as f: sc = json.load(f)
        with open(os.path.join(self.lore_dir, "system_prompts.json")) as f: sp = json.load(f)
        with open(os.path.join(self.lore_dir, "self_claims.yaml")) as f: self_claims = yaml.safe_load(f)
        with open(os.path.join(self.lore_dir, "lexicon.json")) as f: lex = json.load(f)
            
        self.lexicon = LinguisticAnalyzer(lex["VOCAB"], lex["LINGUISTICS"])
        self.physics = PhysicsPacket.void_state()
        self.physics.energy.stamina = 100.0
        
        self.composer = PromptComposer(sp, self_claims)
        self.validator = ResponseValidator(sc)
        self.store = HalcyonStore("mycelium.db")
        self.llm = OllamaInterface()

    def process_input(self, text: str) -> str:
        vector = self.lexicon.vectorize(text)
        self.physics.apply_vector(vector)
        
        if self.physics.energy.stamina <= 0: return "[System] Exhaustion."
            
        bio_state = {"stamina": self.physics.energy.stamina, "cortisol": self.physics.energy.cortisol, "dopamine": self.physics.energy.dopamine}
        prompt = self.composer.compose(text, bio_state, self.physics.to_dict(), "DEFAULT")
        
        for _ in range(3):
            raw = self.llm.generate(prompt)
            if not raw: return "[System] LLM offline."
            try:
                self.validator.validate(raw)
                return raw
            except ValueError as e:
                self.physics.energy.cortisol = min(1.0, self.physics.energy.cortisol + 0.1)
        return "[FIREWALL REJECTION]: Max retries hit."
