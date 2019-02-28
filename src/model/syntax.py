#!/usr/bin/env python3
import logging

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)


def analyze_syntax(text):
    # [START language_quickstart]
    # Imports the Google Cloud client library
    # [START language_python_migration_imports]
    # [END language_python_migration_imports]

    # Instantiates a client
    # [START language_python_migration_client]
    client = language.LanguageServiceClient()
    # [END language_python_migration_client]

    try:
        text = text.decode('utf-8')
    except AttributeError:
        pass

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    tokens = client.analyze_syntax(document=document).tokens

    logger.info('Text: {}'.format(text))
    for token in tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        logger.info(u'{}: {}'.format(part_of_speech_tag.name, token.text.content))
    # [END language_quickstart]

    return tokens


def get_nums(tokens):
    nums = []
    for token in tokens:
        part_of_speech_tag = enums.PartOfSpeech.Tag(token.part_of_speech.tag)
        if 'NUM' in part_of_speech_tag.name:
            nums.append(token.text.content)
    return nums


if __name__ == '__main__':
    while True:
        print(analyze_syntax(input('input: ')))
