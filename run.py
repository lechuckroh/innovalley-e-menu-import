from typing import List

from openpyxl import load_workbook


class Menu:
    def __init__(self, day, service_time, menu_type, main_title, items):
        self.day = day
        self.service_time = service_time
        self.menu_type = menu_type
        self.main_title = main_title
        self.items = items

    def __repr__(self):
        return f"{self.day} {self.service_time} {self.menu_type}: {self.main_title}, {','.join(self.items)}"


def remove_space(s: str) -> str:
    return s.replace(" ", "")


def get_cell_value(ws, col, row) -> str:
    value = ws[f"{col}{row}"].value
    return remove_space(value)


def get_cell_values(ws, col, row) -> List[str]:
    value = ws[f"{col}{row}"].value
    return value.splitlines() if value else []


def read_item(ws, service_time, menu_type, col, row_from, row_to) -> Menu:
    day = get_cell_value(ws, col, 3)
    lines: List[str] = []
    for row in range(row_from, row_to + 1):
        lines.extend(get_cell_values(ws, col, row))

    return Menu(
        day=day,
        service_time=service_time,
        menu_type=menu_type,
        main_title=lines[0],
        items=lines[1:],
    )


def read_day(ws, col):
    return [
        read_item(ws, "morning", "A", col, 4, 6),
        read_item(ws, "morning", "takeout", col, 7, 7),
        read_item(ws, "lunch", "A", col, 8, 13),
        read_item(ws, "lunch", "B", col, 14, 18),
        read_item(ws, "lunch", "takeout1", col, 19, 19),
        read_item(ws, "lunch", "takeout2", col, 20, 20),
        read_item(ws, "lunch", "plus", col, 21, 21),
    ]


def read_all(ws) -> List[Menu]:
    menus: List[Menu] = []
    menus.extend(read_day(ws, 'D'))
    menus.extend(read_day(ws, 'E'))
    menus.extend(read_day(ws, 'F'))
    menus.extend(read_day(ws, 'G'))
    menus.extend(read_day(ws, 'H'))
    return menus


wb = load_workbook(filename='samples/20.03.30.xlsx')
ws = wb.active
result = read_all(ws)
for m in result:
    print(m)
