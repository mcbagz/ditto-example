# ditto-example
Example run of the AI agent Ditto: https://github.com/yoheinakajima/ditto

## Running Ditto
I spent a few hours trying to get Ditto to run with a locally hosted LLM via Ollama. If anyone has gotten this to work, please let me know! Finally, I decided to just use gpt-4o-mini from OpenAI, and it completed the task in under a minute with a cost of $0.007. There is a lesson to be learned here.

I gave Ditto a pretty simple task: 
>Build a website where users can create profiles with usernames and post messages to a global feed that anyone can read, and store all the data in a sqlite database

As you can see from the code, Ditto executed the task quite well! I only had to make a few adjustment:

## Adjustments
The code, as written by Ditto, threw a few errors. Specifically, the SQLite tables were not initialized, so I added the following lines to message.py and user.py, respectively:

```c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user_id INT, content TEXT, timestamp INT)")```

```c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")```

Further, messages were being sorted by "timestamp", which was not included when a new message was being stored, so I added `int(time.time())` and the relevant other code (like `import time`) to message.py

## Other Improvements
Ditto executed the task to the letter of what was written, but these are some additional improvements that would make sense for such an app:
- To create a profile, a user needs to go to {url}/profile; however, there is no link from index.html to get there, so it is unclear to a fresh user how to get started.
- There is no login or authorization to use a username. Perhaps this needed to be stated explicitly in the requirements of the task for Ditto to add it. Rather than re-running Ditto with a more sophisticated prompt, I feel like this app showcases what the agent does with a less detailed prompt.
- Ditto doesn't create a requirements.txt file. This is likely fine for running the app locally, as you probably have all the relevant modules installed, but this file is usually needed for deploying the app elsewhere

## Running This App
The only dependency here is Flask, so if you don't have it, run `pip install flask`.

Clone the app by running `git clone https://github.com/mcbagz/ditto-example`.

Make sure you are in the correct directory, then run `python main.py`.

You'll be able to access the app at http://0.0.0.0:5555. I would not recommend running it in any other environment, due to the problems stated above, but I have found some use running it locally and using it to transfer text across devices in my local network.
