require 'rubygems'
require 'softlayer_api'

username = 'SL38207400'
api_key = '6cbcf6b75c8da7271ea3ea956d0646dc9388aeeeb5d9393d5a7d2f1734edb5d7'
endpoint_url = "http://r128206.application.qadal1301.softlayer.local/v3/sldn/xmlrpc/"
client = SoftLayer::Client.new(:username => username, :api_key => api_key, :endpoint_url => endpoint_url)

def listStatusIdTicket(client, userId, statusId)
  object_filter = SoftLayer::ObjectFilter.new do |filter|
    filter.accept("tickets.statusId").when_it is(statusId)
  end
  begin
    result = client['SoftLayer_Account'].object_filter(object_filter).object_with_id(userId).getTickets
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def betweenDates(client, userId, startDate, endDate)
  object_filter = SoftLayer::ObjectFilter.new do |filter|
    filter.accept("tickets.createDate").when_it is_between_dates(startDate, endDate)
  end
  begin
    result = client['SoftLayer_Account'].object_filter(object_filter).object_with_id(userId).getTickets
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

userId = 9356615
statusOpen = 1001
statusClosed = 1002
listStatusIdTicket(client, userId, statusOpen)
listStatusIdTicket(client, userId, statusClosed)

startDate = '11/28/2021 00:00:00'
endDate = '11/30/2021 00:00:00'
betweenDates(client, userId, startDate, endDate)
