# DEMO WALKTHROUGH

## Step 1
Open Visual Studio Code to the main folder that has this file in it.

## Step 2
Click CTRL+` to open a terminal in VS-Code
Open two separate terminals by clicking the 'window cut in half' icon in the top right corner of the terminal that just popped up.

## Step 3 - Start Backend
On the terminal on the left, type the following commands, with an enter between them and waiting for the previous to finish before running the next.

```cd server```

```pipenv install```

```pipenv shell```

```pipenv run flask run --port 5000 ```

Should be good there.
## Step 4 - Start Frontend
On the terminal on the right, type the following commands, with an enter between them and waiting for the previous to finish before running the next.

```cd chatbot-moderator```

```npm install```

```npm run serve```

Should be good there.
## Step 5 - Use

Head to http://10.197.109.81:8080/, unless there is a different address listed after the last command in the right (direction) terminal.

Now all should be good.