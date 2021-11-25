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


def createStandardTicket(userId):
    body = "I'm testing API ticket creation. Please close this ticket if you see it. Thanks."
    new_ticket = {
        'subjectId': 1021,
        'assignedUserId': userId,
        'title': 'Testing Ticket from Python',
        'priority': 4
    }
    created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', new_ticket, body, None, None, None, None,
                                 None, 'HARDWARE')
    print(created_ticket)


def list_tickets(userId):
    results = client.call('SoftLayer_Account', 'getTickets', id=userId)
    for result in results:
        print(result)


def addUpdate(id):
    body = {
        'entry': 'this ticket was updated'
    }
    results = client.call('SoftLayer_Ticket', 'addUpdate', body, id=id)
    for result in results:
        print(result)


createStandardTicket(current_user['id'])
list_tickets(current_user['id'])
addUpdate(ticketId)
