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
FROM domain
WHERE ID = 