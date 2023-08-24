from environs import Env

from dataclasses import dataclass


@dataclass
class Browser:
    browserPath: str
    homePage: str


@dataclass
class Steam:
    steamPath: str
    gameName: str
    gamePath: str


@dataclass
class Admin:
    adminId: int
    adminName: str


@dataclass
class Bot:
    botName: str
    botToken: str


@dataclass
class Config:
    steam: Steam
    browser: Browser
    admin: Admin
    bot: Bot


def load_config(path: str = None):
    env = Env()
    Env.read_env(path)

    return Config(
        steam=Steam(
            steamPath=env.str("STEAM_PATH"),
            gameName=env.str("GAME_NAME"),
            gamePath=env.str("GAME_PATH")
        ),
        browser=Browser(
            browserPath=env.str("BROWSER_PATH"),
            homePage=env.str("BROWSER_HOME_PAGE")
        ),
        admin=Admin(
            adminId=env.int("ADMIN_ID"),
            adminName=env.str("ADMIN_NAME")
        ),
        bot=Bot(
            botName=env.str("BOT_NAME"),
            botToken=env.str("BOT_TOKEN")
        )
    )
