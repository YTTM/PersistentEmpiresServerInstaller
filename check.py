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
    raise NotImplementedError
