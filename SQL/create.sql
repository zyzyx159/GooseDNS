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
    'F'
);

CREATE TABLE Subdomains(
    id int PRIMARY KEY,
    name text,
    active varchar(1),
    FQDN text,
    FOREIGN KEY(FQDN) REFERENCES domain(FQDN)
);

insert into Subdomains values(
    0,
    'Demonstration',
    'F',
    'example.com'
);

CREATE TABLE Core(
    id int PRIMARY KEY,
    name text,
    FQDN text,
    recordType text,
    value text,
    FOREIGN KEY(FQDN) REFERENCES domain(FQDN)
);

insert into Core values(
    0,
    'nameServer',
    'example.com',
    'NS',
    '127.0.0.1'
);

COMMIT;