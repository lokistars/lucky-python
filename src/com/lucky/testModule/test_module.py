import pytest
import requests as req


def test_getCodeUser():
    url = "http://10.10.11.50:8010/userData/getCodeUser"
    data = {"key": 1}
    res = req.post(url, json=data)

    print("获取结果：", res)
    assert res.status_code == 200


if __name__ == '__main__':
    pytest.main()
