'''
Created on 02.03.2012

@author: dreambit

@organization: GridDynamics
'''
def getNews(githubLogin, githubPassword, organizationName, useToken = False, authToken = ""):
    """
    @type githubLogin: String
    @type githubPassword: String
    @type organizationName: String
    @type useToken: Boolean
    @type authToken: String
    @param githubLogin: Login on GitHub
    @param organizationName: Organization name on GitHub
    @param useToken:  ??????????
    @param authToken: ??????????
    @return: Response from Server, which contains a list of organization's events in JSON format
    """
    pass
def addNewsToDB(response):
    """
    Add last news from JSON content into DataBase
    @type response: Response
    @param response: Response from Server, which contains a list of organization's events in JSON format
    @return: None
    """
    pass
def getLastNewsId():
    """
    This method gets the ID of the latest news from DataBase
    @return: ID of the latest news from DataBase
    """
    pass