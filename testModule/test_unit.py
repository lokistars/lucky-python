import unittest

import pytest
import requests

ip = "http://192.168.11.222:8011/"


def request(url, data, **headers):
    req = requests.post(url, json=data, headers=headers)
    print(req.json())
    assert req.status_code == 200


class TestApi(unittest.TestCase):

    # @pytest.mark.slow
    def test_saveModel(self):
        url = f"{ip}model/saveModel"
        data = {"name": "张三 3311", "id": "642fb9b56ae79e6ef008e666"}
        headers = {"_uid": "99"}
        request(url, data, **headers)

    # @pytest.mark.slow
    def test_getModelList(self):
        url = f"{ip}model/getModelList"
        data = {"name": "张三 3311"}
        request(url, data)

    # @pytest.mark.slow
    def test_savePage(self):
        url = f"{ip}model/savePage"
        data = {"name": "张三 33", "id": "642fb9b56ae79e6ef008e666"}
        headers = {"_uid": "99"}
        request(url, data, **headers)

    # @pytest.mark.slow
    def test_saveSubject(self):
        url = f"{ip}subject/saveSubject"
        data = {"question": "今天星期几", "subName": "99", "description": "99"}
        headers = {"_uid": "99"}
        request(url, data, **headers)

    # @pytest.mark.slow
    def test_findSubject(self):
        url = f"{ip}subject/getSubjectList"
        data = {"question": "abcd"}
        headers = {"_uid": "99"}
        request(url, data, **headers)

    # @pytest.mark.slow
    def test_saveValidation(self):
        url = f"{ip}validation/saveValidation"
        data = {"modelId": "99", "pageId": "99", "subName": ["keys"]}
        headers = {"_uid": "99"}
        request(url, data, **headers)

    @pytest.mark.slow
    def test_getValidationList(self):
        url = f"{ip}validation/getValidationList"
        data = {"modelId": "99", "pageId": "99"}
        request(url, data)
