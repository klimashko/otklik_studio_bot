from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


from otklik_studio_bot.lexicon.lexicon_ru import LEXICON_RU


# ------- Создаем клавиатуру через InlineKeyboardBuilder-------
# ------- клавиатуру, которую отображаем на команду /start -------

# Создаем кнопки клавиатуры
btn_about_studio = InlineKeyboardButton(
    text=LEXICON_RU['about_studio'],
    callback_data='btn_about_studio_pressed'
)
btn_book_a_photoshoot = InlineKeyboardButton(
    text=LEXICON_RU['book_a_photoshoot'],
    url='https://n1035709.yclients.com/company/960077/personal/select-time?')

btn_bye_sertificate = InlineKeyboardButton(
    text=LEXICON_RU['bye_sertificate'],
    url='https://n1035709.yclients.com/company/960077/personal/select-services?')

btn_services_prices = InlineKeyboardButton(
    text=LEXICON_RU['services_prices'],
    callback_data='btn_services_prices_pressed'
)

btn_location = InlineKeyboardButton(
    text=LEXICON_RU['location'],
    url='https://yandex.ru/maps/967/obninsk/house/dolgininskaya_ulitsa_20/Z08Ycw9hS0EHQFtvfX1xeX9iZw==/'
        '?from=mapframe&ll=36.581218%2C55.108192&source=mapframe&um='
        'constructor%3A6335d1707e795bb4aa4cfc17cb2afe681a890b0c57e9d23580c7529bb348f45a&utm_source='
        'mapframe&z=19.2')

btn_contacts = InlineKeyboardButton(
    text=LEXICON_RU['contacts'],
    callback_data='btn_about_studio_pressed'
)

# Инициализируем билдер для клавиатуры с первичным набором кнопок
primary_kb_builder = InlineKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=1
primary_kb_builder.row(btn_about_studio, btn_book_a_photoshoot, btn_bye_sertificate, btn_services_prices, btn_location, btn_contacts, width=1)

# Создаем клавиатуру с первичным набором кнопок
primary_kb: InlineKeyboardMarkup = primary_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# --- Создаем клавиатуру через InlineKeyboardBuilder---
# --- клавиатуру, которую отображаем на нажатие кнопки 'services_prices' ---

# Создаем кнопки клавиатуры
btn_fotosessions = InlineKeyboardButton(
    text=LEXICON_RU['fotosessions'],
    callback_data='btn_fotosessions_pressed'
)

btn_certificates = InlineKeyboardButton(
    text=LEXICON_RU['certificates'],
    callback_data='btn_certificates_pressed'
)

services_prices_kb_builder = InlineKeyboardBuilder()

services_prices_kb_builder.row(btn_fotosessions, btn_certificates, width=1)

services_prices_kb: InlineKeyboardMarkup = services_prices_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)


# --- Создаем клавиатуру, которую отображаем на нажатие кнопки 'fotosessions' ---
btn_choose_session_pay = InlineKeyboardButton(
    text=LEXICON_RU['choose_session_pay'],
    url='https://n1035709.yclients.com/company/960077/personal/select-time?')

# Создаем объект инлайн-клавиатуры
kb_fotosessions = InlineKeyboardMarkup(
    inline_keyboard=[[btn_choose_session_pay], [btn_certificates]]
)

# --- Создаем клавиатуру, которую отображаем на нажатие кнопки 'certificates' ---
btn_certificates = InlineKeyboardButton(
    text=LEXICON_RU['bye_sertificate'],
    url='https://n1035709.yclients.com/company/960077/personal/select-services?')

# Создаем объект инлайн-клавиатуры
kb_certificates = InlineKeyboardMarkup(
    inline_keyboard=[[btn_certificates], [btn_fotosessions]]
)
