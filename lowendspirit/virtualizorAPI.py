from phpserialize import unserialize
import urllib.parse as urp
import pycurl
from io import BytesIO
import json


class Virtualizor_Enduser_API:
    def __init__(self, apikey, apipass, apiip, apiport='4083', apiprotocol="https", apierror=[]):
        '''
        Constructor
        :param apikey: The API KEY of your account
        :param apipass: The API password of your account
        :param apiip: The IP of the Control Panel
        :param apiport: Optional port to connect to, default is set to 4083 for SSL, for non SSL use 4082
        :param apiprotocol: Default protocol set to https
        :param apierror: empty array to store errors
        :return:
        '''
        self.apikey = apikey
        self.apipass = apipass
        self.apiip = apiip
        self.apiport = apiport
        self.apiprotocol = apiprotocol
        self.apierror = apierror

    def __repr__(self):
        '''
        Dumps a variable
        '''
        return (str(self.apiip) + '; apikey=' + str(self.apikey) + '; apipass=' + str(self.apipass))

    @staticmethod
    def unserialize_(apistr):
        '''
        Unserializes a string
        :param apistr: The serialized string
        :return: the unserialized array on success or false on failure
        '''
        apistr = unserialize(apistr)

        if not apistr:
            apistr = unserialize(apistr)

        if not apistr:
            return False
        else:
            return apistr

    def apicall(self, path, post=[], cookies=[]):
        '''
        Makes an API request to the server to do a particular task
        :param path: The action you want to do
        :param post: An array of DATA that should be posted
        :param cookies: An array FOR SENDING COOKIES
        :return: The unserialized array on success OR False on failure
        '''
        url = self.apiprotocol + "://" + self.apiip + ":" + self.apiport + "/" + path

        url += "&api=serialize&apikey=" + urp.quote_plus(self.apikey) + "&apipass=" + urp.quote_plus(self.apipass)

        # Set curl parameters.
        ch = pycurl.Curl()
        ch.setopt(ch.URL, url)

        # time out
        ch.setopt(ch.CONNECTTIMEOUT, 3)

        # Turn off the server and peer verification (TrustManager Concept)
        ch.setopt(ch.SSL_VERIFYPEER, 0)
        ch.setopt(ch.SSL_VERIFYHOST, 0)
        ch.setopt(ch.SSL_CIPHER_LIST, 'rsa_rc4_128_sha')

        # user agent
        ch.setopt(ch.USERAGENT, 'Virtualizor')

        # Cookies
        if cookies:
            ch.setopt(ch.COOKIESESSION, True)
            ch.setopt(ch.COOKIE, urp.urlencode(cookies, '', '; '))

        if post:
            ch.setopt(ch.POSTFIELDS, urp.urlencode(post))
            ch.setopt(ch.POST, 1)

        # get response from server
        buffer = BytesIO()
        ch.setopt(ch.WRITEDATA, buffer)
        ch.perform()
        ch.close()
        resp = buffer.getvalue()

        if not resp:
            return False

        r = self.unserialize_(resp)

        if not r:
            return False

        return r

    def listall(self):
        resp = self.apicall('index.php?act=listvs')
        return resp

    def listvs(self):
        '''
        List the Virtual Servers in your account
        :return: The array containing a list of Virtual Servers one has in their account
        '''
        resp = self.apicall('index.php?act=listvs')
        return resp.get(b'vs').keys()

    def start(self, id):
        '''
        START a Virtual Server
        :param id: The VM's ID
        :return: bool True on success or False on failure
        '''
        res = self.apicall('index.php?svs=' + str(id) + '&act=start&do=1')
        if res.get(b'done'):
            return True
        else:
            return False

    def stop(self, id):
        '''
        STOP a Virtual Server
        :param id: The VM's ID
        :return: bool True on success or False on failure
        '''
        res = self.apicall('index.php?svs=' + str(id) + '&act=stop&do=1')
        if res.get(b'done'):
            return True
        else:
            return False

    def restart(self, id):
        '''
        RESTART a Virtual Server
        :param id: The VM's ID
        :return: bool True on success or False on failure
        '''
        res = self.apicall('index.php?svs=' + str(id) + '&act=restart&do=1')
        if res.get(b'done'):
            return True
        else:
            return False

    def poweroff(self, id):
        '''
        POWEROFF a Virtual Server
        :param id: The VM's ID
        :return: bool True on success or False on failure
        '''
        res = self.apicall('index.php?svs=' + str(id) + '&act=poweroff&do=1')
        if res.get(b'done'):
            return True
        else:
            return False

    def status(self, id):
        '''
        STATUS of a Virtual Server
        :param id: The VM's ID
        :return: status of the server
        '''
        res = self.apicall('index.php?svs=' + str(id) + '&act=start')
        if res.get(b'status') == 1:
            return 'Online'
        else:
            return 'Offline'

    def hostname(self, id, newhostname=None):
        '''
        GET or SET the hostname of a VM. To get the current hostname dont pass newhostname parameter
        :param id: The VMs ID
        :param newhostname: The new HOSTNAME of the virtual server.
        :return: The CURRENT hostname is returned if $newhostname is NULL.
         *       FALSE is returned if there was an error while setting the new hostname
         *       'onboot' is returned if the new hostname will be set when the VPS is STOPPED and STARTED
         *       'done' is returned if the new hostname has been set right now - Mainly OpenVZ
        '''

        # are we going to change hostname ?
        if newhostname != None:
            post = (('newhost', newhostname.encode()), ('changehost', 'Change Hostname'))

            resp = self.apicall('index.php?svs=' + str(id) + '&act=hostname', post)

            # was there an error
            if resp.get(b'error') != None:
                error = resp(b'error')
                return false
            # will it be done when the VPS is STOPED and STARTED ?
            elif resp.get(b'onboot') != None:
                return 'onboot'
            # It was done successfully
            elif resp.get(b'done') != None:
                return 'done'
        # just return hostname
        else:
            resp = self.apicall('index.php?svs' + str(id) + '&act=hostname')
            #return resp(b'current').json()
            return resp.get(b'current').decode()

    def cpu(self, id):
        '''
        GET the CPU details of a VM. Incase of Xen / KVM, only information is available as usage cannot be sensed.
        :param id: The VMs ID
        :return: An array containing the details is returned. Usage details is available only in case of OpenVZ.
        '''

        resp = self.apicall('index.php?svs=' + str(id) + '&act=cpu')
        return resp.get(b'cpu')

    def ram(self, id):
        '''
        GET the RAM details of a VM. Incase of Xen / KVM, only information is available as usage cannot be sensed.
        :param id: The VMs ID
        :return: An array containing the details is returned. Usage details is available only in case of OpenVZ.
        '''
        resp = self.apicall('index.php?svs=' + str(id) + '&act=ram')
        return resp.get(b'ram')

    def disk(self, id):
        '''
        GET the Disk details of a VM. Incase of Xen / KVM, only information is available as usage cannot be sensed.
        :param id: The VMs ID
        :return: An array containing the details is returned. Usage details is available only in case of OpenVZ.
        '''
        resp = self.apicall('index.php?svs=' + str(id) + '&act=disk')
        return [resp.get(b'disk'), resp.get(b'inodes')]

    def bandwidth(self, id, month=None):
        '''
        GET the Bandwidth Usage of a VM.
        :param id: The VMs ID
        :param month: The month in the format YYYYMM e.g. 201205 is for the Month of May, 2012
        :return: Returns an array of Bandwidth Information for the Month GIVEN.
                 By Default the CURRENT MONTH details are returned
        '''
        if month != None:
            resp = self.apicall('index.php?svs=' + str(id) + '&act=bandwidth' + '&show=' + month)
            return resp.get(b'bandwidth')
        else:
            resp = self.apicall('index.php?svs=' + str(id) + '&act=bandwidth')
            return resp.get(b'bandwidth')

    def processes(self, id):
        '''
        List the Processes in a VPS - Only OpenVZ
        :param id: The VMs ID
        :return: An array containing all the processes is returned
        '''
        resp = self.apicall('index.php?svs=' + str(id) + '&act=processes')
        return resp.get(b'processes')

    def services(self, id):
        '''
        List the Services in a VPS - Only OpenVZ
        :param id: The VMs ID
        :return: An array containing all the services is returned
        '''
        resp = self.apicall('index.php?svs=' + str(id) + '&act=services')
        return [resp.get(b'services'), resp.get(b'autostart'), resp.get(b'running')]

    def changepassword(self, id, password):
        '''
        Changes the root password of a VPS
        :param id: The VMs ID
        :param password: The new password to set
        :return: FALSE is returned if there was an error while setting the new password
                'onboot' is returned if the new password will be set when the VPS is STOPPED and STARTED
                'done' is returned if the new password has been set right now - Mainly OpenVZ
        '''
        post = (('newpass', password),
                ('conf', password),
                ('changepass', 'Change Password'))

        resp = self.apicall('index.php?svs=' + str(id) + '&act=changepassword', post)
        #return resp

        # was there an error
        if resp.get(b'error') != None:
            error = resp.get(b'error')
            return False
        # will it be done when the VPS is STOPPED and STARTED ?
        elif resp.get(b'onboot') != None:
            return 'onboot'
        # it was done successfully
        elif resp.get(b'done') != None:
            return 'done'

    def vnc(self, id):
        '''
        Get the VNC Details like PORT, IP, VNC Password. Only available in case of Xen and KVM VPS if VNC is enabled.
        :param id: The VMs ID
        :return: An array containing all the VNC Details
        '''
        resp = self.apicall('index.php?svs=' + str(id) + '&act=vnc')
        if resp == False:
            return 'VNC is not enabled'
        elif resp.get(b'info') != None:
            return resp.get(b'info')

    def vncpass(self, id, password):
        '''
        Change the VNC Password. Only available in case of Xen and KVM VPS if VNC is enabled.
        :param id: The VMs ID
        :param password: The new password to set
        :return: FALSE is returned if there was an error while setting the new password
                'onboot' is returned if the new password will be set when the VPS is STOPPED and STARTED
        '''
        post = (('newpass', password.encode()),
                ('conf', password.encode()),
                ('vncpass', 'Change Password'))
        resp = self.apicall('index.php?svs=' + str(id) + '&act=vncpass', post)

        # was there an error
        if resp.get(b'error') != None:
            return False
        elif resp.get(b'onboot') != None or resp.get(b'done') != None:
            return 'onboot'

    def ostemplate(self, vid, newosid=None, newpass=None):
        '''
        Re-installs a VPS if the newosid is specified. If the newosid is not passed,
        then this function will return an array of available templates.
        :param vid: The VMs ID
        :param newosid: The Operating System ID (you got from the list) that will be installed on the VPS.
        :param newpass: The new root password to set
        :return: FALSE is returned if there was an error while setting the new password
                 string 'onboot' is returned if the new password will be set when the VPS is STOPPED and STARTED
                 string 'done' is returned if the new password has been set right now - Mainly OpenVZ
                 array An array of the list of available OS Templates is returned if newosid is None
        '''
        # get the list of OS Templates
        resp = self.apicall('index.php?svs=' + str(vid) + '&act=ostemplate')

        # Get a list of Virtual Servers
        listvs = self.listvs()
        virtualization = listvs.get(vid).get(b'virt').decode()
        availabledistros = resp.get(b'oslist').get(virtualization.encode())
        ostemplate = []
        for distro in availabledistros.values():
            for key, value in distro.items():
                ostemplate.append((key, value.get(b'name').decode()))

        if newosid != None:
            post = (('newos', str(newosid)),
                    ('newpass', newpass.encode()),
                    ('conf', newpass.encode()),
                    ('reinsos', 'Reinstall'))
            resp = self.apicall('index.php?svs=' + str(vid) + '&act=ostemplate', post)

            # was there an error
            if resp.get(b'error') != None:
                return resp.get(b'error')
            # will it be done when the VPS is STOPPED and STARTED ?
            elif resp.get(b'onboot') != None:
                return 'onboot'
            # It was done successfully
            elif resp.get(b'done') != None:
                return 'done'
        else:
            return ostemplate

    def controlpanel(self, id, panel):
        '''
        Install a Control Panel
        :param id: The VMs ID
        :param panel: The Name of the Panel you want to install. Options - cpanel, plesk, webuzo, kloxo, webmin
        :return: FALSE is returned if there was an error while installing the control panel
                'onboot' is returned if the control panel will be installed when the VPS is STOPPED and STARTED
                'done' is returned if the control panel has been installed right now - Mainly OpenVZ
        '''

        post = (('ins', panel), ('', str(1)))
        resp = self.apicall('index.php?svs=' + str(id) + '&act=controlpanel', post)

        # Was there an error
        if resp.get(b'error') != None:
            #return False
            return resp.get(b'error')
        # will it be done when the VPS is STOPPED and STARTED ?
        elif resp.get(b'onboot') != None:
            return 'onboot'
        # It was done successfully
        elif resp.get(b'done') != None:
            return 'done'
