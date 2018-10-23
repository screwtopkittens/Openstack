import pyrax
import os

USER = raw_input("Enter Your Username: ")
API_KEY = raw_input("Enter Your API KEY: ")

##Sets API Credentials 
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_default_region('IAD')
pyrax.set_credentials(USER, API_KEY)
cs = pyrax.cloudservers
imgs = cs.images.list()
flvs = cs.list_flavors()

def BUILD_CUSTOM_SERVER():
  ##This sets the image and flavour Varibles
  SERVER_NAME = raw_input("Enter the server name: ")
  IMAGE_VAR = raw_input("Enter the image uuid: ")
  FLAVOR_VAR = raw_input("Enter the flavor id: ")
  KEY_PAIR_NAME = raw_input("Enter the SSH key name: ")
  image = cs.images.get(IMAGE_VAR)
  flavor = cs.flavors.get(FLAVOR_VAR)
  return;

##selects task
print " Welcome to Dans Amazing cloud server configuration tool please see the menu below and select an Action"
print "1. Build Standard Server"
print "2. Show built server details"
print "3. delete server"
print "4. show avalible images"
print "5. show avalible flavors"
action = raw_input("Enter a selection: ")

if action == "1":
  BUILD_CUSTOM_SERVER()
  
if action == "2":
  print cs.servers.list()
  
if action == "3":
  ##dELETES server##
  server.delete()
  
if action == "4":
  for img in imgs:
    print img.name, "  -- ID:", img.id
    
if action == "5":
  for flv in flvs:
    print "Name:", flv.name
    print "  ID:", flv.id
    print "  RAM:", flv.ram
    print "  Disk:", flv.disk
    print "  VCPUs:", flv.vcpus

  ##Gets keypair to use with server##
  public_key = open(os.path.expanduser("~/.ssh/id_rsa.pub")).read()
  keypair = cs.keypairs.create(KEY_PAIR_NAME, public_key)

  ##Builds Server##
  server = cs.servers.create(SERVER_NAME, image.id, flavor.id, key_name=keypair.name)
  pyrax.utils.wait_for_build(server, verbose=True)
  
##obtains images list
##images = pyrax.images.list()
    
##Obtains Flavour list
##flavor_list = cs.list_flavors()


##displayS ASSOCIATED ADDRESSES WITH CREATED SERVER##
#server.addresses


