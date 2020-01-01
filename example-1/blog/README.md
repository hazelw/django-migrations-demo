# Example 1

When you start a Django project you'll usually add some new models. This example is the simplest,
happiest path.

Here we've got two new models in the posts app and no migrations yet. Run
`./manage.py makemigrations posts` to generate the migration scripts and `./manage.py migrate` to add the models to the
database (and see the changes in `db.sqlite3`).

Things to note:
- As the migration is the initial migration for the posts app, Django has automatically marked it
as initial = True. If there are no migrations where initial is True, Django will treat the first
migration in the /migrations folder as the initial one. Marking a migration as the initial migration
gives us some special skipping options (optionally see https://docs.djangoproject.com/en/3.0/ref/django-admin/#cmdoption-migrate-fake-initial).
- We've got two calls to CreateModel. Internally these are calls to CREATE TABLE.
- Django has given us an ID on each model to use as a primary key, even though we haven't defined it on the model.
- As we've defined foreign keys (post.author, comment.author and post.author) Django generates CREATE INDEX statements for them.
- You can see the SQL that a particular migration will run by doing `./manage.py sqlmigration app_label migration_name` (eg. `./manage.py sqlmigrate posts 0001_initial`)
- Even though the database doesn't care that `comment_type` will be either 'question' or 'comment', including the options was a deliberate design decision from the Django team (more info: https://code.djangoproject.com/ticket/22837). This means that if you change the options a field could have, a new migration script should be generated.
