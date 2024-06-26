BEGIN TRANSACTION;

CREATE TABLE domain(
    FQDN text PRIMARY KEY,
    email text,
    SN int(10),
    refresh text,
    retry text,
    expire text, 
    minTTL text,
    active varchar(1)
);

insert into domain values(
    'example.com',
    'email@example.com',
    1970010101,
    '10800',
    '1800',
    '1209600',
    '10800',
    'T'
);

CREATE TABLE Subdomains(
    id int PRIMARY KEY,
    name text,
    active varchar(1),
    FQDN text,
    FOREIGN KEY(FQDN) REFERENCES domain(FQDN)
);

insert into Subdomains values(
    1,
    'Demonstration',
    'F',
    'example.com'
);

CREATE TABLE MISC(
    id int PRIMARY KEY,
    name text,
    FQDN text,
    recordType text,
    value text,
    FOREIGN KEY(FQDN) REFERENCES domain(FQDN)
);

insert into MISC values(
    1,
    'nameServer',
    'example.com',
    'NS',
    '127.0.0.1'
);

COMMIT;