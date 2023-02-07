from logger import logger


class ParserFindTagException(Exception):
    pass


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        logger.error(f'{tag} {attrs}: not found', stack_info=True)
        raise ParserFindTagException(f'{tag} {attrs}: not found')
    return searched_tag
