BEGIN TRANSACTION;

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
