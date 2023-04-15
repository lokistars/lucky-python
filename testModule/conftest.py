import pytest


@pytest.fixture(scope="function", autouse=True)
def println():
    print("测试用例执行之前")


# 需要在测试用例入参中设置方法名
@pytest.fixture(scope="session")
def session_headers():
    headers = {'Content-Type': 'application/json', '_uid': '2'}
    return headers


# 在 pytest 的配置中添加一个名为 "slow" 的标记，以便在运行 pytest 时使用 -m 选项来选择特定的标记运行测试用例
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.addinivalue_line("markers", "model: mark test as model to run")


def pytest_sessionstart(session):
    session.headers = {'Content-Type': 'application/json', '_uid': '2'}
