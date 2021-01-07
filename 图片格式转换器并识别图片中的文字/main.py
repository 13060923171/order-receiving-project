from aip import AipOcr
APP_ID = '23499900'
API_KEY = 'T2fdzx29K8kYHFystc3El8EL'
SECRET_KEY = 'pWU0gDBRa6IW2xOyNwPobnjgbjHQi9lG'

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

try:
    client1 = AipOcr(APP_ID,API_KEY,SECRET_KEY)
    image = get_file_content('sample8.png')
    options = {}
    options['language_type'] = 'CHN_ENG'
    options['detect_direction'] = 'true'
    options['detect_language'] = 'true'
    options['probability'] = 'true'
    print(client1.accurate(image,options))
except:
    print('error')