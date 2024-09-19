from DBInterface import *

class Domain:
    ID = ''
    FQDN = ''
    Email = ''
    SN = ''
    refresh = ''
    retry = ''
    expire = ''
    Minimum_TTL = ''
    Wan_IP = ''
    Active = ''

    def makeNew(self):
        self.ID = DBInterface().maxDomainID() + 1

    def selectExisting(self, domID):
        self.ID = domID
        currentDomainID = DBInterface().domainSelect(self.ID)

