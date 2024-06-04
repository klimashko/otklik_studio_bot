from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_FAQ_RU

# ------- Создаем клавиатуру через InlineKeyboardBuilder-------
# ------- клавиатуру, которую отображаем на команду /start -------

# Создаем кнопки клавиатуры
btn_about_studio = InlineKeyboardButton(
    text=LEXICON_RU['about_studio'],
    callback_data='btn_about_studio_pressed'
)

btn_video_guide = InlineKeyboardButton(
    text=LEXICON_RU['video_guide'],
    url='https://www.instagram.com/p/C48CPTPIftr/')

btn_faq = InlineKeyboardButton(
    text=LEXICON_RU['faq'],
    callback_data='btn_faq_pressed'
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
    callback_data='btn_about_contacts_pressed'
)

# Инициализируем билдер для клавиатуры с первичным набором кнопок
primary_kb_builder = InlineKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=1
primary_kb_builder.row(
    btn_about_studio, btn_video_guide, btn_faq, btn_book_a_photoshoot, btn_bye_sertificate,
    btn_services_prices,
    btn_location, btn_contacts, width=1)

# Создаем клавиатуру с первичным набором кнопок
primary_kb: InlineKeyboardMarkup = primary_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# --- Создаем клавиатуру, которую отображаем на нажатие кнопки 'faq'
# ---через InlineKeyboardBuilder-

# --- Создаем кнопку вернуться назад, которую добавим в клавиатуру ---
btn_come_back = InlineKeyboardButton(
    text=LEXICON_RU['come_back'],
    callback_data='btn_come_back_pressed'
)

# Список для хранения всех кнопок вопросов с 1 по 11 с использованием list comprehension
faq_buttons = [
    InlineKeyboardButton(
        text=LEXICON_FAQ_RU[str(i)],
        callback_data=f'btn_question_{i}_pressed'
    ) for i in range(1, 12)
]

# Создание билдера для клавиатуры, которая отображается при нажатии кнопки 'faq'
faq_kb_builder = InlineKeyboardBuilder()

# Добавление кнопок в билдер
faq_kb_builder.row(*faq_buttons, btn_come_back)
faq_kb_builder.adjust(3, 3, 3, 2, 1)  # Указали сколько кнопок будет в рядах

# Создаем клавиатуру FAQ
faq_keyboard: InlineKeyboardMarkup = faq_kb_builder.as_markup(resize_keyboard=True)

# Создаем кнопку и клавиатуру, которая будет отображаться,
# при нажатии на кнопку Вернуться назад
btn_come_back_faq_list = InlineKeyboardButton(
    text=LEXICON_FAQ_RU['come_back_faq_list'],
    callback_data='btn_come_back_faq_list_pressed'
)

faq_answer_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[btn_come_back_faq_list]]
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

# --- Создаем кнопку вернуться назад, которую мб добавим в клавиатуры ---
# btn_come_back уже создана выше строка 71

# Создаем объект инлайн-клавиатуры
kb_fotosessions = InlineKeyboardMarkup(
    inline_keyboard=[[btn_choose_session_pay], [btn_certificates], [btn_come_back]]
)

# --- Создаем клавиатуру, которую отображаем на нажатие кнопки 'certificates' ---
btn_certificates = InlineKeyboardButton(
    text=LEXICON_RU['bye_sertificate'],
    url='https://n1035709.yclients.com/company/960077/personal/select-services?')
# В этой клавиатуре kb_certificates тоже используем кнопку вернуться назад  btn_come_back---
# Создаем объект инлайн-клавиатуры
kb_certificates = InlineKeyboardMarkup(
    inline_keyboard=[[btn_certificates], [btn_fotosessions], [btn_come_back]]
)

# --- Создаем клавиатуру через InlineKeyboardBuilder---
# --- клавиатуру, которую отображаем на нажатие кнопки 'contacts' ---

# Создаем кнопки клавиатуры
btn_email = InlineKeyboardButton(
    text=LEXICON_RU['email'],
    url='mailto:milena77756@yandex.ru'  # Эта нопка давала ошибку- адрес инвалид, пришлось убрать из клавы
)

btn_instagram = InlineKeyboardButton(
    text=LEXICON_RU['instagram'],
    url='https://www.instagram.com/otklik.studio?igsh=MTZyY3RxeW4zMW80MA%3D%3D&utm_source=qr'
)

btn_whatsapp = InlineKeyboardButton(
    text=LEXICON_RU['whatsapp'],
    url='https://api.whatsapp.com/send/?phone=79605209672&text&type=phone_number&app_absent=0'
)

btn_telegram = InlineKeyboardButton(
    text=LEXICON_RU['telegram'],
    url='https://t.me/otklik40'
)

btn_vkontakte = InlineKeyboardButton(
    text=LEXICON_RU['vkontakte'],
    url='https://vk.com/club224538241'
)
contacts_kb_builder = InlineKeyboardBuilder()

contacts_kb_builder.row(btn_vkontakte, btn_telegram, btn_whatsapp, btn_instagram, btn_come_back)

# Явно сообщаем билдеру сколько хотим видеть кнопок в рядах
contacts_kb_builder.adjust(2, 2, 1, 1)

# Создаем клавиатуру
contacts_kb: InlineKeyboardMarkup = contacts_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# --- Создаем клавиатуру, которую отображаем на нажатие кнопки 'about_studio' ---
# В этой клавиатуре ut_studio тоже используем кнопку вернуться назад  btn_come_back---
# Создаем объект инлайн-клавиатуры
kb_about_studio = InlineKeyboardMarkup(
    inline_keyboard=[[btn_come_back]]
)
