# Insert query

insert_new_url = '''
insert into {0}(full_url_hash, short_url_hash, url, ip_address, user_agent)
values('{1}', '{2}', '{3}', '{4}', '{5}')
'''

get_url = '''
select url
from {0}
where short_url_hash = '{1}'
limit 1
'''

update_visits_by_short_hash = '''
update {0}
set visits = visits + 1
where short_url_hash = '{1}'
'''