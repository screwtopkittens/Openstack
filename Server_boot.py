####DANs Super script for booting servers Version 1
####Version 1.0.0.a
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
  image = cs.images.get(IMAGE_VAR)
  flavor = cs.flavors.get(FLAVOR_VAR)
  ##Gets keypair to use with server##
  public_key = open(os.path.expanduser("~/.ssh/id_rsa.pub")).read()
  keypair = cs.keypairs.create(SERVER_NAME, public_key)

  ##Builds Server##
  server = cs.servers.create(SERVER_NAME, image.id, flavor.id, key_name=keypair.name)
  pyrax.utils.wait_for_build(server, verbose=True)
  print "ID:", server.id
  print "Status:", server.status
  print "Admin password:", server.adminPass
  print "Networks:", server.networks
  MAIN_MENU()

def STANDARD_SERVER_BUILD():
   ##This sets the image and flavour Varibles
  SERVER_NAME = raw_input("Enter the server name: ")
  IMAGE_STA = "9a153957-6b23-4c82-bd98-2529b6f0ef6b"
  FLAVOR_STA = "general1-1"
  
  print " Please select the image you would like to build"
  print "1. Ubuntu 18.04 LTS (Bionic Beaver)"
  print "2. Ubuntu 16.04 LTS (Xenial Xerus)"
  print "3. Ubuntu 14.04 LTS (Trusty Tahr)"
  print "4. CentOS 7"
  print "5. CentOS 6"
  print "6. Debian 9 (Stretch)"
  action_srv = raw_input("Enter a selection: ")
 
  if action_srv == "1":
    IMAGE_STA = "9a153957-6b23-4c82-bd98-2529b6f0ef6b"
  if action_srv == "2":
    IMAGE_STA = "907770dd-ddf4-4281-afda-f9d25125c1bd"
  if action_srv == "3":
    IMAGE_STA = "0bb1924b-14fc-4638-a5a7-46024e4fcc1b"
  if action_srv == "4":
    IMAGE_STA = "8990ceb6-eb12-4c4f-b602-63b8459e02f9"
  if action_srv == "5":
    IMAGE_STA = "cce201c0-33f8-4a59-847e-352d2658fa1c"
  if action_srv == "6":
    IMAGE_STA = "2d970ae8-c358-4284-a43f-47cfd5968b70"
    
  print " Please select the flavor you would like to build"
  print "1. 1 GB General Purpose v1"
  print "2. 2 GB General Purpose v1"
  print "3. 4 GB General Purpose v1"
  print "4. 8 GB General Purpose v1"
  action_flv = raw_input("Enter a selection: ")
   
  if action_flv == "1":
    FLAVOR_STA = "general1-1"
  if action_flv == "2":
    FLAVOR_STA = "general1-2"
  if action_flv == "3":
    FLAVOR_STA = "general1-4"
  if action_flv == "4":
    FLAVOR_STA = "general1-8"
    
  image = cs.images.get(IMAGE_STA)
  flavor = cs.flavors.get(FLAVOR_STA)
  
  ##Gets keypair to use with server##
  public_key = open(os.path.expanduser("~/.ssh/id_rsa.pub")).read()
  keypair = cs.keypairs.create(SERVER_NAME, public_key)
  
  ##Builds Server##
  server = cs.servers.create(SERVER_NAME, image.id, flavor.id, key_name=keypair.name)
  pyrax.utils.wait_for_build(server, verbose=True)
  print "ID:", server.id
  print "Status:", server.status
  print "Admin password:", server.adminPass
  print "Networks:", server.networks
  MAIN_MENU()
  
def LIST_SERVERS():
  print cs.servers.list()
  MAIN_MENU()

def AVALIBLE_IMAGES():
  for img in imgs:
    print img.name, "  -- ID:", img.id
  MAIN_MENU()

def AVALIBLE_FLAVORS():
  for flv in flvs:
    print "Name:", flv.name
    print "  ID:", flv.id
    print "  RAM:", flv.ram
    print "  Disk:", flv.disk
    print "  VCPUs:", flv.vcpus
  MAIN_MENU()
  
def MAIN_MENU():
  ##selects task
  print " Welcome to Dans Amazing cloud server configuration tool please see the menu below and select an Action"
  print "1. Build Custom Server"
  print "2. Show built server details"
  print "3. Build standard Server"
  print "4. show avalible images"
  print "5. show avalible flavors"
  action = raw_input("Enter a selection: ")

  if action == "1":
    BUILD_CUSTOM_SERVER()
  
  if action == "2":
    LIST_SERVERS()
  
  if action == "3":
    STANDARD_SERVER_BUILD()
  
  if action == "4":
    AVALIBLE_IMAGES()
    
  if action == "5":
    AVALIBLE_FLAVORS()
    
    
MAIN_MENU()





