# Phase 3 CLI Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

***

## Introduction

You now have a basic idea of what constitutes a CLI, but you (understandably!)
likely don't have the best idea of where to start. Fork and clone this lesson
for a template for your CLI. Take a look at the directory structure before we
begin:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py
```

> **Note: You may already know some or all of the material covered in this
> lesson. We hope that having it all in one place will help you in designing
> and developing your project, regardless of where you're starting off.**

***

## Where Do I Start?

This project will likely be one of the biggest projects you've undertaken so
far. Your first task should be creating a Git repository to keep track of your
work and roll back any undesired changes.

### Removing Existing Git Configuration

If you're using this template, start off by removing the existing metadata for
Github and Canvas. Run the following command to carry this out:

```console
$ rm -rf .git .github .canvas
```

The `rm` command removes files from your computer's memory. The `-r` flag tells
the console to remove _recursively_, which allows the command to remove
directories and the files within them. `-f` removes them permanently.

`.git` contains this directory's configuration to track changes and push to
Github (you want to track and push _your own_ changes instead), and `.github`
and `.canvas` contain the metadata to create a Canvas page from your Git repo.
You don't have the permissions to edit our Canvas course, so it's not worth
keeping them around.

### Creating Your Own Git Repo

First things first- rename this directory! Once you have an idea for a name,
move one level up with `cd ..` and run `mv python-p3-cli-project-template
<new-directory-name>` to change its name.

> **Note: `mv` actually stands for "move", but your computer interprets this
> rename as a move from a directory with the old name to a directory with
> a new name.**

`cd` back into your new directory and run `git init` to create a local git
repository. Add all of your local files to version control with `git add --all`,
then commit them with `git commit -m'initial commit'`. (You can change the
message here- this one is just a common choice.)

Navigate to [GitHub](https://github.com). In the upper-right corner of the page,
click on the "+" dropdown menu, then select "New repository". Enter the name of
your local repo, choose whether you would like it to be public or private, make
sure "Initialize this repository with a README" is unchecked (you already have
one), then click "Create repository".

Head back to the command line and enter `git remote add <project name> <github
url>`. This will map the remote repository to your local repository. Finally,
push your first commit with `git push -u origin main`.

Your project is now version-controlled locally and online. This will allow you
to create different versions of your project and pick up your work on a
different machine if the need arises.

***

## Generating Your Pipenv

You might have noticed in the file structure- there's already a Pipfile! That
being said, we haven't put much in there- just Python version 3.8 and ipdb.

Install any dependencies you know you'll need for your project, like SQLAlchemy
and Alembic, before you begin. You can do this straight from the command line:

```console
$ pipenv install sqlalchemy alembic
```

From here, you should run your second commit:

```console
$ git add Pipfile Pipfile.lock
$ git commit -m'add sqlalchemy and alembic to pipenv'
$ git push
```

Now that your environment is set up, run `pipenv shell` to enter it.

***

## Generating Your Database

Once you're in your environment, you can start development wherever you'd like.
We think it's easiest to start with setting up your database.

`cd` into the `lib/db` directory, then run `alembic init migrations` to set up
Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
create, then replace line 21 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

We haven't created our `Base` or any models just yet, but we know where they're
going to be. Navigate to `models.py` and start creating those models. Remember
to regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create
checkpoints in case you ever need to roll those modifications back.

If you want to seed your database, now would be a great time to write out your
`seed.py` script and run it to generate some test data. You may want to use
Pipenv to install Faker to save you some time.

***

## Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

Here's what all of these things have in common (if done well): a number of
`import` statements (usually _a lot_ of import statements), an `if __name__ ==
"__main__"` block, and a number of function calls inside of that block. These
functions should be kept in other modules (ideally not _just_ `helpers.py`)

There will likely be some `print()` statements in your CLI script to let the
user know what's going on, but most of these can be placed in functions in
other modules that are grouped with others that carry out similar tasks. You'll
see some variable definitions, object initializations, and control flow
operators (especially `if/else` blocks and `while` loops) as well. When your
project is done, your `cli.py` file might look like this:

```py
from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5, function_6,
    function_7, function_8,
    function_9, function_10
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    function_9(z)
    function_10(x, y, z)
    print('Thanks for using my CLI')

```

***

## Updating Your README.md

`README.md` is a Markdown file that describes your project. These files can be
used in many different ways- you may have noticed that we use them to generate
entire Canvas lessons- but they're most commonly used as homepages for online
Git repositories. **When you develop something that you want other people to
use, you need to have a README.**

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this lesson's resources for a basic guide to Markdown.

### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

***
Car Compare CLI
Overview
The Car Compare CLI is a command-line interface application that allows users to add car details, compare different cars, and manage car records. The application uses web scraping to gather car information, stores it in a database using SQLAlchemy, and provides various functionalities through a user-friendly CLI.

Features
Add Cars: Enter car details and save them to the database.
Compare Cars: View details of all saved cars and compare their attributes.
Manage Records: Delete existing car records and manage the list of saved cars.
Interactive CLI: Navigate through the CLI to perform different actions and view results.
Requirements
Python 3.8
SQLAlchemy
Alembic
Requests
BeautifulSoup4
IPDB (for interactive debugging, optional)
Installation
Clone the Repository

bash
Copy code
git clone <your-repository-url>
cd car_compare_cli
Set Up Virtual Environment

Create a virtual environment to isolate project dependencies:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

On Windows:

bash
Copy code
.venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source .venv/bin/activate
Install Dependencies

Install the required packages using pipenv:

bash
Copy code
pipenv install
This will install all necessary dependencies, including:

sqlalchemy for ORM functionality
alembic for database migrations
requests for making HTTP requests
beautifulsoup4 for web scraping
ipdb for interactive debugging (optional)
Usage
Start the CLI Application

Run the CLI application:

bash
Copy code
python cli.py
Follow Prompts

Enter the name of the car and manufacturer when prompted.
Choose options to add more cars, compare cars, or delete existing records.
Use the CLI menu to navigate through the application.
Example
plaintext
Copy code
Welcome to Car Compare CLI
Enter the name of the car or type 'exit' to quit: x1
Enter the name of the manufacturer: bmw
Details for x1 have been successfully saved.

--- List of Cars Added ---
1: x1, 49.50 - 52.50 Lakh, 134.1 - 147.51 bhp, 230 Nm - 360 Nm, 1499 cc - 1995 cc
Manufacturer: bmw
Features: powered front seats, height adjustable driver seat, cruise control, automatic climate control, parking sensors

Options:
1. Add More Cars
2. Compare Cars
3. Delete Existing Car
4. Exit

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
