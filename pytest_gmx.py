import pytest

def pytest_addoption(parser):
    """Add options to control gromacs"""

    group = parser.getgroup('gmx')
    group.addoption(
            "--low-performance", 
            action="store_true", 
            dest='low_performance',
            help='Instruct gromacs to run on low performance mode',
    )
    

@pytest.fixture
def low_performance(request):
    return request.config.option.low_performance
