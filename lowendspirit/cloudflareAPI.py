import requests
from requests.auth import HTTPBasicAuth
import json
import pprint


class Cloudflare_Enduser_API:
    def __init__(self, cf_token, cf_email):
        self.cf_token = cf_token
        self.cf_email = cf_email
        self.headers = {
            'Content-Type': 'application/json',
            'X-Auth-Key': self.cf_token,
            'X-Auth-Email': self.cf_email
        }

    def cfQuery(self, domain_id='', endpoint='', data={}):
        """
        Main GET query function
        :param domain_id: ID of domain to query
        :param endpoint: user, zone, etc...
        :return: result cloudflare response
        """
        if not domain_id and not endpoint:
            #print('domain id and endpoint not set')
            return requests.get(api_endpoint + '/zones' + domain_id + endpoint, headers=self.headers)
        elif domain_id and endpoint:
            return requests.get(api_endpoint + '/zones/' + domain_id + '/' + endpoint, headers=self.headers)
        elif endpoint:
            return requests.get(api_endpoint + '/' + endpoint, headers=self.headers)

    def cfQuery_patch(self, data, endpoint):
        """
        Main PATCH query function
        :param domain_id: ID of domain to query
        :param endpoint: user, zone, etc...
        :param data: data to be patched
        :return: result cloudflare response
        """
        auth = HTTPBasicAuth(self.cf_email, self.cf_token)
        return requests.patch(api_endpoint + endpoint, data=json.dumps(data), auth=auth,
                              headers=self.headers)

    def cfQuery_post(self, data, endpoint):
        """
        Main POST query function
        :param data: data to be posted
        :return: cloudflare response
        """
        return requests.post(api_endpoint + endpoint, data=json.dumps(data), headers=self.headers)

    def cfQuery_delete(self, id, endpoint):
        return requests.delete(api_endpoint + endpoint + id, headers=self.headers)

    def cfQuery_put(self, data, endpoint):
        """
        Main POST query function
        :param data: data to be posted
        :return: cloudflare response
        """
        return requests.put(api_endpoint + endpoint, data=json.dumps(data), headers=self.headers)


    def pp_print_of(self, some_input):
        """
        Preaty print the output
        :param some_input: anything it can be a function too
        :return: function output with pprint
        """
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pprint(some_input)

    def list_all(self):
        """
        Get all data associated with cloudflare user
        :return: all data for the user account
        """
        r = self.cfQuery().json()
        pp = pprint.PrettyPrinter(indent=4)
        return pp.pprint(r)

    def list_domain_ids(self):
        """
        lists domain ID/'s
        :return: get list of all domain's and id's associated with cloudflare account
        """
        r = self.cfQuery().json()
        records = []
        for domain in r.get('result'):
            domain_name = domain.get('name')
            domain_id = domain.get('id')
            records.append((domain_name, domain_id))
        return dict(records)

    def get_record(self, id):
        """
        get dns records for given domain id
        :param id: you need to know the domain id that can be found through list_domain_ids function
        :return: return list of all dns records associated with domain
        """
        domains = self.list_domain_ids()
        endpoint = 'dns_records'  # endpoint of the query for CloudFlare API v4

        if str(id) in domains.values():
            r = self.cfQuery(domain_id=id, endpoint=endpoint)
            return r.json().get('result')[0].get('content')
        elif str(id) not in domains.values():
            return ''.join('There is no domain with id: ' + str(id) +
                           "\nlist od available domain id's is:\n" +
                           json.dumps(domains))

    def get_user(self):
        """
        Get user info
        :return: return user info
        """
        return self.cfQuery(endpoint='user').json()

    def patch_user(self, data):
        """
        Update your user profile
        :param data: dictionary of data to be changed,
        :return: PATCH request to update user profile
        """
        return self.cfQuery_patch(endpoint='/user', data=data)

    def get_user_billing_profile(self, x):
        """
        User Billing Profile
        :param x: cloudflare app endpoint (profile, history)
        :return: current billing profile
        """
        return self.cfQuery(endpoint='user/billing/' + x).json()

    def get_app_subscriptions(self, x=None):
        """
        List all of your app subscriptions
        :param x: optional parameter to show info for app
        :return: list
        """
        if x:
            return self.cfQuery(endpoint='user/billing/subscriptions/apps' + '/' + x).json()
        return self.cfQuery(endpoint='user/billing/subscriptions/apps').json()

    ######## FOR NOW WILL LEAVE OUT REST OF PAYED API CALLES

    def get_firewall_rules(self):
        """
        List firewall access rules
        :param x: optional parameter to show info for app
        :return: list
        """
        return self.cfQuery(endpoint='/user/firewall/access_rules/rules').json()

    def set_access_rule(self, data):
        return self.cfQuery_post(data, endpoint='/user/firewall/access_rules/rules').json()

    def update_access_rule(self, data):
        return self.cfQuery_patch(data, endpoint='/user/firewall/access_rules/rules').json()

    def del_access_rule(self, id):
        return self.cfQuery_delete(id, endpoint='/user/firewall/access_rules/rules/').json()

    ################################################################
    ########## Domain related

    def add_new_zone(self, data):
        #return self.cfQuery_post(data, endpoint='/zones')
        pass

    def get_zone_details(self, id):
        return self.cfQuery(domain_id=id).json()

    ################################################################
    ############## DNS Record

    def create_dns_record(self, id, data):
        return self.cfQuery_post(data, endpoint='/zones/' + id + '/dns_records').json()

    def get_dns_records(self, id):
        endpoint = '/dns_records'
        return self.cfQuery(domain_id=id, endpoint=endpoint).json()

    def get_dns_record_details(self, id, record_id):
        endpoint = '/dns_records/' + record_id
        return self.cfQuery(domain_id=id, endpoint=endpoint).json()

    def update_dns_record(self, data):
        endpoint = '/zones/' + data.get('zone_id') + '/dns_records/' + data.get('id')
        return self.cfQuery_put(data, endpoint=endpoint).json()

    def del_dns_record(self, zone_id, domain_id):
        endpoint = '/zones/' + zone_id + '/dns_records/'
        return self.cfQuery_delete(id=domain_id, endpoint=endpoint).json()

    #################################################################
    ################## Analytics

    def get_zone_analytics(self, zone_id):
        endpoint = 'analytics/dashboard'
        return self.cfQuery(domain_id=zone_id, endpoint=endpoint).json()


    ##################################################################
    ################## Zone Firewall rules

    def get_zone_firewall_rules(self, zone_id):
        endpoint = 'firewall/access_rules/rules'
        return self.cfQuery(domain_id=zone_id, endpoint=endpoint).json()

    def create_zone_firewall_rule(self, zone_id, data):
        endpoint = '/zones/' + zone_id + '/firewall/access_rules/rules'
        return self.cfQuery_post(data=data, endpoint=endpoint).json()

    def update_zone_firewall_rule(self, zone_id, data):
        endpoint = '/zones/' + zone_id + '/firewall/access_rules/rules'
        return self.cfQuery_patch(data=data, endpoint=endpoint)

    def del_zone_firewall_rule(self, zone_id, data):
        endpoint = '/zones/' + zone_id + '/firewall/access_rules/rules'
        #return self.cfQuery_delete(id=data.get(id), endpoint=endpoint)
        pass




