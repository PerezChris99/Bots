const Twit = require('twit');

const T = new Twit({
  consumer_key: 'YOUR_CONSUMER_KEY',
  consumer_secret: 'YOUR_CONSUMER_SECRET',
  access_token: 'YOUR_ACCESS_TOKEN',
  access_token_secret: 'YOUR_ACCESS_TOKEN_SECRET',
  timeout_ms: 60 * 1000,  // optional HTTP request timeout to apply to all requests.
});

// Like a tweet
T.post('favorites/create', { id: 'TWEET_ID' }, (err, data, response) => {
  console.log(data);
});

// Follow a user
T.post('friendships/create', { screen_name: 'SCREEN_NAME' }, (err, data, response) => {
  console.log(data);
});

// Unfollow a user
T.post('friendships/destroy', { screen_name: 'SCREEN_NAME' }, (err, data, response) => {
  console.log(data);
});

// Comment on a tweet
T.post('statuses/update', { status: 'YOUR_COMMENT', in_reply_to_status_id: 'TWEET_ID' }, (err, data, response) => {
  console.log(data);
});

// Unfollow non-followers
T.get('followers/ids', { screen_name: 'SCREEN_NAME' }, (err, data, response) => {
  const followers = data.ids;
  T.get('friends/ids', { screen_name: 'SCREEN_NAME' }, (err, data, response) => {
    const friends = data.ids;
    const nonFollowers = friends.filter(friend => !followers.includes(friend));
    nonFollowers.forEach(nonFollower => {
      T.post('friendships/destroy', { user_id: nonFollower }, (err, data, response) => {
        console.log(data);
      });
    });
  });
});

// Follow accounts with more than 1000 followers
T.get('users/search', { q: 'FOLLOW_KEYWORD', count: 100 }, (err, data, response) => {
  data.forEach(user => {
    if (user.followers_count >= 1000) {
      T.post('friendships/create', { user_id: user.id }, (err, data, response) => {
        console.log(data);
      });
    }
  });
});

// Unfollow accounts with less than 1000 followers
T.get('friends/list', { count: 200 }, (err, data, response) => {
  data.users.forEach(user => {
    if (user.followers_count < 1000) {
      T.post('friendships/destroy', { user_id: user.id }, (err, data, response) => {
        console.log(data);
      });
    }
  });
});
