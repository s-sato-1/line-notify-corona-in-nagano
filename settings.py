import configparser


conf = configparser.ConfigParser(interpolation = None)
conf.read('settings.ini')

line_notify_token = conf['line']['line_notify_token']
line_notify_api = conf['line']['line_notify_api']
covid19_api = conf['line']['covid19_api']
