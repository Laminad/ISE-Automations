from datetime import datetime as dt
import hashlib
import requests
import sys


class MABDeviceAdd():
	
	def __init__(self):
		self.endpoint_name = ''
		self.endpoint_id = ''
		self.endpoint_description = ''
		self.group_id = ''
		self.identity_store = ''
		self.identity_store_id = ''
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
		self.identity_store = input('Enter the Identity Store of the Endpoint: ')
		
	def get_endpoint_mac_address(self):
		self.endpoint_mac_address = input('Enter the MAC address of the endpoint: ')
		
		
	def get_portal_user(self):
		self.portal_user = input('Enter your ISE API username: ')
		
		
	def get_profile_id(self):
		self.profile_id = input('Enter the Profile ID of the Enpoint: ')
		
		
	def generate_endpoint_id(self):
		self.endpoint_id = hashlib.sha256(self.endpoint_mac_address)
		
		
	def enpoint_add_api_post_output(self):
	
		#Method: PUT
		#URI: https://ISE_IP_ADDRESS:9060/ers/config/endpoint
		#HTTP Accept header:application/vnd.com.cisco.ise.identity.endpoint.1.0+xml 

		device = """
		<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
			<ns3:endpoint name={} id={} description={} xmlns:ns2='ers.ise.cisco.com' xmlns:ns3='identity.ers.ise.cisco.com'>
				<groupId>{}</groupId>
				<identityStore>{}</identityStore>
				<identityStoreId>{}</identityStoreId>
				<mac>{}</mac>
				<portalUser>{}</portalUser>
				<profileId>{}</profileId>
				<staticGroupAssignment>true</staticGroupAssignment>
				<staticProfileAssignment>false</staticProfileAssignment>
			</ns3:endpoint>
		""".format(self.endpoint_name, self.endpoint_id, self.endpoint_description, self.group_id, self.identity_store, self.identity_store_id, self.endpoint_mac_address, self.portal_user, self.profile_id)