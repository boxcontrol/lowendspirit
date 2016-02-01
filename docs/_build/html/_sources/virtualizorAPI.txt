Virtualizor Enduser API
=======================

Initiate the virtualizor object::

    >>> virtualizor = lowendspirit.Virtualizor_Enduser_API(apikey="your_api_key",
                                                           apiip="my.panel.com",
                                                           apipass="your_api_pass",
                                                           apiprotocol='http',
                                                           apiport='4082')

Get list of VPS's
-----------------

    >>> virtualizor.listvs()

START, STOP, RESTART, POWEROFF the VPS
--------------------------------------

    >>> virtualizor.start(id='server_id')  # start server
    >>> virtualizor.stop(id=1005)  # stop server with ID 1005
    >>> virtualizor.restart(7463)  # restart server with ID 7463
    >>> virtualizor.poweroff(1276)  # poweroff server with ID 1276

Get server status::

    >>> virtualizor.status(id='server_id')

GET or SET server's hostname
----------------------------

To get server hostname::

    >>> virtualizor.hostname(1782)

To set server hostname::

    >>> virtualizor.hostname(1782, newhostname='testserver')

Get CPU details
---------------

    >>> virtualizor.cpu(2777)

Get Bandwidth Details
---------------------

To get usage for current month::

    >>> virtualizor.bandwidth(2777)

To get usage for May of 2015:

    >>> virtualizor.bandwidth(2777, '201505')

List the processes - OpenVZ only
--------------------------------

    >>> virtualizor.processes(4778)

List the services - OpenVZ only
-------------------------------

    >>> virtualizor.services(4778)

Change ROOT password of the VPS
-------------------------------

    >>> virtualizor.changepassword(1003, 'newpassword')

Get the VNC Details XEN/KVM only
--------------------------------

    >>> virtualizor.vnc(1003)

For this function to work you need to have VNC enabled for the VPS.

Change VNC password XEN/KVM only
--------------------------------

    >>> virtualizor.vncpass(1003, 'newpassword')

For this function to work you need to have VNC enabled for the VPS.

List available OS Templates
---------------------------

    >>> virtualizor.ostemplate(1387)

You will get list of available OS templates with their associated ID, which you need to reinstall VPS.

Reinstall the OS
----------------

    >>> virtualizor.ostemplate(1387, newosid=1, newpass='root_password')

`newosid` you obtain from previous function, `newpass` is root password for reinstalled server.

Install a Control Panel

    >>> virtualizor.controlpanel(1387, 'cpanel')

