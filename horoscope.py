import requests
from requests import RequestException
from bs4 import BeautifulSoup
from constants.constants import AQUARIUS_URL, SAGINARIUS_URL, LIBRA_URL, VIRGO_URL
from utils import find_tag


class Horoscope:

    @staticmethod
    def aquarius_prediction() -> str:
        aquarius_horoscope = requests.get(AQUARIUS_URL)
        if aquarius_horoscope is None:
            raise RequestException(f'Error: {aquarius_horoscope} not found')
        soup = BeautifulSoup(aquarius_horoscope.text, 'lxml')
        find_div_aquarius = find_tag(
            soup,
            'div',
            attrs={'class': 'cols__column cols__column_small_32 cols__column_medium_43 cols__column_large_47'}
        )
        return find_tag(find_div_aquarius, 'p').text

    @staticmethod
    def saginarius_prediction() -> str:
        saginarius_horoscope = requests.get(SAGINARIUS_URL)
        if saginarius_horoscope is None:
            return f'Error {saginarius_horoscope} path not found'
        soup = BeautifulSoup(saginarius_horoscope.text, 'lxml')
        find_div_saginarius = find_tag(
            soup,
            'div',
            attrs={'class': 'cols__column cols__column_small_32 cols__column_medium_43 cols__column_large_47'}
        )
        return find_tag(find_div_saginarius, 'p').text

    @staticmethod
    def libra_prediction() -> str:
        libra_horoscope = requests.get(LIBRA_URL)
        if libra_horoscope is None:
            return f'Error {libra_horoscope} not found'
        soup = BeautifulSoup(libra_horoscope.text, 'lxml')
        find_div_libra = find_tag(
            soup,
            'div',
            attrs={'class': 'cols__column cols__column_small_32 cols__column_medium_43 cols__column_large_47'}
        )
        return find_tag(find_div_libra, 'p').text

    @staticmethod
    def virgo_prediction() -> str:
        virgo_prediction = requests.get(VIRGO_URL)
        if virgo_prediction is None:
            return f'Error: {virgo_prediction} not found'
        soup = BeautifulSoup(virgo_prediction.text, 'lxml')
        find_div_virgo = find_tag(
            soup,
            'div',
            attrs={'class': 'cols__column cols__column_small_32 cols__column_medium_43 cols__column_large_47'}
        )
        return find_tag(find_div_virgo, 'p').text
