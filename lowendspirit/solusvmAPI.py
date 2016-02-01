import requests

class Solus_Enduser_API:
    def __init__(self, url, api_hash, api_key):
        self.url = url
        self.api_hash = api_hash
        self.api_key = api_key
        self.values = ({'rdtype': 'json', 'hash': self.api_hash, 'key': self.api_key})

    def to_json(self, data):
        data=data.replace('><', '>...<')
        data = data.split('>')
        result = []
        for i in data:
            i = i.replace('<', '')
            i = i.replace('...', '')
            i = i.split('/')[0]
            result.append(i)
        if len(result) % 2 == 0:
            result.pop()
        result = {result[i]: result[i+1] for i in range(0, len(result) - 1, 2)}
        return result

    def sQuery(self, url, api_hash, api_key, values, action, extra=''):
        if not extra:
            values.update({'rdtype': 'json', 'hash': api_hash, 'key': api_key, 'action': action})
            response = requests.get('https://'+url+'/api/client/command.php', params=values, timeout=50)
        else:
            response = requests.get('https://'+url+'/api/client/command.php?key=' +
                                api_key + "&hash=" + api_hash +
                                "&action=info&" + extra, timeout=50)
        return response.text

    def get_status(self):
        data = self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='status')
        return self.to_json(data)

    def get_info(self):
        data =  self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='info')
        return self.to_json(data)

    def get_full_info(self):
        extra = 'ipaddr=true&hdd=true&mem=true&bw=true'
        data = self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='info', extra=extra)
        return self.to_json(data)

    def server_reboot(self):
        data = self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='reboot')
        return self.to_json(data)

    def server_shutdown(self):
        data = self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='shutdown')
        return self.to_json(data)

    def server_boot(self):
        data = self.sQuery(self.url, self.api_hash, self.api_key, self.values, action='boot')
        return self.to_json(data)


"""
url = 'vpsadmin.inceptionhosting.com'
api_key = 'I2M74-1S5QT-4CLMB'
api_hash = '8bc51adcd6c5eaef399d5d317a278c1392fdac04'
values = ({'rdtype': 'json', 'hash': api_hash, 'key': api_key})

nethLES = Solus_Enduser_API(url, api_hash, api_key)
print(nethLES.get_full_info())
print(nethLES.get_info())
print(nethLES.get_status())
#print(nethLES.server_shutdown())
#print(nethLES.server_shutdown())
print(nethLES.server_boot())
"""


