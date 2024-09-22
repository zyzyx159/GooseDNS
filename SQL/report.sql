SELECT 
    (SELECT count(*) 
    FROM domain 
    WHERE ID > 0)
    AS Total_Domains,
    (SELECT count(*)
    FROM domain
    WHERE ID > 0 
    AND active = 'T')
    AS Active_Domains,
    (SELECT COUNT(*)
    FROM Subdomains
    WHERE ID > 0)
    as Total_Subdomains,
    (SELECT count(*)
    FROM Subdomains
    WHERE ID > 0
    AND active = 'T')
    AS Active_Subdomains;