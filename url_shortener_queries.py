# Insert query

insert_new_url = '''
insert into url_map(full_url_hash, short_url_hash, url, ip_address, user_agent)
values('{0}', '{1}', '{2}', '{3}', '{4}')
'''

get_url = '''
select url
from url_map
where short_url_hash = '{0}'
'''

update_visits_by_short_hash = '''
update url_map
set visits = visits + 1
where short_url_hash = '{0}'
'''