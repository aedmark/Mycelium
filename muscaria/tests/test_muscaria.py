from muscaria.engine import MuscariaEngine
from unittest.mock import MagicMock

def test_muscaria_initialization():
    engine = MuscariaEngine(db_path=":memory:")
    assert engine.physics.energy.dopamine == 0.8
