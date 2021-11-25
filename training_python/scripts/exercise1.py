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


def addUpdate(id):
    body = {
        'entry': 'this ticket was updated'
    }
    results = client.call('SoftLayer_Ticket', 'addUpdate', body, id=id)
    for result in results:
        print(result)


def edit(id):
    body = {
        'statusId': 1002
    }
    contents = 'This is the content for edit a ticket'
    results = client.call('SoftLayer_Ticket', 'edit', body, contents, id=id)
    print(results)


def getAttachedFiles(id):
    results = client.call('SoftLayer_Ticket', 'getAttachedFiles', id=id)
    for result in results:
        print(result)


def createAdministrativeTicket():
    current_user = client.call('SoftLayer_Account', 'getCurrentUser')
    body = "I'm testing administrative API ticket creation. Please close this ticket if you see it. Thanks."
    new_ticket = {
        'subjectId': 1021,
        'assignedUserId': current_user['id'],
        'title': 'Testing Ticket from Python',
        'priority': 4
    }
    created_ticket = client.call('SoftLayer_Ticket', 'createAdministrativeTicket', new_ticket, body, None, None, None,
                                 None, None, 'HARDWARE')
    print(created_ticket)


def createCancelServerTicket():
    reason = 'Testing for cancel server ticket'
    content = 'This is the content for testing cancel server ticket'
    result = client.call('SoftLayer_Ticket', 'createCancelServerTicket', 123456, reason, content, None, 'HARDWARE')
    print(result)


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


def getAttachedHardware(id):
    results = client.call('SoftLayer_Ticket', 'getAttachedHardware', id=id)
    for result in results:
        print(result)


def getObject(id):
    results = client.call('SoftLayer_Ticket', 'getObject', id=id)
    print(results)


def getTicketsClosedSinceDate(id):
    results = client.call('SoftLayer_Ticket', 'getTicketsClosedSinceDate', id=id)
    print(results)


def getUpdates(id):
    results = client.call('SoftLayer_Ticket', 'getUpdates', id=id)
    for result in results:
        print(result)


def markAsViewed(id):
    results = client.call('SoftLayer_Ticket', 'markAsViewed', id=id)
    print(results)


def getAllObjects():
    results = client.call('SoftLayer_Ticket_Subject', 'getAllObjects')
    for result in results:
        print(result)


def addBulkPortalPermission(userId):
    res = client.call('SoftLayer_User_Customer_CustomerPermission_Permission', 'getAllObjects')
    for result in res:
        print(result)

    res = client.call('SoftLayer_User_Customer', 'getPermissions', id=userId)
    for result in res:
        print(result)

    permission = {
        'key': 'SE_4',
        'keyName': 'ANTI_MALWARE_MANAGE',
        'name': 'Manage Antivirus/Spyware'
    }
    result = client.call('SoftLayer_User_Customer', 'addBulkPortalPermission', permission, id=userId)
    print(result)


def createObject():
    password = 'SecurityPassword123-'
    user_template = {
        'username': 'testUsernameNov24',
        'firstName': 'API',
        'lastName': 'Learner',
        'email': 'someone@somewhere.com',
        'companyName': 'IBM',
        'address1': '123 api road',
        'city': 'Houston',
        'country': 'US',
        'postalCode': 'TX 77002',
        'userStatusId': 1001,
        'timezoneId': 107
    }
    created_user = client.call('SoftLayer_User_Customer', 'createObject', user_template, password, password)
    print(created_user)


def editObject(userId):
    user_template = {
        'address1': '123 api road edited',
    }
    created_user = client.call('SoftLayer_User_Customer', 'editObject', user_template, id=userId)
    print(created_user)


def getApiAuthenticationKeys(userId):
    results = client.call('SoftLayer_User_Customer', 'getApiAuthenticationKeys', id=userId)
    print(results)


def getChildUsers(userId):
    results = client.call('SoftLayer_User_Customer', 'getChildUsers', id=userId)
    for result in results:
        print(result)


def getHasFullHardwareAccessFlag(userId):
    results = client.call('SoftLayer_User_Customer', 'getHasFullHardwareAccessFlag', id=userId)
    print(results)


def getLoginAttempts(userId):
    results = client.call('SoftLayer_User_Customer', 'getLoginAttempts', id=userId)
    for result in results:
        print(result)


def getPortalLoginToken(username, password):
    results = client.call('SoftLayer_User_Customer', 'getPortalLoginToken', username, password)
    print(results)


def removeAllHardwareAccessForThisUser(userId):
    results = client.call('SoftLayer_User_Customer', 'removeAllHardwareAccessForThisUser', id=userId)
    print(results)


def removeAllVirtualAccessForThisUser(userId):
    results = client.call('SoftLayer_User_Customer', 'removeAllVirtualAccessForThisUser', id=userId)
    print(results)


def updateVpnPassword(newPassword, userId):
    results = client.call('SoftLayer_User_Customer', 'updateVpnPassword', newPassword, id=userId)
    print(results)


def securityQuestionGetAllObjects():
    results = client.call('SoftLayer_User_Security_Question', 'getAllObjects')
    for result in results:
        print(result)


# Run scripts
addUpdate(ticketId)
createAdministrativeTicket()
createCancelServerTicket()
createStandardTicket(current_user['id'])
edit(ticketId)
getAttachedFiles(ticketId)
getAttachedHardware(ticketId)
getObject(ticketId)
getTicketsClosedSinceDate(ticketId)
getUpdates(ticketId)
markAsViewed(ticketId)

## SoftLayer_Ticket_Subject
getAllObjects()

## SoftLayer_User_Customer
addBulkPortalPermission(current_user['id'])
createObject()
editObject(userId)
getApiAuthenticationKeys(current_user['id'])
getChildUsers(current_user['id'])
getHasFullHardwareAccessFlag(current_user['id'])
getLoginAttempts(current_user['id'])
getPortalLoginToken('SL38207400', 'LatinoAmerica123-')
removeAllHardwareAccessForThisUser(userId)
removeAllVirtualAccessForThisUser(userId)
updateVpnPassword('NewPassword123-', userId)

## SoftLayer_User_Security_Question
securityQuestionGetAllObjects()
