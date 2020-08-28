import configparser

config = configparser.RawConfigParser() # object creation for predefined method
config.read(".\\Configurations\\config.ini") #method used to reach config.ini

#Obtaining data from config.ini

class ReadConfig:
    #create a method for each variable i.e 3

    # static method allows you to directly access method without creating an object for class
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password