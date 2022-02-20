from modules import list_created_account
from instapy import InstaPy

accounts = list_created_account.list_created_account()
for a in accounts:
    insta_username = a['username']
    insta_password = a['password']

# if you want to run this script on a server,
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
session.set_do_comment(True, percentage=10)
accs = ['edrafid','biscuitrafid']
session.follow_by_list(accs, times=1, sleep_delay=600, interact=False)
# end the bot session
session.end()

