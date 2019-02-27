#!/usr/bin/env python3
import json
import os
import logging

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as xmlParser

import code.dust as dust_code


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)


file_dir = os.path.realpath(__file__)
config_dir = os.path.normpath(os.path.join(file_dir, '../../../env/config.json'))

fp = open(config_dir)
config = json.load(fp)

api_key = config['api_key']
end_point = config['end_point']


def get_dust(state='seoul'):
    url = '{}/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'.format(end_point)

    query_params = '?' + urlencode({
        quote_plus('ServiceKey'): unquote(api_key),
        quote_plus('numOfRows'): '1',
        quote_plus('PageNo'): '1',
        quote_plus('itemCode'): 'PM10',
        quote_plus('dataGubun'): 'HOUR',
        quote_plus('searchCondition'): 'WEEK'
    })

    request = Request(url + query_params, method='GET')
    response_body = urlopen(request).read().decode('utf-8')
    root = xmlParser.fromstring(response_body)

    dust = root.find('body').find('items').find('item').find(state).text
    dust = int(dust)
    logger.info('dust measurement value: {}'.format(dust))

    return dust


def get_dust_level(dust):
    level = None
    if 0 <= dust <= 30:
        level = dust_code.Level.GOOD
    if 31 <= dust <= 80:
        level = dust_code.Level.AVERAGE
    if 81 <= dust <= 150:
        level = dust_code.Level.BAD
    if dust >= 151:
        level = dust_code.Level.VERY_BAD

    logger.info('dust level: {}'.format(level))
    return level


if __name__ == '__main__':
    print(get_dust_level(get_dust()))
