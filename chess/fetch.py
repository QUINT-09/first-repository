import configparser

def get_value(what_section,what_item):
    config = configparser.ConfigParser()  
    config.read('src/config.txt')
    value = config.get(str(what_section),str(what_item))
    return value



""" config.set(what_section,what_item,"4")
with open('src/config.txt', 'w') as configfile:
    config.write(configfile) """