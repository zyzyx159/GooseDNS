select count(FQDN)
from Domain
where id > 0;

select count(FQDN)
from Domain
where id > 0
and active = 't';

select count(name)
from Subdomains
where id > 0;

select count(name)
from Subdomains
where id > 0
and active = 't';