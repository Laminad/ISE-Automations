class NetworkDeviceAdd(self):


	import hashlib
	
	
	def __init__(self):
		self.device_id = ''
		self.device_hostname = ''
		self.ise_ip_address = ''
		self.radius_shared_secret = ''
		self.device_ip_address = ''
		self.device_subnet_mask = '32'
		self.device_group = ''
		self.device_location = ''
		self.snmp_version = 'TWO_C'
		self.snmp_community_string = ''
		
		
	def get_device_hostname(self): 
		self.device_hostname = input('Enter the device hostname: ')
		
		
	def get_device_ip_address(self):
		self.device_ip_address = input('Enter the device IP Address: ')
	
	
	def get_ise_ip_address(self):
		self.ise_ip_address = input('Enter the IP address of the ISE ERS enabled node: ')
		
		
	def get_radius_shared_secert(self):
		self.radius_shared_secert = input('Enter the RADIUS Shared Secert: ')	
	
	
	def get_device_group(self):
		self.device_group = input('Enter the Device Group: ')
		
		
	def get_device_location(self):
		self.device_location = input('Enter the device location: ')
		
		
	def get_snmp_community_string(self):
		self.snmp_community_string = input('Enter the device snmp community string: ')
		
		
	def generate_device_id(self):
		self.device_id = hashlib.sha256(self.device_hostname)
		
		
	def print_network_add_api_post(self):
	
		#Method: POST
		#URI: https://ISE_IP_ADDRESS:9060/ers/config/networkdevice
		#Content-Type: application/vnd.com.cisco.ise.network.networkdevice.1.1+xml; charset=utf-8

		print(
		"<?xml version='1.0' encoding='UTF-8' standalone='yes'?>",
			"<ns4:networkdevice", 
				"id="+self.device_id,
				"name="+self.device_name,
				"xmlns:ers='ers.ise.cisco.com'",
				"xmlns:xs='http://www.w3.org/2001/XMLSchema'",
				"xmlns:ns4='network.ers.ise.cisco.com'>",
				"<link rel='self' href='https://"+self.ise_ip_address+":9060/ers/config/networkdevice/"+self.device_id+"' type='application/xml'/>",
				"<authenticationSettings>",
					"<enableKeyWrap>false</enableKeyWrap>",
					"<keyInputFormat>ASCII</keyInputFormat>",
					"<networkProtocol>RADIUS</networkProtocol>",
					"<radiusSharedSecret>"+self.radius_shared_secret+"</radiusSharedSecret>",
				"</authenticationSettings>",
				"<coaPort>1700</coaPort>",
				"<NetworkDeviceIPList>",
					"<NetworkDeviceIP>",
						"<ipaddress>"+self.device_ip_address+"</ipaddress>",
						"<mask>"+self.device_subnet_mask+"</mask>",
					"</NetworkDeviceIP>",
				"</NetworkDeviceIPList>",
				"<NetworkDeviceGroupList>",
					"<NetworkDeviceGroup>"+self.device_group+"</NetworkDeviceGroup>",
					"<NetworkDeviceGroup>"+self.device_location+"</NetworkDeviceGroup>",
				"</NetworkDeviceGroupList>",
				"<profileName>Cisco</profileName>",
				"<snmpsettings>",
					"<linkTrapQuery>true</linkTrapQuery>",
					"<macTrapQuery>true</macTrapQuery>",
					"<originatingPolicyServicesNode>Auto</originatingPolicyServicesNode>",
					"<pollingInterval>28800</pollingInterval>",
					"<roCommunity>"+self.snmp_community_string+"</roCommunity>",
					"<version>"+self.snmp_version+"</version>",
				"</snmpsettings>",
			"</ns4:networkdevice>")
		

	if __name__ == '__main__':
		#Collecting Device details.
		self.get_device_hostname()
		self.get_device_ip_address()
		self.get_ise_ip_address()
		self.get_radius_shared_secret()
		self.get_device_group()
		self.get_device_location()
		self.get_snmp_community_string()
		
		#Using Device details to input missing API values.
		self.generate_device_id()
		self.print_network_add_api_post()
		
		