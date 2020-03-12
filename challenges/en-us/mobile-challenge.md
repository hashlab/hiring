# Hash Mobile Challenge

First of all, we recommend you to read our [key values](https://www.keyvalues.com/hash) to understand what we prioritize in development process. We hope you do your best as we will evaluate that way. ;)

## General Rules

- The project should be developed in a **native language** of the platform that you are applying for

- The project should be available in a Github repository

- You cannot submit any changes to repository after delivery the code

- Email us in dev@hash.com.br to send the link to your code or for any questions

## Overview

The goal of this challenge is to implement a mobile app that consumes the [Reddit](reddit.com) API and list all posts and its comments of a specific topic e.g. [Programming](https://www.reddit.com/r/programming) topic.

Here is the link for Reddit API documentation: https://www.reddit.com/dev/api/

To fetch data as `json` from Reddit API you just need to put `.json` in the end of URL.

Example:

- The web page: https://www.reddit.com/r/programming
- The `json` data: https://www.reddit.com/r/programming.json

## Task

You'll implement two screens in your app. The first one represents a screen that will list all posts of a topic, and the second one represents the details of a selected post.

### 1. Listing all posts

You must implement a screen that lists all posts of a topic of your choice. In the listing you must show the name of user that created the post, the title, the date and time of creation (you can show it as a time elapsed format) and the media whenever applicable.

You can also show any other information of a post you want, such as comments count.

For instance, to fetch `json` data for all posts of a topic you just need to make a HTTP call to the URL of a topic:

https://www.reddit.com/r/programming.json

### 2. Show post details

You must implement a second screen that shows the details of the selected post in the posts listing. In this screen you need to show the same data required in the posts listing, in addition of all comments with its replies.

For instance, to fetch `json` data of a post you need to make a HTTP call to the following example URL:

https://www.reddit.com/r/programming/comments/ew2a7y/lets_destroy_c.json

## Requirements

- Your code should be **100% crash free**

- You **must** paginate data loading whenever applicable

- You **must** include tests

- You **must** include guidelines to setup, compile and run your code in README.md file

- You **must** follow the UI best practices of the platform that you are applying for

## Tips

- It's a good practice to alert the user whenever the application is processing or fetching data

- Take time to digest everything you need before you start the development

- If you have any questions, please contact us. We'll be more than happy to help you!
