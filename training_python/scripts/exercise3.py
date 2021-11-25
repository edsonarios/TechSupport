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


def list_tickets_closed(userId):
    object_filter = {
        "tickets": {
            'status': {
                'name': {
                    'operation': 'Closed'
                }
            }
        }
    }
    results = client.call('SoftLayer_Account', 'getTickets', id=userId, filter=object_filter)
    for result in results:
        print(result)


def list_tickets_open(userId):
    object_filter = {
        "tickets": {
            'status': {
                'name': {
                    'operation': 'Open'
                }
            }
        }
    }
    results = client.call('SoftLayer_Account', 'getTickets', id=userId, filter=object_filter)
    for result in results:
        print(result)


def list_tickets_betweenDate(userId):
    object_filter = {
        "tickets": {
            'createDate': {
                'operation': 'betweenDate',
                'options': [{
                    'name': 'startDate',
                    'value': ['11 / 24 / 2021']
                },
                    {
                        'name': 'endDate',
                        'value': ['11/25/2021']
                    }]
            }
        }
    }
    results = client.call('SoftLayer_Account', 'getTickets', id=userId, filter=object_filter)
    for result in results:
        print(result)


list_tickets_closed(current_user['id'])
list_tickets_open(current_user['id'])
list_tickets_betweenDate(current_user['id'])
