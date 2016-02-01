CloudFlare API v4!
==================

Initiate the Cloudflare object::

    >>> cloud_flare = lowendspirit.Cloudflare_Enduser_API(cf_email='yourcfemail@example.com',
                                                          cf_token='your_cloudflare_API_key')

List all data associated with your account
------------------------------------------

    >>> cloud_flare.list_all()

List all domains and their ID's
-------------------------------

    >>> cloud_flare.list_domain_ids()

Return list of all dns records associated with domain
-----------------------------------------------------

    >>> cloud_flare.get_record(id='domain_id')

you need to get `id` from previous function `list_domain_ids()`.

Get user info or your current details
-------------------------------------

    >>> cloud_flare.get_user()

Update user
-----------

    >>> data = {"first_name":"John","last_name":"Appleseed","telephone":"+1 123-123-1234","country":"US","zipcode":"12345"}
    >>> cloud_flare.patch_user(data)

Get user billing profile
------------------------

    >>> cloud_flare.get_user_billing_profile('profile')

or

    >>> cloud_flare.get_user_billing_profile('history')

for full list of available api endpoints visit https://api.cloudflare.com/

Firewall rules
--------------

Get list of firewall rules::

    >>> cloud_flare.get_firewall_rules()

Set firewall rule for all domains under your account::

    >>> rule = {"mode": "challenge", "configuration": {"target": "ip", "value": "1.2.3.4"},
                "notes": "This rule is on because of an event that occured on date X"}
    >>> cloud_flare.set_access_rule(data=rule)

Update firewall rule::

    >>> rule = {"mode": "block", "configuration": {"target": "ip", "value": "1.2.3.4"},
                "notes": "This rule is on because of an event that occured on date X"}
    >>> cloud_flare.update_access_rule()

Delete firewall rule::

    >>> cloud_flare.del_access_rule(id='id_of_rule_to_be_deleted')

To get `id` of the rule to delete get list of firewall rules first.

ZONE related
------------

Create new zone::

    >>> not implemented yet

Get zone details::

    >>> cloud_flare.get_zone_details(id='zone_id')


DNS Records
-----------

Create DNS record::

    >>> data = {"type": "A", "name":"your_domain.com", "content": "127.0.0.1", "ttl": 120}
    >>> cloud_flare.create_dns_record(id='zone_id', data=data)

you get `zone_id` with `list_domain_ids()` first.

Get list of dns records::

    >>> cloud_flare.get_dns_records(id='zone_id')

Get details of the dns record::

    >>> cloud_flare.get_dns_record_details(id='zone_id', record_id='record_id')

Update DNS record::

    >>> data = {"id": "a3d143047e57c6479c3a3a8328c21917",
                "type": "A",
                "name": "example.com",
                "content": "1.2.3.4",
                "proxiable": True,
                "proxied": False,
                "ttl": 120,
                "locked": False,
                "zone_id": "6261e6e9c365e4db31d68046982f84f6",
                "zone_name": "example.com",
                "created_on": "2014-01-01T05:20:00.12345Z",
                "modified_on": "2014-01-01T05:20:00.12345Z",
                "data": {}}
    >>> cloud_flare.update_dns_record(data=data)

Delete DNS record::

    >>> cloud_flare.del_dns_record(zone_id='zone_id', domain_id='domain_id')

Analytics
---------

    >>> cloud_flare.get_zone_analytics(zone_id='zone_id')

Zone firewall rules
-------------------

Get zone firewall rules::

    >>> cloud_flare.get_zone_firewall_rules(zone_id='zone_id')

Create zone firewall rule::

    >>> data = {"mode": "challenge",
                "configuration": {"target": "ip", "value": "127.0.0.7"},
                "notes": "This rule is on because of an event that occured on date X"}
    >>> cloud_flare.create_zone_firewall_rule(zone_id='zone_id', data=data)

Update zone firewall rule::

    >>> data = {"mode": "challenge",
                "configuration": {"target": "ip", "value": "127.0.0.7"},
                "notes": "This rule is on because of an event that occured on date X"}
    >>> cloud_flare.update_zone_firewall_rule(zone_id='zone_id', data=data)

Delete zone firewall rule::

    >>> not implemented yet


