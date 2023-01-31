const Twitter = require('twitter');

const client = new Twitter({
  consumer_key: 'Your consumer key here',
  consumer_secret: 'Your consumer secret here',
  access_token_key: 'Your access token key here',
  access_token_secret: 'Your access token secret here'
});

// Function to like tweets containing a specific keyword
const likeTweets = (keyword) => {
  const params = { q: keyword, count: 10, result_type: 'recent' };
  client.get('search/tweets', params, (error, tweets, response) => {
    if (!error) {
      const statuses = tweets.statuses;
      for (let i = 0; i < statuses.length; i++) {
        client.post(`favorites/create`, { id: statuses[i].id_str }, (error, tweet, response) => {
          if (error) {
            console.log(error);
          } else {
            console.log(`Liked tweet: ${statuses[i].text}`);
          }
        });
      }
    } else {
      console.log(error);
    }
  });
};

// Function to retweet tweets containing a specific keyword
const retweetTweets = (keyword) => {
  const params = { q: keyword, count: 10, result_type: 'recent' };
  client.get('search/tweets', params, (error, tweets, response) => {
    if (!error) {
      const statuses = tweets.statuses;
      for (let i = 0; i < statuses.length; i++) {
        client.post(`statuses/retweet/${statuses[i].id_str}`, (error, tweet, response) => {
          if (error) {
            console.log(error);
          } else {
            console.log(`Retweeted tweet: ${statuses[i].text}`);
          }
        });
      }
    } else {
      console.log(error);
    }
  });
};

// Function to comment on tweets containing a specific keyword
const commentOnTweets = (keyword, comment) => {
  const params = { q: keyword, count: 10, result_type: 'recent' };
  client.get('search/tweets', params, (error, tweets, response) => {
    if (!error) {
      const statuses = tweets.statuses;
      for (let i = 0; i < statuses.length; i++) {
        client.post(`statuses/update`, { in_reply_to_status_id: statuses[i].id_str, status: `@${statuses[i].user.screen_name} ${comment}` }, (error, tweet, response) => {
          if (error) {
            console.log(error);
          } else {
            console.log(`Commented on tweet: ${statuses[i].text}`);
          }
        });
      }
    } else {
      console.log(error);
    }
  });
};

