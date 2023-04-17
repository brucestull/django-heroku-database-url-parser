# DATABASE_URL:
# - `postgres://DATABASE_USER:DATABASE_PASSWORD@DATABASE_HOST:DATABASE_PORT/DATABASE_NAME`
# Parse a string into a dictionary with following delimeters:
# - `postgres://`
# - `:`
# - `@`
# - `:`
# - `/`


the_test_url = 'postgres://database_user:database_password@database_host:database_port/database_name'

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

print(get_database_config_variables(the_test_url))
