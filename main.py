import instaloader

SESSION = instaloader.Instaloader()

USER = "fake_friends_bt"    #Email: fakefriendsburner@yahoo.com    Email Password: Fakefriends
PASS = "Fakefriends"        #instagram birthday just in case Jan 1st 2000
SESSION.login(USER, PASS)

profile = instaloader.Profile.from_username(SESSION.context, "<username of target>")

follower_list = []
count = 0
for follower in profile.get_followers():
    count += 1
    print("[" + str(count) + "] " + follower.username)
    follower_list.append(follower.username)

print("\nFinished Followers! Checking Following...\n")
count = 0

for followee in profile.get_followees():
    count += 1
    followee_username = followee.username
    if followee_username in follower_list:
        print("[" + str(count) + "] [YES] " + followee_username)
    else:
        print("[" + str(count) + "] [NO] " + followee_username)
        file = open("FakeFriendsList", "a+")
        file.write(followee.username + "\n")
        print
        file.close()