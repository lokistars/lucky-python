import pytest
import requests

from .utils.requestsUtil import RequestsUtil
from .utils.yamlUtils import *


@pytest.mark.parametrize('args', readYaml())
@pytest.mark.slow
def test_requests(args):
    print(args['name'])
    url = args['request']['url']
    method = args['request']['method']
    data = args['request']['data']
    headers = args['headers']
    # res = requests.post(url, data=data, headers=headers)
    res = RequestsUtil().sendRequest(method, url, data, headers=headers)
    print("获取结果：", res)
    assert res.status_code == 200
