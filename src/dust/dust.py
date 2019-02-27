import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET

import code.dust as DUST_CODE


fp = open('../env/config.json')
config = json.load(fp)

api_key = config['api_key']
end_point = config['end_point']


def get_dust(state='seoul'):
    API_key = unquote(api_key)
    url = '{}/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'.format(end_point)

    query_params = '?' + urlencode({
        quote_plus('ServiceKey'): API_key,
        quote_plus('numOfRows'): '1',
        quote_plus('PageNo'): '1',
        quote_plus('itemCode'): 'PM10',
        quote_plus('dataGubun'): 'HOUR',
        quote_plus('searchCondition'): 'WEEK'
    })

    request = Request(url + query_params, method='GET')
    response_body = urlopen(request).read().decode('utf-8')
    root = ET.fromstring(response_body)

    dust = root.find('body').find('items').find('item').find(state).text
    return int(dust)


def get_dust_level(dust):
    if 0 <= dust <= 30:
        return DUST_CODE.LEVEL.GOOD
    if 31 <= dust <= 80:
        return DUST_CODE.LEVEL.AVERAGE
    if 81 <= dust <= 150:
        return DUST_CODE.LEVEL.BAD
    if dust >= 151:
        return DUST_CODE.LEVEL.VERY_BAD


if __name__ == '__main__':
    print(get_dust())
