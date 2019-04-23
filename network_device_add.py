import hashlib as hl

class NetworkDeviceAdd:


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


	def get_radius_shared_secret(self):
		self.radius_shared_secret = input('Enter the RADIUS Shared secret: ')	


	def get_device_group(self):
		self.device_group = input('Enter the Device Group: ')


	def get_device_location(self):
		self.device_location = input('Enter the device location: ')


	def get_snmp_community_string(self):
		self.snmp_community_string = input('Enter the device snmp community string: ')


	def generate_device_id(self):
		hostname = self.device_hostname.encode(encoding='UTF-8', errors='strict')
		self.device_id = hl.sha256(hostname).hexdigest()


	def print_network_add_api_post(self):

		#Method: POST
		#URI: https://ISE_IP_ADDRESS:9060/ers/config/networkdevice
		#Content-Type: application/vnd.com.cisco.ise.network.networkdevice.1.1+xml; charset=utf-8

		print(
		"<?xml version='1.0' encoding='UTF-8' standalone='yes'?>\n"
			"<ns4:networkdevice\n" 
				"id="+self.device_id+"\n"
				"name="+self.device_hostname+"\n"
				"xmlns:ers='ers.ise.cisco.com'\n"
				"xmlns:xs='http://www.w3.org/2001/XMLSchema'\n"
				"xmlns:ns4='network.ers.ise.cisco.com'>\n"
				"<link rel='self' href='https://"+self.ise_ip_address+":9060/ers/config/networkdevice/"+self.device_id+"' type='application/xml'/>\n"
				"<authenticationSettings>\n"
					"<enableKeyWrap>false</enableKeyWrap>\n"
					"<keyInputFormat>ASCII</keyInputFormat>\n"
					"<networkProtocol>RADIUS</networkProtocol>\n"
					"<radiusSharedSecret>"+self.radius_shared_secret+"</radiusSharedSecret>\n"
				"</authenticationSettings>\n"
				"<coaPort>1700</coaPort>\n"
				"<NetworkDeviceIPList>\n"
					"<NetworkDeviceIP>\n"
						"<ipaddress>"+self.device_ip_address+"</ipaddress>\n"
						"<mask>"+self.device_subnet_mask+"</mask>\n"
					"</NetworkDeviceIP>\n"
				"</NetworkDeviceIPList>\n"
				"<NetworkDeviceGroupList>\n"
					"<NetworkDeviceGroup>"+self.device_group+"</NetworkDeviceGroup>\n"
					"<NetworkDeviceGroup>"+self.device_location+"</NetworkDeviceGroup>\n"
				"</NetworkDeviceGroupList>\n"
				"<profileName>Cisco</profileName>\n"
				"<snmpsettings>\n"
					"<linkTrapQuery>true</linkTrapQuery>\n"
					"<macTrapQuery>true</macTrapQuery>\n"
					"<originatingPolicyServicesNode>Auto</originatingPolicyServicesNode>\n"
					"<pollingInterval>28800</pollingInterval>\n"
					"<roCommunity>"+self.snmp_community_string+"</roCommunity>\n"
					"<version>"+self.snmp_version+"</version>\n"
				"</snmpsettings>\n"
			"</ns4:networkdevice>\n")


		
if __name__ == '__main__':
	nda = NetworkDeviceAdd()
	nda.get_device_hostname()
	nda.get_device_ip_address()
	nda.get_ise_ip_address()
	nda.get_radius_shared_secret()
	nda.get_device_group()
	nda.get_device_location()
	nda.get_snmp_community_string()

	#Using Device details to input missing API values.
	nda.generate_device_id()
	nda.print_network_add_api_post()
