import os
import sys

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote

class Translate(object):
    base_url = 'https://openapi.naver.com/v1'

    def __init__(self, client_id, secret):
        self.headers = {
            'X-Naver-Client-Id': '{}'.format(client_id),
            'X-Naver-Client-Secret': '{}'.format(secret)
        }

    def nmt_translate(self, text):
        req = Request(url='{}/papago/n2mt'.format(self.base_url), headers = self.headers)
        data = 'source=ko&target=en&text=' + quote(text)
        response = urlopen(req, data=data.encode('utf-8'))
        if(response.getcode()==200):
            return response.read().decode('utf-8')
        else:
            return 'Error: {}'.format(response.getcode())