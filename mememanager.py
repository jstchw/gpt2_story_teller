import praw


class MemeManager:

    def __init__(self, client_id, client_secret, user_agent, subreddits_list, limit, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.subreddits_list = subreddits_list
        self.limit = limit
        self.reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret,
                                  user_agent=self.user_agent, username=username, password=password)
        print('>>> Reddit User: ', self.reddit.user.me())