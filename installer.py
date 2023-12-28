import shutil


def run(config):
    # Persistent Empires files license
    if config['pe_server_license'] is not None:
        src = config['pe_server_license']
        dst = f"{config['destination']}"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
    # Bannerlord Dedicated
    if config['bannerlord'] is not None:
        src = config['bannerlord']
        dst = f"{config['destination']}"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
    # Persistent Empires
    if config['pe'] is not None:
        for folder in ['DsAssetPackages', 'ModuleData', 'Prefabs', 'SceneObj']:
            src = f"{config['pe']}\\{folder}"
            dst = f"{config['destination']}\\Modules\\PersistentEmpires\\{folder}"
            print(f'{src}\n> {dst}')
            shutil.copytree(src, dst, dirs_exist_ok=True)
    # Persistent Empires submodule
    if config['pe_submodule_file'] is not None:
        src = config['pe_submodule_file']
        dst = f"{config['destination']}\\Modules\\PersistentEmpires\\SubModule.xml"
        print(f'{src}\n> {dst}')
        shutil.copy2(src, dst)
    # Persistent binary files
    if config['pe_bin'] is not None:
        src = config['pe_bin']
        dst = f"{config['destination']}\\bin\\Win64_Shipping_Server"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
    # Persistent Empires config
    if config['pe_config'] is not None:
        src = config['pe_config']
        dst = f"{config['destination']}\\Modules\\PersistentEmpires\\ModuleData\\Configs"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
    # Bannerlord mission files (.txt)
    if config['mission'] is not None:
        src = config['mission']
        dst = f"{config['destination']}\\Modules\\Native"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
    # Server starters (.bat)
    if config['starter'] is not None:
        src = config['starter']
        dst = f"{config['destination']}\\bin\\Win64_Shipping_Server"
        print(f'{src}\n> {dst}')
        shutil.copytree(src, dst, dirs_exist_ok=True)
