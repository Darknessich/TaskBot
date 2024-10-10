from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    start: Start
    button: Button
    reminder: Reminder


class Start:
    @staticmethod
    def answer(*, username) -> Literal["""Привет, &lt;b&gt;{ $username }&lt;/b&gt;! Выбери действие:"""]: ...


class Button:
    new: ButtonNew
    list: ButtonList
    lang: ButtonLang
    set: ButtonSet

    @staticmethod
    def save() -> Literal["""Сохранить"""]: ...

    @staticmethod
    def cancel() -> Literal["""Отмена"""]: ...


class ButtonNew:
    @staticmethod
    def reminder() -> Literal["""Создать новое напоминание"""]: ...


class ButtonList:
    @staticmethod
    def reminders() -> Literal["""Запланированные напоминания"""]: ...

    @staticmethod
    def passed() -> Literal["""Прошедшие напоминания"""]: ...


class ButtonLang:
    @staticmethod
    def setup() -> Literal["""Выбор языка"""]: ...


class Reminder:
    @staticmethod
    def description() -> Literal["""&lt;b&gt;Описание:&lt;/b&gt;"""]: ...

    @staticmethod
    def time() -> Literal["""&lt;b&gt;Время:&lt;/b&gt;"""]: ...

    @staticmethod
    def period() -> Literal["""&lt;b&gt;Периодичность:&lt;/b&gt;"""]: ...

    @staticmethod
    def files() -> Literal["""&lt;b&gt;Файлы:&lt;/b&gt;"""]: ...


class ButtonSet:
    @staticmethod
    def description() -> Literal["""Изменить описание"""]: ...

    @staticmethod
    def time() -> Literal["""Изменить время"""]: ...

    @staticmethod
    def period() -> Literal["""Изменить период"""]: ...

    @staticmethod
    def files() -> Literal["""Изменить файлы"""]: ...

