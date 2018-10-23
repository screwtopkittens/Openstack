import pyrax
import os

USER = "none"
API_KEY = "non"
cs = pyrax.cloudservers


print " Welcome to Dans Amazing cloud server configuration tool please see the menu below and select an Action"
print "1. Build Standard Server"
print "2. Show built server details"
print "3. delete server"
print "4. Set User name and API key"
action = raw_input("Enter a selection: ")

if action == "4":
  USER = raw_input("Enter Your Username: ")
  API_KEY = raw_input("Enter Your API KEY: ")
  
##Sets API Credentials 
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_default_region('IAD')
pyrax.set_credentials(USER, API_KEY)

##obtains images list
images = pyrax.images.list()

##Obtains Flavour list
flavor_list = cs.list_flavors()




##This sets the image and flavour Varibles
#image = pyrax.images.get('907770dd-ddf4-4281-afda-f9d25125c1bd')
# flavor = cs.flavors.get('3')

##Generates Keypair to use for authentication with server##
#public_key = open(os.path.expanduser("~/.ssh/id_rsa.pub")).read()
#keypair = cs.keypairs.create("mykeypair", public_key)

##Builds Server##
#server = cs.servers.create('test', image.id, flavor.id, key_name=keypair.name)
#pyrax.utils.wait_for_build(server_dan, verbose=True)


##displayS ASSOCIATED ADDRESSES WITH CREATED SERVER##
#server.addresses

##dELETES server##
#server.delete()
