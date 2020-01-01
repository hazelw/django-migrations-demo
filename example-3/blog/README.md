# Example 3 - double deletion (aka guide to --fake-ery part 1)

After further examining comment sentiment we've decided that it was a terrible idea to allow comments on our blog at all (never read the comments) and Bob, a fellow developer, has decided to remove the comment table entirely.

- Bob has deleted the model, but hasn't yet run the migration to remove the table.
- You've rebased your branch on master and have run `./manage.py makemigrations && ./manage.py migrate` to remove the table on your side (see `0002_delete_comment.py`)...
- Bob merges his own migration (`0003_delete_comment.py`) alongside another migration to make a simple update to the post table (`0002_post_subtitle.py` - as we've decided that we're a newspaper now).

- The easiest way to simulate this situation is:
    `rm ./posts/migrations/0002_post_subtitle.py posts/migrations/0003_delete_comment.py`
    `./manage.py migrate`
    `git checkout -- posts/migrations`

- When you now try and run `./manage.py migrate` you're confronted with a nasty warning.
- If you follow the instructions and merge the two branches using `./manage.py makemigrations --merge`, you will end up in an even worse place. You'll notice that both your migration and Bob's migration delete the same table. In general you should be careful merging migrations that touch the same table (and even more careful if they touch the same field).

- As Bob's migrations are now in the master branch and have gone out to production - they're the source of truth.
- You decide to delete your own migration (`0002_delete_comment.py`) and accept Bob's way... but as your local database has already been migrated, you're still in a bit of a mess. (Try running `./manage.py migrate` once `0002_delete_comment.py` has been removed. You should see `django.db.utils.OperationalError: no such table: posts_comment`.)

- This is where --fake comes in.
- You can list the migrations that have run by running `./manage.py showmigrations`. You'll see that `0003_delete_comment` hasn't been able to run.
- You can now *fake the migration*. Faking the migration tells Django that the migration has run, and to mark it as done. Faking migrations is a powerful tool, but needs to be used sensibly. If you are going to fake a migration, be specific about which migration (or which app) needs to be faked, and make sure that there is nothing in the faked migration that hasn't already taken place on your database.

- `./manage.py migrate posts 0003_delete_comment --fake`


This brings you back to a normal, working local database. Phew.

If you are having similar problems with pytest, you can tell pytest to throw away the whole test database using `pytest --reuse-db=False`.
