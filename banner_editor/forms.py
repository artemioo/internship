from wtforms import Form, StringField, TextAreaField, validators, URLField, SelectField, FileField
from wtforms import IntegerField
from wtforms.widgets import HiddenInput

strip_filter = lambda x: x.strip() if x else None # удаление пробелов


class BannerCreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    image = FileField('картинка')

    url = URLField('ссылка на источник',
                   [validators.URL(require_tld=True, message='Введите корректный URL')], filters=[strip_filter])

    status = SelectField('Выбирете статус', choices=['Enabled', 'Disabled'],
                         coerce=str, option_widget=None, validate_choice=True)

    position = IntegerField('Позиция(приоритет) баннера')


class BannerUpdateForm(BannerCreateForm):
    id = IntegerField(widget=HiddenInput())
