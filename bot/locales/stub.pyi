from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    start: Start
    button: Button
    header: Header
    current: Current
    enter: Enter
    not_: Not_
    amount: Amount


class Start:
    @staticmethod
    def answer(*, username) -> Literal["""Привет, &lt;b&gt;{ $username }&lt;/b&gt;! Выбери действие:"""]: ...


class Button:
    new: ButtonNew
    list: ButtonList
    lang: ButtonLang
    set: ButtonSet
    main: ButtonMain
    without: ButtonWithout

    @staticmethod
    def save() -> Literal["""Сохранить"""]: ...

    @staticmethod
    def cancel() -> Literal["""Отмена"""]: ...

    @staticmethod
    def back() -> Literal["""Назад"""]: ...

    @staticmethod
    def done() -> Literal["""Выполнено"""]: ...

    @staticmethod
    def apply() -> Literal["""Подтвердить"""]: ...

    @staticmethod
    def delete() -> Literal["""Удалить"""]: ...


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


class Header:
    @staticmethod
    def description() -> Literal["""&lt;b&gt;Описание&lt;/b&gt;"""]: ...

    @staticmethod
    def date() -> Literal["""&lt;b&gt;Дата&lt;/b&gt;"""]: ...

    @staticmethod
    def time() -> Literal["""&lt;b&gt;Время&lt;/b&gt;"""]: ...

    @staticmethod
    def period() -> Literal["""&lt;b&gt;Периодичность&lt;/b&gt;"""]: ...

    @staticmethod
    def files() -> Literal["""&lt;b&gt;Файлы&lt;/b&gt;"""]: ...


class Current:
    @staticmethod
    def description() -> Literal["""&lt;b&gt;Текущее описание&lt;/b&gt;"""]: ...

    @staticmethod
    def date() -> Literal["""&lt;b&gt;Текущая дата&lt;/b&gt;"""]: ...

    @staticmethod
    def time() -> Literal["""&lt;b&gt;Текущее время&lt;/b&gt;"""]: ...

    @staticmethod
    def period() -> Literal["""&lt;b&gt;Текущая периодичность&lt;/b&gt;"""]: ...


class ButtonSet:
    @staticmethod
    def description() -> Literal["""Изменить описание"""]: ...

    @staticmethod
    def date() -> Literal["""Изменить дату"""]: ...

    @staticmethod
    def time() -> Literal["""Изменить время"""]: ...

    @staticmethod
    def period() -> Literal["""Изменить период"""]: ...

    @staticmethod
    def files() -> Literal["""Изменить файлы"""]: ...

    @staticmethod
    def reminder() -> Literal["""Изменить"""]: ...

    @staticmethod
    def passed() -> Literal["""Создать аналогичное"""]: ...


class ButtonMain:
    @staticmethod
    def menu() -> Literal["""Главное меню"""]: ...


class Enter:
    @staticmethod
    def description() -> Literal["""Введите новое описание"""]: ...

    @staticmethod
    def date() -> Literal["""Выберите дату"""]: ...

    @staticmethod
    def time() -> Literal["""Выберите время"""]: ...

    @staticmethod
    def period() -> Literal["""Выберите периодичность"""]: ...

    @staticmethod
    def files() -> Literal["""Добавьте/Удалите файлы"""]: ...


class Not_:
    @staticmethod
    def periodically() -> Literal["""не периодично"""]: ...


class ButtonWithout:
    @staticmethod
    def period() -> Literal["""Без периода"""]: ...


class Amount:
    @staticmethod
    def reminders() -> Literal["""&lt;b&gt;Всего запланнированных напоминаний&lt;/b&gt;"""]: ...

    @staticmethod
    def passed() -> Literal["""&lt;b&gt;Всего прошедших напоминаний&lt;/b&gt;"""]: ...

