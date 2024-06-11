BEGIN TRANSACTION;

CREATE TABLE domain(
    FQDN text primary key,
    email text,
    SN int(10),
    refresh text,
    retry text,
    expire text, 
    minTTL text,
    WAN_IP text,
    active varchar(1)
);

CREATE TABLE Subdomains(
    id int primary key,
    name text,
    active varchar(1),
    FOREIGN KEY(FQDN) REFERENCES domain(FQDN)
);

CREATE TABLE MISC(
    id int primary key,
    name text,
    FOREIGN KEY (FQDN) REFERENCES domain(FQDN),
    recordType text,
    value text    
);


COMMIT;