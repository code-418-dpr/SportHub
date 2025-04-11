import re
import logging

MALE_KEYWORDS = {'мальчики', 'юноши', 'юниоры', 'мужчины'}
FEMALE_KEYWORDS = {'девочки', 'девушки', 'юниорки', 'женщины'}
HYPHEN_REGEX = re.compile(r'\s*-\s*')

logger = logging.getLogger(__name__)
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    filemode='a',
    format='%(name)s %(asctime)s %(levelname)s %(message)s',
)


def parse(source: str) -> dict[str, list[bool] | list[int]]:
    genders: list[bool] = [False, False]
    ages: list[int] = []
    last_word = ''
    source = HYPHEN_REGEX.sub('-', source)

    try:
        for word in source.split():
            if any(keyword in word.lower() for keyword in MALE_KEYWORDS):
                genders[0] = True
            elif any(keyword in word.lower() for keyword in FEMALE_KEYWORDS):
                genders[1] = True
            elif word.isdigit():
                if last_word == 'от':
                    ages.append((int(word), 100))
                elif last_word == 'до':
                    ages.append((0, int(word)))
            elif '-' in word:
                start, end = map(int, word.split('-'))
                ages.append((start, end))
            last_word = word
        if not ages:
            ages.append((0, 100))
    except Exception:
        logger.exception('Ошибка при парсинге участников события')

    return { 'ages': ages, 'genders': genders }
