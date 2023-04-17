# Django Heroku `DATABASE_URL` Parser

Python function to parse Heroku-provided `DATABASE_URL`.

* URL to be parsed:
  * `postgres://DATABASE_USER:DATABASE_PASSWORD@DATABASE_HOST:DATABASE_PORT/DATABASE_NAME`
  * `postgres://aaaaaaaaaaaaaa:a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1@aa1-11-111-11-111.aaaaaaa-1.amazonaws.com:1111/a1a1a1a1a1a1a1`
    * It is not ensured that the sub-string values will be alpha or numeric.

* Delimiters:
  * `postgres://`
  * `:`
  * `@`
  * `:`
  * `/`

## GitHub Copilot Suggestions

```python
def config(url):
    url = url.split('://')[1]
    url = url.split(':')
    url = url[1].split('@')
    url = url[0].split(':')
    return {
        "database": url[0],
        "user": url[1],
        "password": url[2],
        "host": url[3],
        "port": url[4]
    }

```

```python
# Parse a Heroku database URL into a dictionary
# https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
import os
import urlparse

def config():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    return {
        "database": url.path[1:],
        "user": url.username,
        "password": url.password,
        "host": url.hostname,
        "port": url.port
    }
```

## My Evolution

```python
def get_database_config_variables(url):
    """
    Parse the Heroku `DATABASE_URL` into a dictionary.
    """
    # Remove the `postgres://` from the beginning of the string
    url = url.split('://')[1]
    # Split the string into a list of strings at the `:` delimeter
    url = url.split(':')
    # Split the second string url[1] into a list of strings at the `@` delimeter
    url[1] = url[1].split('@')
    # Split the third string url[2] into a list of strings at the `/` delimeter
    url[2] = url[2].split('/')

    return url
```

```python
def get_database_config_variables(url):
    """
    Parse the Heroku `DATABASE_URL` into a dictionary.
    """
    # Remove the `postgres://` from the beginning of the string
    url = url.split('://')[1]
    # Split the remaining string into a list on the `@` character, which separates the database credentials from the host info
    credentials_and_host_info = url.split('@')
    # Get the database credentials (`DATABASE_USER` and `DATABASE_PASSWORD`) from the first item in the list
    credentials = credentials_and_host_info[0].split(':')
    # Get the database `host_info` from the second item in the list, which is the `DATABASE_HOST`, `DATABASE_PORT`, and `DATABASE_NAME`
    host_info = credentials_and_host_info[1].split(':')
    # Get the database host and port from the first item in the list
    host = host_info[0]
    # Get the database port and name from the second item in the list
    port_and_name = host_info[1].split('/')
    # Get the database port and name from the first item in the list
    port = port_and_name[0]
    # Get the database name from the second item in the list
    name = port_and_name[1]
    # Return a dictionary with the database credentials and host info
    return {
        'DATABASE_USER': credentials[0],
        'DATABASE_PASSWORD': credentials[1],
        'DATABASE_HOST': host,
        'DATABASE_PORT': port,
        'DATABASE_NAME': name
    }
```
