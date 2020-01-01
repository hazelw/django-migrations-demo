# Example 4 - field double deletion (aka guide to fake-ery part 2)

Someone in the business found out that we were no longer tracking comments and demanded an immediate rollback of the changes Bob made.

"Fine," says Bob, "I will get rid of the sentiment metric instead".

And so Bob removes the sentiment field from the comment and deploys to production again, allowing the change to bed in before he removes the field from the database.

We pull again and, once again, run `./manage.py makemigrations && ./manage.py migrate` to bring our database up to date. We drop the sentiment field from the Comment table.
