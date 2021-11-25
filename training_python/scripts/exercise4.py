import SoftLayer

username = 'SL38207400'
api_key = '6cbcf6b75c8da7271ea3ea956d0646dc9388aeeeb5d9393d5a7d2f1734edb5d7'
endpoint_url = "http://r128206.application.qadal1301.softlayer.local/v3/sldn/rest"
client = SoftLayer.create_client_from_env(username,
                                          api_key,
                                          endpoint_url)

ticketId = 138769271
userId = 9356615
current_user = client.call('SoftLayer_Account', 'getCurrentUser')


def list_tickets_show_only_id(userId):
    results = client.call('SoftLayer_Account', 'getTickets', id=userId)
    for result in results:
        print(result['id'])


list_tickets_show_only_id(current_user['id'])
