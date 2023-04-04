import json
import requests


class RequestsUtil:
    session = requests.session()

    def sendRequest(self, method, url, data, **kwargs):
        res = None
        method = str(method).lower()
        if method == "get":
            res = RequestsUtil.session.request(method, url=url, params=data, **kwargs)

        elif method == "post":

            res = RequestsUtil.session.post(url, json=data, **kwargs)
        else:
            data = json.dumps(data)
            res = RequestsUtil.session.request(method, url=url, data=data, **kwargs)
        return res

