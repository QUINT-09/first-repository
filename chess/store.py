import configparser

def set_value(what_section,what_item,new_value):
    config = configparser.ConfigParser()  
    config.read('src/config.txt')
    config.set(str(what_section),str(what_item),str(new_value))
    with open('src/config.txt', 'w') as configfile:
        config.write(configfile)
    



