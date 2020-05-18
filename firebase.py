from collections import defaultdict
from datetime import date
from typing import List, Dict

from menu import Menu, format_date


def group_by_service_time(menus: List[Menu]):
    multimap: Dict[str, List[Menu]] = defaultdict(list)
    for menu in menus:
        multimap[menu.service_time].append(menu)

    result = dict()
    for service_time, menu_list in multimap.items():
        menu_by_type = dict()
        for menu in menu_list:
            menu_by_type[menu.menu_type] = menu.to_dict()
        result[service_time] = menu_by_type

    return result


def group_by_date(menus: List[Menu]):
    multimap: Dict[date, List[Menu]] = defaultdict(list)
    for menu in menus:
        multimap[menu.day].append(menu)

    result = dict()
    for date_, menu_list in multimap.items():
        result[format_date(date_)] = group_by_service_time(menu_list)

    return result


def update_menus(db, id_token, menus: List[Menu]):
    data = group_by_date(menus)
    db.child("menus").child("by-date").update(data, id_token)
