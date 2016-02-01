Quickstart
==========

First, make sure you have installed lowendspirit.

Let's get startde with some simple examples:

Begin with importing lowendspirit module::

    >>> import lowendspirit


Cloudflare
----------

Now, let's create cloudflare object::

    >>> cloud_flare = lowendspirit.Cloudflare_Enduser_API(cf_email='yourcfemail@example.com',
                                                          cf_token='your_cloudflare_API_key')
    >>> # get all data associated with your account
    >>> cloud_flare.list_all()


Example, output::

    {   'errors': [],
        'messages': [],
        'result': [   {   'created_on': '2016-01-28T10:01:00.746824Z',
                          'development_mode': 0,
                          'id': '',
                          'meta': {   'custom_certificate_quota': 0,
                                      'multiple_railguns_allowed': False,
                                      'page_rule_quota': '3',
                                      'phishing_detected': False,
                                      'step': 4,
                                      'wildcard_proxiable': False},
                          'modified_on': '2016-01-28T10:10:54.444469Z',
                          'name': 'domain1.net',
                          'name_servers': [   'elle.ns.cloudflare.com',
                                              'josh.ns.cloudflare.com'],
                          'original_dnshost': None,
                          'original_name_servers': [   'dns1.registrar-servers.com',
                                                       'dns5.registrar-servers.com',
                                                       'dns4.registrar-servers.com',
                                                       'dns3.registrar-servers.com',
                                                       'dns2.registrar-servers.com'],
                          'original_registrar': None,
                          'owner': {   'email': 'yourcfemail@example.com',
                                       'id': '',
                                       'type': 'user'},
                          'paused': False,
                          'permissions': [   '#analytics:read',
                                             '#billing:edit',
                                             '#billing:read',
                                             '#cache_purge:edit',
                                             '#dns_records:edit',
                                             '#dns_records:read',
                                             '#lb:edit',
                                             '#lb:read',
                                             '#logs:read',
                                             '#organization:edit',
                                             '#organization:read',
                                             '#ssl:edit',
                                             '#ssl:read',
                                             '#waf:edit',
                                             '#waf:read',
                                             '#zone:edit',
                                             '#zone:read',
                                             '#zone_settings:edit',
                                             '#zone_settings:read'],
                          'plan': {   'can_subscribe': True,
                                      'currency': 'USD',
                                      'externally_managed': False,
                                      'frequency': '',
                                      'id': '0feeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
                                      'is_subscribed': True,
                                      'legacy_id': 'free',
                                      'name': 'Free Website',
                                      'price': 0},
                          'status': 'active',
                          'type': 'full'},
                      {   'created_on': '2016-01-23T10:49:25.162252Z',
                          'development_mode': 0,
                          'id': '',
                          'meta': {   'custom_certificate_quota': 0,
                                      'multiple_railguns_allowed': False,
                                      'page_rule_quota': '3',
                                      'phishing_detected': False,
                                      'step': 4,
                                      'wildcard_proxiable': False},
                          'modified_on': '2016-01-29T13:38:36.716124Z',
                          'name': 'domain2.com',
                          'name_servers': [   'elle.ns.cloudflare.com',
                                              'josh.ns.cloudflare.com'],
                          'original_dnshost': None,
                          'original_name_servers': [   'dns3.registrar-servers.com',
                                                       'dns5.registrar-servers.com',
                                                       'dns4.registrar-servers.com',
                                                       'dns1.registrar-servers.com',
                                                       'dns2.registrar-servers.com'],
                          'original_registrar': None,
                          'owner': {   'email': 'yourcfemail@example.com',
                                       'id': '',
                                       'type': 'user'},
                          'paused': False,
                          'permissions': [   '#analytics:read',
                                             '#billing:edit',
                                             '#billing:read',
                                             '#cache_purge:edit',
                                             '#dns_records:edit',
                                             '#dns_records:read',
                                             '#lb:edit',
                                             '#lb:read',
                                             '#logs:read',
                                             '#organization:edit',
                                             '#organization:read',
                                             '#ssl:edit',
                                             '#ssl:read',
                                             '#waf:edit',
                                             '#waf:read',
                                             '#zone:edit',
                                             '#zone:read',
                                             '#zone_settings:edit',
                                             '#zone_settings:read'],
                          'plan': {   'can_subscribe': True,
                                      'currency': 'USD',
                                      'externally_managed': False,
                                      'frequency': '',
                                      'id': '0feeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
                                      'is_subscribed': True,
                                      'legacy_id': 'free',
                                      'name': 'Free Website',
                                      'price': 0},
                          'status': 'active',
                          'type': 'full'}],
        'result_info': {   'count': 2,
                           'page': 1,
                           'per_page': 20,
                           'total_count': 2,
                           'total_pages': 1},
        'success': True}
    >>>


If you have more then 2 domains then the list goes on.

SolusVM
-------

Create SolusVM object::

    >>> solus_vm = lowendspirit.Solus_Enduser_API(url='solusqueryaddress.com',
                                                  api_hash='API_HASH_for_your_server',
                                                  api_key='API_Key_for_your_server')
    >>> # get full server info
    >>> solus_vm.get_full_info()

Example output::

    >>>
        {   'bw': '536870912000,731629,536870180371,0',
        'hdd': '2147483648,434012160,1713471488,20',
        'hostname': 'your_hostname',
        'ipaddr': '192.168.0.146,2a00:xxx:x:xxx::xxxx:xxxx',
        'ipaddress': '192.168.0.146',
        'mem': '134217728,5668864,128548864,4',
        'status': 'success',
        'statusmsg': '',
        'vmstat': ''}
    >>>

Virtulizor
----------

Create virtualizor object::

    >>> virtualizor = lowendspirit.Virtualizor_Enduser_API(apikey="your_api_key",
                                                           apiip="my.panel.com",
                                                           apipass="your_api_pass",
                                                           apiprotocol='http',
                                                           apiport='4082')
    >>> # get list of vm's in your account
    >>> virtualizor.listvs()

If you want to use `https` protocol then you don't need to pass it as argument, also in that case don't pass `apiport`, it will default  to https and 4083.
For example::

    >>> virtualizor = lowendspirit.Virtualizor_Enduser_API(apikey="your_api_key",
                                                           apiip="my.panel.com",
                                                           apipass="your_api_pass")

Example output for `listvs()` gives you the ID's of server's under your account::

    >>> dict_keys([7625])
    >>>

If you have more then one server in your account that list will be longer.


