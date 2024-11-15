import pytest
from arbitron.config.settings import Settings

@pytest.fixture
def settings():
    """Fixture for test settings."""
    return Settings(
        API_KEY="test_key",
        API_SECRET="test_secret",
        MAX_POSITION_SIZE=100.0,
        RISK_TOLERANCE=0.01
    )

@pytest.fixture
def trading_agent(settings):
    """Fixture for trading agent."""
    from arbitron.core.agent import TradingAgent
    return TradingAgent(config=settings.dict()) 