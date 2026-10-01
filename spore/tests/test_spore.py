from spore.engine import SporeEngine
from unittest.mock import MagicMock

def test_spore_initialization():
    engine = SporeEngine(db_path=":memory:")
    assert engine.physics.energy.dopamine == 0.1
    
def test_spore_code_friction():
    engine = SporeEngine(db_path=":memory:")
    engine.llm = MagicMock()
    engine.llm.generate.return_value = "def foo(): pass"
    
    code_input = "def my_func():\n    return True"
    engine.process_input(code_input)
    assert engine.physics.energy.stamina > 95.0
