__author__ = 'mriegel'

storage = {}


def get_cfg(name):
    fnc = 'get_'+name+'_cfg()'

    try:
        config = eval(fnc)
        return config
    except:
        raise NotImplementedError


def get_user_cfg():
    from user import UserConfig
    return load_cfg('user', UserConfig)


def get_package_cfg():
    from package import PackageConfig
    return load_cfg('package', PackageConfig)


def get_api_cfg():
    from api import ApiConfig
    return load_cfg('api', ApiConfig)


def load_cfg(namespace, config):
    if not namespace in storage:
        storage[namespace] = config()
    return storage[namespace]