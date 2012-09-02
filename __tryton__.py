# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name' : 'Calendar',
    'name_bg_BG' : 'Календар',
    'name_de_DE' : 'Kalender',
    'name_es_CO' : 'Calendario',
    'name_es_ES' : 'Calendario',
    'name_fr_FR' : 'Calendrier',
    'name_ru_RU' : 'Календарь',
    'version' : '2.2.2',
    'author' : 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': 'Add CalDAV support',
    'description_bg_BG' : 'Добавя подръжка на CalDAV',
    'description_de_DE' : 'Fügt Unterstützung für CalDAV hinzu',
    'description_es_CO' : 'Añade soporte para CalDAV',
    'description_es_ES' : 'Añade soporte para CalDAV',
    'description_fr_FR' : 'Ajoute le support CalDAV',
    'description_ru_RU' : 'Добавление поддержки CalDAV',
    'depends' : [
        'ir',
        'res',
        'webdav',
    ],
    'xml' : [
        'calendar.xml',
    ],
    'translation': [
        'locale/bg_BG.po',
        'locale/cs_CZ.po',
        'locale/de_DE.po',
        'locale/es_CO.po',
        'locale/es_ES.po',
        'locale/fr_FR.po',
        'locale/nl_NL.po',
        'locale/ru_RU.po',
    ],
}
