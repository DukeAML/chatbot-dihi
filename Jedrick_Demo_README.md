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

```pipenv run flask run --port 9999 ```

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

Critical Commands:
'having chest pain', 
'drooping of my face',                               
'unable to walk',
'short of breath at rest',
'tight chest pain',
'chest pain and nausea', 
'having chest pains that have gotten increasingly worse',
'chest pains that have gotten worse',
'chest pain that has gotten worse', 
'chest pain has gotten worse',
'passing out nonstop',
'passing out again'