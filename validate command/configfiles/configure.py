from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())
print(list(config['account']))

print(config['account']['status'])
config['account']['status'] = "desactive blz?"
print(config['account']['status'])

with open(file, 'w') as configfile:
    config.write(configfile)