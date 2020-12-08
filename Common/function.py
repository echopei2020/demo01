import os,configparser
def project_path():
    path1 = os.path.split(os.path.realpath(__file__))[0].split('C')[0]
    path2 = str(path1)
    return path2

def config_url():
    config=configparser.ConfigParser()
    file_config=project_path()+'config.ini'
    # print("config:",file_config)
    config.read(project_path()+'config.ini')
    return config.get('testUrl','url')
if __name__=='__main__':
    print(project_path())
    print(config_url())
    # project_path()
    # config_url()