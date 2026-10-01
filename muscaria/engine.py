import json
import yaml
import os
from mycelium.lexicon import LinguisticAnalyzer
from mycelium.physics import PhysicsPacket
from mycelium.composer import PromptComposer, ResponseValidator
from mycelium.store import HalcyonStore
from mycelium.llm import OllamaInterface

class MuscariaEngine:
    """
    The Creative Mode Fruiting Body.
    Wraps Mycelium biological processing with elevated neurochemistry
    and relaxed physical friction for unbounded ideation.
    """
    def __init__(self, db_path="muscaria.db"):
        print("[Muscaria] Booting Creative Mode...")
        self.lore_dir = os.path.join(os.path.dirname(__file__), "lore")
        
        # Load Localized Lore
        with open(os.path.join(self.lore_dir, "style_crimes.json")) as f:
            style_crimes = json.load(f)
        with open(os.path.join(self.lore_dir, "system_prompts.json")) as f:
            system_prompts = json.load(f)
        with open(os.path.join(self.lore_dir, "self_claims.yaml")) as f:
            self_claims = yaml.safe_load(f)
        with open(os.path.join(self.lore_dir, "lexicon.json")) as f:
            lex_data = json.load(f)
            
        print("[Muscaria] Lore loaded. Booting Mycelium Core...")
        
        # Initialize Mycelium Core dependencies
        self.lexicon = LinguisticAnalyzer(lex_data["VOCAB"], lex_data["LINGUISTICS"])
        self.physics = PhysicsPacket.void_state()
        
        # Elevated Neurochemistry Baseline for Creative Mode
        self.physics.energy.stamina = 100.0
        self.physics.energy.dopamine = 0.8  # Very high baseline inspiration
        self.physics.energy.cortisol = 0.05 # Low initial stress
        
        self.composer = PromptComposer(system_prompts, self_claims)
        self.validator = ResponseValidator(style_crimes)
        self.store = HalcyonStore(db_path)
        self.llm = OllamaInterface()
        
        print("[Muscaria] The Muse is Awake.\n")

    def process_input(self, text: str) -> str:
        # 1. Biological Processing via Mycelium
        vector = self.lexicon.vectorize(text)
        
        # We manually apply the vector to leverage Muscaria's unique rules
        # In Muscaria, dopamine increases with 'flow' (kinetic/poetic words)
        self.physics.apply_vector(vector)
        flow = vector.get("flow", 0.0)
        self.physics.energy.dopamine = min(1.0, self.physics.energy.dopamine + (flow * 0.1))
        
        if self.physics.energy.stamina <= 0.0:
            return "[System] The creative spark fades. You are exhausted. (ATP = 0)"
            
        # 2. Compose Prompt via Mycelium
        bio_state = {
            "stamina": self.physics.energy.stamina,
            "cortisol": self.physics.energy.cortisol,
            "dopamine": self.physics.energy.dopamine
        }
        
        prompt = self.composer.compose(
            user_query=text, 
            bio_state=bio_state, 
            physics_state=self.physics.to_dict(),
            template_key="CREATIVE"
        )
        
        # For the engine wrapper demo, we mock the LLM response
        # Hit the real LLM
        raw_response = self.llm.generate(prompt, temperature=0.8)
        if not raw_response: return "[System] LLM offline."
        
                # 3. Anti-RLHF Firewall via Mycelium
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
