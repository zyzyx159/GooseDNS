SELECT ID, 
    FQDN, 
    Email, 
    SN, 
    Refresh, 
    Retry, 
    Expire, 
    Minimum_TTL, 
    Wan_IP, 
    Active 
FROM Domain
WHERE ID = 