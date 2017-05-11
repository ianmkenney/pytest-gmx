import pytest

def pytest_addoption(parser):
    parser.addoption("--low-performance", action="store_true", default=False)

@pytest.fixture
def lowperformance(request):
    return request.config.getoption("--low-performance")
