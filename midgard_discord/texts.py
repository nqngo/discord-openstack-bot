# Large texts in the application


# Fragments
INFO_MORE = """

For more information, visit https://docs.midgardlab.io
"""


# Success texts
WELCOME = (
    """
Welcome to Midgard. Midgard is a private OpenStack cloud for VAIT testing, training, and development purpose.
At the moment, Midgard offers the following capacities:
    1. Virtual Machines.
    2. Automatic SSL certificate termination.
"""
    + INFO_MORE
)

PORT_FORWARDED = (
    """
<@{discord_user_id}> `{protocol}://{server_ip}:{port}` successfully deployed.`. Access it at:

https://{hostname}.midgardlab.io
"""
    + INFO_MORE
)

SERVER_CREATED = (
    """
<@{discord_user_id}> Your server has been successfully created. To access your server, add the following to your `~/.ssh/config` file:
```
Host {server_name}
    HostName {server_ip}
    ProxyCommand /usr/local/bin/cloudflared access ssh --hostname {hostname}
```
Then you can access your server by running `ssh {server_name}`.
"""
    + INFO_MORE
)


# Error texts
ERROR_NOT_REGISTERED = (
    """
<@{discord_user_id}> You are not yet registered. Please register by running `\migard register`.
"""
    + INFO_MORE
)

ERROR_SERVER_NOT_FOUND = (
    """
<@{discord_user_id}> You do not have any server. Please create a server by running `\midgard server launch`.
"""
    + INFO_MORE
)