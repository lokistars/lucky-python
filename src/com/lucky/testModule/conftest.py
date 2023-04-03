import pytest
import requests


# 定义了一个会话级别的 HTTP 请求会话，它被设置了一个通用的 User-Agent 头
@pytest.fixture(scope="session")
def before():
    session = requests.Session()
    session.headers.update({"User-Agent": "pytest"})
    # 测试运行前执行
    yield session
    # 测试运行后执行
    session.close()


# 在 pytest 的配置中添加一个名为 "slow" 的标记，以便在运行 pytest 时使用 -m 选项来选择特定的标记运行测试用例
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")
