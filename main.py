import os
import sys
import time
import datetime
import requests
import json
import urllib.request

import settings


class LineNotify(object):
    """
    """
    def __init__(self, api, token):
        """
        """
        self.api = api
        self.token= token

    def notify(self, msg):
        """
        """
        line_notify_token = self.token
        notification_message = msg
        line_notify_api = self.api
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{notification_message}'}
        requests.post(line_notify_api, headers=headers, data=data)

    def notify_with_screenshot(self, msg):
        """
        """
        line_notify_token = self.token
        notification_message = msg
        line_notify_api = self.api
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{notification_message}'}
        files = {'imageFile': open("screenshot/screenshot.png", "rb")}
        requests.post(line_notify_api, headers=headers, data=data, files=files)


if __name__ == "__main__":
    """
    """
    line = LineNotify(settings.line_notify_api, settings.line_notify_token)
    try:
        api = settings.covid19_api
        res = urllib.request.urlopen(api)
        data = json.loads(res.read().decode('utf-8'))

        if (data['errorInfo']['errorFlag'] == '0'):
            # print(data['itemList'][0])
            # print(data['itemList'][1])
            # print(datetime.date.today())
            latest_date = data['itemList'][0]['date']
            area = data['itemList'][0]['name_jp']
            npatients = data['itemList'][0]['npatients']
            increase = int(npatients) - int(data['itemList'][1]['npatients'])
            line.notify("\r\n日付: {}\r\n地域: {}\r\n累計の感染者数: {}\r\n前日比での増加人数: {}".format(latest_date, area, npatients, increase))
        else:
            line.notify("[Err] Api errorFlag is not '0'")

    except urllib.error.HTTPError as e:
        line.notify('[Err] {}'.format(e))
    except json.JSONDecodeError as e:
        line.notify('[Err] {}'.format(e))
