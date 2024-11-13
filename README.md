# Instagram-API

BoxAPI is a robust API solution for accessing a wide array of Instagram data, such as user profiles, media, stories, locations, hashtags, and more. It’s designed for developers seeking an efficient, reliable way to integrate comprehensive Instagram information into their applications.

## Features

### User
- **Retrieve User by ID** 📱: Get user information using their Instagram ID.
- **Retrieve Web Profile Information** 💻: Access detailed profile information available on Instagram web.
- **Retrieve Media**: Fetch all media associated with a user.
- **Retrieve Media by Username**: Get media by providing the Instagram username.
- **Retrieve Clips**: Access Instagram Reels and other clips.
- **Retrieve Guides**: Fetch guides created by the user.
- **Retrieve Tags**: Access tags related to the user.
- **Retrieve Followers**: Get a list of followers of the user.
- **Retrieve Following List**: Access the list of users that the specified user follows.
- **Retrieve Stories**: Get current stories posted by the user.
- **Retrieve Highlights**: Access story highlights saved by the user.
- **Retrieve Live Streams**: Fetch live video sessions.
- **Retrieve Similar Accounts**: Get a list of similar or suggested accounts.
- **Search Users**: Search for users by username or other parameters.

### Media
- **Retrieve Media Information**: Get detailed media information.
- **Retrieve Media by Shortcode**: Access media information using the unique shortcode.
- **Retrieve Likes**: Get a list of users who liked a media post.
- **Retrieve Comments**: Access all comments on a media post.
- **Retrieve Shortcode by ID**: Convert a media ID to its shortcode.
- **Retrieve ID by Shortcode**: Convert a shortcode to its media ID.

### Guide
- **Retrieve Guide Information**: Access details of Instagram guides.

### Location
- **Retrieve Location Information**: Get details of a specific location.
- **Retrieve Media by Location**: Access media posts tagged with a specific location.
- **Search Locations**: Search for locations based on names or coordinates.

### Hashtag
- **Retrieve Hashtag Information**: Access information related to a specific hashtag.
- **Retrieve Media by Hashtag**: Fetch media associated with a hashtag.
- **Search Hashtags**: Search for hashtags by name or keyword.

### Highlight
- **Retrieve Highlight Stories**: Access stories saved in a user’s highlights.

### Comment
- **Retrieve Comment Likes**: Get users who liked a specific comment.
- **Retrieve Comment Replies**: Fetch replies to a particular comment.

### Audio
- **Retrieve Media by Audio**: Access media associated with specific audio tracks.
- **Search Audio**: Search for audio tracks on Instagram.

## Getting Started

To get started, Read the Instagram BoxAPI documents at [BoxAPI](https://boxapi.ir/docs/instagram/instagram-api/) to create an account and get your API credentials.

### Authentication

BoxAPI uses Basic Authentication. You must include your BoxAPI username and password in the request headers.

```bash
POST https://boxapi.ir/api/instagram/ENDPOINT

