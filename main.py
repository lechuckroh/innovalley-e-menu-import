import configparser
import logging
import os
import sys
from typing import Any, List

import click
from dotenv import load_dotenv
from pyrebase import pyrebase
from pyrebase.pyrebase import Database

from firebase import update_menus
from menu import load_excel, Menu


@click.group()
def cli():
    pass


@click.command(name="import")
@click.argument('file')
@click.option('-c', '--config', default='config.ini')
@click.option('-v', '--verbose', count=True)
def import_(file: str, config: str, verbose: int):
    init_logger(verbose)

    menu_list: List[Menu] = []
    if os.path.isdir(file):
        for f in os.listdir(file):
            if f.endswith(".xlsx"):
                menu_list.extend(load_excel(os.path.join(file, f)))
    else:
        menu_list.extend(load_excel(file))

    for menu in menu_list:
        logging.info(menu)

    cfg = load_config(config)
    db, user = init_firebase(cfg)
    id_token = user["idToken"]
    update_menus(db, id_token, menu_list)


cli.add_command(import_)


# 로그 설정
def init_logger(verbose: int):
    root = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    level = logging.INFO

    if verbose >= 1:
        level = logging.DEBUG

    root.setLevel(level)
    handler.setLevel(level)


# 설정 파일 로그
def load_config(filename):
    cfg_path = filename if os.path.isabs(filename) else os.path.abspath(
        os.path.join(os.path.dirname(__file__), filename))

    config = configparser.RawConfigParser()
    dataset = config.read(cfg_path)
    if len(dataset) == 0:
        sys.exit(f'failed to load {cfg_path}')

    logging.info(f'[LOAD] {cfg_path}')
    return config


# Firebase DB 연결
def init_firebase(cfg) -> (Database, Any):
    fb = cfg['Firebase']

    api_key = os.getenv("INNO_API_KEY")
    if api_key:
        fb["apiKey"] = api_key
    email = os.getenv("INNO_EMAIL") or fb["email"]
    password = os.getenv("INNO_PASSWORD") or fb["password"]

    firebase = pyrebase.initialize_app(fb)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    db = firebase.database()
    return db, user


if __name__ == '__main__':
    load_dotenv()
    cli()
