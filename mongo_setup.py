import mongoengine

alias_core = 'core'


def init():
    db = 'tfm'
    # Other connection options here (server, port, username, etc.)
    mongoengine.register_connection(alias=alias_core, name=db)