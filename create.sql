BEGIN TRANSACTION;

Create table domain(
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

insert into domain values(
    'example.com',
    'john@example.com',
    2024061001,
    '10800',
    '1800',
    '1209600',
    '10800',
    '1.2.3.4',
    'T'
);

COMMIT;