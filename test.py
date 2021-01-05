import subprocess
import os.path
from contextlib import contextmanager
import shutil
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('sudo apt update && sudo apt install yarn')
os.system('sudo apt-get update')
os.system('sudo apt-get install yarn -y')


# Download git repo for vue-storefront-api
if not os.path.exists('vue-storefront-api'):
    subprocess.call('git clone https://github.com/vuestorefront/vue-storefront-api.git', shell = True)
elif os.path.exists('vue-storefront-api'):
  print ("Direcory Already exists")

# Make backup copy for .json file
chn_path = os.chdir('./vue-storefront-api')
shutil.copyfile('./config/default.json', './config/local.json')
#print(os.getcwd())

#Run command for docker -compose
cmd = 'docker-compose -f docker-compose.yml -f docker-compose.nodejs.yml up -d'
os.system(cmd)
os.system ('yarn install')
os.system ('yarn restore')
os.system ('yarn migrate')
os.system ('curl -XGET http://localhost:9200/_mapping?pretty=true')

#change Directory
chan_path = os.chdir('../')
#print(os.getcwd())

# Download git repo for vue-storefront
if not os.path.exists('vue-storefront'):
    subprocess.call('git clone https://github.com/vuestorefront/vue-storefront.git', shell = True)
    os.chdir ('./vue-storefront')
    subprocess.call('git submodule add -b master https://github.com/DivanteLtd/vsf-capybara.git src/themes/capybara', shell= True)
    subprocess.call('git submodule update --init --remote' , shell= True)
elif os.path.exists('vue-storefront'):
  print (bcolors.WARNING + "Direcory Already exists")
chan_path = os.chdir('../')
# Append existing file
os.chmod('./vue-storefront', 0o777)
chn_path = os.chdir('./vue-storefront')
shutil.copyfile('./config/default.json', './config/local.json')
#print(os.getcwd())
my_file = open("docker-compose.yml")
string_list = my_file.readlines()
my_file.close()
print(string_list)
string_list [25] = "      - './yarn.lock:/var/www/yarn.lock'\n"
my_file = open("docker-compose.yml", "w")
new_file_contents = "".join(string_list)
my_file.write(new_file_contents)
my_file.close()
readable_file = open("docker-compose.yml")
read_file = readable_file.read()
print(read_file)
# os.system ('sudo yarn install')
# os.system('sudo npm i -g @vue-storefront/cli')
os.chdir ('./src/themes/capybara/scripts')
#print(os.getcwd())
os.system('sudo yarn install')
os.system('node generate-local-config.js')
os.chdir('../')
#print(os.getcwd())
newPath = shutil.copy('local.json', '../../../config')
os.chdir('../../../')
print(os.getcwd())
my_file = open("tsconfig.json")
string_list = my_file.readlines()
my_file.close()
print(string_list) #"theme\/\*"\: "theme/*":
string_list [22] = "\"theme/*\":[\"src/themes/capybara/*\"],\n"
my_file = open("tsconfig.json", "w")
new_file_contents = "".join(string_list)
my_file.write(new_file_contents)
my_file.close()
readable_file = open("tsconfig.json")
read_file = readable_file.read()
print(read_file)
os.system('sudo npm install --g lerna')
os.system('lerna bootstrap && yarn build')
#print (bcolors.WARNING + 'select the Capybara theam and  Select default' )

#os.system('vsf init:theme')

# Run Finale compose command
cmd = 'docker-compose up -d'
os.system(cmd)

print("Ready to go Wait for 2 min")
time.sleep(120)    # Pause 5.5 seconds
print("Cook Book is ready")


print (bcolors.OKBLUE + "Open Url localhost:3000")
