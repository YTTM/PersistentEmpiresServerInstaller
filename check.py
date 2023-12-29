import os


def configuration(config):
    flags = [False, False, False, False, False, False, False, False, False, False]
    if 'pe_server_license' in config.keys():
        flags[0] = True
    if 'bannerlord' in config.keys():
        flags[1] = True
    if 'pe' in config.keys():
        flags[2] = True
    if 'pe_submodule_file' in config.keys():
        flags[3] = True
    if 'pe_bin' in config.keys():
        flags[4] = True
    if 'pe_config' in config.keys():
        flags[5] = True
    if 'mission' in config.keys():
        flags[6] = True
    if 'starter' in config.keys():
        flags[7] = True
    if 'destination' in config.keys():
        flags[8] = True
    if len(config.keys()) == 9:
        flags[9] = True

    return flags


def paths(config):
    flags = [False, False, False, False, False, False, False, False, False]

    def isvalidpath(path):
        try:
            if os.path.exists(path):
                return True
        except Exception:
            pass
        return False

    if config['pe_server_license'] is None:
        flags[0] = 'skip'
    elif isvalidpath(config['pe_server_license']):
        flags[0] = 'exists'
    if config['bannerlord'] is None:
        flags[1] = 'skip'
    elif isvalidpath(config['bannerlord']):
        flags[1] = 'exists'
        if isvalidpath(f"{config['bannerlord']}/bin/Win64_Shipping_Server/DedicatedCustomServer.Starter.exe"):
            flags[1] = True
    if config['pe'] is None:
        flags[2] = 'skip'
    elif isvalidpath(config['pe']):
        flags[2] = 'exists'
    if config['pe_submodule_file'] is None:
        flags[3] = 'skip'
    elif isvalidpath(config['pe_submodule_file']):
        flags[3] = 'exists'
    if config['pe_bin'] is None:
        flags[4] = 'skip'
    elif isvalidpath(config['pe_bin']):
        flags[4] = 'exists'
    if config['pe_config'] is None:
        flags[5] = 'skip'
    elif isvalidpath(config['pe_config']):
        flags[5] = 'exists'
    if config['mission'] is None:
        flags[6] = 'skip'
    elif isvalidpath(config['mission']):
        flags[6] = 'exists'
    if config['starter'] is None:
        flags[7] = 'skip'
    elif isvalidpath(config['starter']):
        flags[7] = 'exists'
    if config['destination'] is None:
        flags[8] = 'skip'
    elif isvalidpath(config['destination']):
        flags[8] = 'exists'

    return flags
