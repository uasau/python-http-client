import os


class Config(object):
    """Allow variables assigned in .env available using
       os.environ.get('VAR_NAME')
       
       :param base_path: The path to your .env config file
       :type base_path: string
       """
    def __init__(self, base_path=None):
        if base_path == "test":
            base_path = os.path.join(os.path.dirname(__file__), os.pardir)
        elif base_path:
            base_path = base_path
        else:
            base_path = os.path.join(os.path.dirname(__file__), os.pardir)
        if os.path.exists(base_path + '/.env'):
            file = open(base_path + '/.env')
            for line in file:
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]
            file.close()