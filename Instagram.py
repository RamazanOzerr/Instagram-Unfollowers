import instaloader as ig
from tqdm import tqdm
from time import sleep

class Instagram():
    def __init__(self):
        self.followers_file_name = "followers.txt"
        self.following_file_name = "following.txt"
        self.unfollowers_file_name = "unfollowers.txt"

        self.username = input("please enter your username: ")
        self.password = input("please enter your password: ")
        self.targetAcc_username = input("please enter the target username which you wanna get the unfollowers list of: ")

        # calling methods
        self.login()  # log in
        self.get_followers()    # gets followers and writes them into a txt file
        self.get_following()     # gets followees and writes them into a txt file
        self.get_unfollowers()   # gets unfollowers and writes them into a txt file

    def login(self):
        self.L = ig.Instaloader()
        self.L.login(self.username,self.password)
        # self.profile = ig.Profile.from_username(self.L.context,self.username)
        self.profile = ig.Profile.from_username(self.L.context, self.targetAcc_username)
        print("has been successfully logged in")

    def get_followers(self):
        print("getting followers...")
        for i in self.profile.get_followers():
            with open(self.followers_file_name,"a+", encoding="utf-8") as file:
                file.write(i.username + "\n")
        print("followers list has been created, check out the 'followers.txt' file")

    def get_following(self):
        print("getting followees...")
        for i in self.profile.get_followees():
            with open(self.following_file_name,"a+", encoding="utf-8") as file:
                file.write(i.username+"\n")

        print("following list has been created, check out the 'following.txt' file")

    def get_unfollowers(self):
        print("getting unfollowers.. almost done")
        file1 = open("followers.txt", "r")
        file2 = open("following.txt", "r")
        FollowersList = file1.readlines()
        FollowingList = file2.readlines()

        unfollowers_list = list()
        for i in FollowingList:
            if i not in FollowersList:
                unfollowers_list.append(i)
        with open(self.unfollowers_file_name, "w") as file:
            for username in unfollowers_list:
                file.write(username)

if __name__ == '__main__':
    instagram = Instagram()
    print("its done, you can check the 'unfollowers.txt' file")