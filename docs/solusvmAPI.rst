SolusVM API v1
==============

Initiate the SolusVM object::

    >>> solus_vm = lowendspirit.Solus_Enduser_API(url='solusqueryaddress.com',
                                                    api_hash='API_HASH_for_your_server',
                                                    api_key='API_Key_for_your_server')


Get full server info::

    >>> solus_vm.get_full_info()

Get server status::

    >>> solus_vm.get_status()

Get server info::

    >>> solus_vm.get_info()

Reboot server::

    >>> solus_vm.server_reboot()

Shutdown server::

    >>> solus_vm.server_shutdown()

Boot server::

    >>> solus_vm.server_boot()


All enduser API calls for solusvm v1 are implemented with this. Hopefully with v2 there will be more available endpoints and settings.