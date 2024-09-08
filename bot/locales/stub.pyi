from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    start: Start
    button: Button


class Start:
    @staticmethod
    def answer(*, username) -> Literal["""Привет, &lt;b&gt;{ $username }&lt;/b&gt;!
Я &amp;#x2014; Бот для создания напоминаний."""]: ...


class Button:
    new: ButtonNew
    list: ButtonList
    lang: ButtonLang


class ButtonNew:
    @staticmethod
    def reminder() -> Literal["""Создать новое напоминание"""]: ...


class ButtonList:
    @staticmethod
    def reminders() -> Literal["""Список запланированных напоминаний"""]: ...

    @staticmethod
    def passed() -> Literal["""Список прошедших напоминаний"""]: ...


class ButtonLang:
    @staticmethod
    def setup() -> Literal["""Выбор языка"""]: ...

