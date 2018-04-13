# Insert query

insert_new_url = '''
insert into url_map(full_url_hash, short_url_hash, url)
values('{0}', '{1}', '{2}')
'''

get_url = '''
select url
from url_map
where short_url_hash = '{0}'
'''