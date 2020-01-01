# Example 2 - nulling nulls

This time, we're adding a new field to Comment - 'sentiment'. We've decided that it is very, very important to measure the sentiment of comments made on our blog and that it can't possibly be null. Have a look at the output of `./manage.py makemigrations`.

We're told that we either need to set a default, or allow it to be null. Either is a valid option - one may be better than another depending on what we're using the field for. In the case of sentiment we can't really assume that all historical comments are neutral in tone, so it may be better to make the new field nullable. We can do this by setting `null=True` on the sentiment field.
