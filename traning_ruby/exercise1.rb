require 'rubygems'
require 'softlayer_api'

username = 'sl307608-dcabero'
api_key = 'edeef0ba3714d992cf67ca170204d3cafaf10028d6933deaf7e0cc61a3b81028'
endpoint_url = "https://api.softlayer.com/xmlrpc/v3.1/"
client = SoftLayer::Client.new(:username => username, :api_key => api_key, :endpoint_url => endpoint_url)

def captureImage(client, virtual_guest_id)
  capture_template = {
    'description' => 'test',
    'name' => 'reloadFlexImage',
    'summary' => 'test summary',
    'volumes' => {
      'bootVolumeFlag' => false,
      'name' => 'imageVolume'
    }
  }
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).captureImage(capture_template)
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def createArchiveTransaction(client, virtual_guest_id)
  blockDevices = {
    'device' => 'Name Device'
  }
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).createArchiveTransaction("Name", blockDevices, "note")
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def createObject(client, productOrder)
  begin
    order = client['SoftLayer_Virtual_Guest'].createObject(productOrder)
    pp order
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def deleteObject(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).deleteObject
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def findByIpAddress(client, ipAddress)
  begin
    result = client['SoftLayer_Virtual_Guest'].findByIpAddress(ipAddress)
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def generateOrderTemplate(client, templateOrder)
  begin
    result = client['SoftLayer_Virtual_Guest'].generateOrderTemplate(templateOrder)
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getActiveTransaction(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getActiveTransaction
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getBandwidthImageByDate(client, virtual_guest_id, starDate, endDate, networkType)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getBandwidthImageByDate(starDate, endDate, networkType)
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getBlockDevices(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getBlockDevices
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getCreateObjectOptions(client)
  begin
    result = client['SoftLayer_Virtual_Guest'].getCreateObjectOptions
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getMonitoringAgents(client)
  begin
    result = client['SoftLayer_Virtual_Guest'].getMonitoringAgents
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getObject(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getObject
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getOperatingSystem(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getOperatingSystem
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getOrderTemplate(client, virtual_guest_id, billingType)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getOrderTemplate(billingType)
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getPowerState(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getPowerState
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getPrimaryNetworkComponent(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getPrimaryNetworkComponent
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def getSecurityScanRequests(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).getSecurityScanRequests
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def isPingable(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).isPingable
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

def reloadCurrentOperatingSystemConfiguration(client, virtual_guest_id)
  begin
    result = client['SoftLayer_Virtual_Guest'].object_with_id(virtual_guest_id).reloadCurrentOperatingSystemConfiguration
    pp result
  rescue Exception => exception
    puts "Unable to retrieve account information: #{exception}"
  end
end

# Parameters
virtual_guest_id = 126291644
ipAddress = "75.126.18.181"
productOrder = {
  "hostname" => "host1",
  "domain" => "example.com",
  'datacenter' => { 'name' => 'dal05' },
  "startCpus" => 1,
  "maxMemory" => 1024,
  "hourlyBillingFlag" => true,
  "localDiskFlag" => true,
  "operatingSystemReferenceCode" => "UBUNTU_LATEST"
}

starDate = '[11 / 28 / 2021]'
endDate = '[11 / 30 / 2021]'
networkType = 'public'


# Run scripts
captureImage(client, virtual_guest_id)
createArchiveTransaction(client, virtual_guest_id)
create_Object(client, productOrder)
deleteObject(client, virtual_guest_id)
findByIpAddress(client, ipAddress)
generateOrderTemplate(client, productOrder)
getActiveTransaction(client, virtual_guest_id)
getBandwidthImageByDate(client, virtual_guest_id, starDate, endDate, networkType)
getBlockDevices(client, virtual_guest_id)
getCreateObjectOptions(client)
getMonitoringAgents(client)
getObject(client, virtual_guest_id)
getOperatingSystem(client, virtual_guest_id)
getOrderTemplate(client, virtual_guest_id, 'HOURLY')
getPowerState(client, virtual_guest_id)
getPrimaryNetworkComponent(client, virtual_guest_id)
getSecurityScanRequests(client, virtual_guest_id)
isPingable(client, virtual_guest_id)
reloadCurrentOperatingSystemConfiguration(client, virtual_guest_id)
