require 'rubygems'
require 'softlayer_api'

username = 'SL38207400'
api_key = '6cbcf6b75c8da7271ea3ea956d0646dc9388aeeeb5d9393d5a7d2f1734edb5d7'
endpoint_url = "http://r128206.application.qadal1301.softlayer.local/v3/sldn/xmlrpc/"
client = SoftLayer::Client.new(:username => username, :api_key => api_key, :endpoint_url => endpoint_url)

def listTicketsById(client, userId)
  begin
    result = client['SoftLayer_Account'].object_with_id(userId).getTickets
    result.each do
    |ticket| puts ticket['id']
    end
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

userId = 9356615
listTicketsById(client, userId)
