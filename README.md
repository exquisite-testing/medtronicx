# Pylenium Page Object Model

This project provides setup and running of the test using Pylenium with the Page Object Model to automate tests on a Reddit website.

## Prerequisites

- Python 3.x
- Pylenium
- Behave (for running Cucumber scenarios)

## Instructions

This assignment will test your skills with test automation and your selected language

Using a test automation framework, create a script (as complex or simple as you wish) to:

- Open the website https://www.reddit.com/
- Search for a subreddit called "gaming"
- Open the sub-reddit
- Print out the top most post's title
- Perform a login
- Downvote the second post if it's upvoted already, upvote otherwise (in case the second post is an advertisement or announcement, use the third)

## Install dependencies

pip install -r requirements.txt

## Running the Tests

python test_script.py

## Running Cucumber Scenarios

run `behave` from the root
