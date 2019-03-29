class MABDeviceAdd(self):

	import hashlib

	def __init__(self):
		self.endpoint_name = ''
		self.endpoint_id = ''
		self.endpoint_description = ''
		self.group_id = ''
		self.identity_store = ''
		self.endpoint_mac_address = ''
		self.portal_user = ''
		self.profile_id = ''
		
	
	def get_endpoint_name(self):
		self.endpoint_name = input('Enter the Enpoint Name: ')
		
		
	def get_endpoint_description(self):
		self.endpoint_description = input('Enter a description for the Endpoint: ')
		
		
	def get_group_id(self):
		self.group_id = input('Enter the group ID of the Endpoint: ')
		
		
	def get_identity_store(self):
		self.i
		dentity_store = input('Enter the Identity Store of the Endpoint: ')
		
	def get_endpoint_mac_address(self):
		self.endpoint_mac_address = input('Enter the MAC address of the endpoint: ')
		
		
	def get_portal_user(self):
		self.portal_user = input('Enter your ISE API username: ')
		
		
	def get_profile_id(self):
		self.profile_id = input('Enter the Profile ID of the Enpoint: ')
		
		
	def generate_endpoint_id(self):
		self.endpoint_id = hashlib.sha256(self.endpoint_mac_address)
		
		
	def enpoint_add_api_post_output(self):
	
		#Method: GET
		#URI: https://ISE_IP_ADDRESS:9060/ers/config/endpoint
		#HTTP Accept header:application/vnd.com.cisco.ise.identity.endpoint.1.0+xml 
		
		print(	
		'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
		'<ns3:endpoint',
			'name='+self.endpoint_name,
			'id='+self.endpoint_id,
			'description='+self.endpoint_description,
			'xmlns:ns2="ers.ise.cisco.com"',
			'xmlns:ns3="identity.ers.ise.cisco.com">',
			'<groupId>'+self.group_id+'</groupId>',
			'<identityStore>'+self.identity_store+'</identityStore>',
			'<identityStoreId>'self.identity_store+'</identityStoreId>',
			'<mac>'+self.endpoint_mac_address+'</mac>',
			'<portalUser>'+self.portal_user+'</portalUser>',
			'<profileId>'+self.profile_id+'</profileId>',
			'<staticGroupAssignment>true</staticGroupAssignment>',
			'<staticProfileAssignment>false</staticProfileAssignment>',
		'</ns3:endpoint>')