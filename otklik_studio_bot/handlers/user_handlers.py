from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from typing import List
from otklik_studio_bot.keyboards.keyboards import primary_kb, services_prices_kb, kb_fotosessions, kb_certificates, contacts_kb, kb_about_studio, faq_keyboard, faq_answer_keyboard
from otklik_studio_bot.lexicon.lexicon_ru import LEXICON_RU, LEXICON_FAQ_RU
from otklik_studio_bot.services.services import get_bot_choice, get_winner
from otklik_studio_bot.services.score_service import score_counter, list_counter

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=primary_kb)


# Этот хэндлер будет срабатывать на кнопку 'about_studio'
# и отправлять в чат текст про студию и клавиатуру с 1 кнопкой "Вернуться назад"
@router.callback_query(F.data == 'btn_about_studio_pressed')
async def process_btn_about_studio_pressed(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text=LEXICON_RU['text_about_studio'],
        reply_markup=kb_about_studio
)

# Этот хэндлер будет срабатывать на кнопку 'faq'
# и отправлять в чат текст с пронумерованными вопросами и клавиатуру с кнопками "Вернуться назад"
@router.callback_query(F.data == 'btn_faq_pressed')
async def process_btn_faq_pressed(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text=LEXICON_RU['text_faq'],
        reply_markup=faq_keyboard
)

# Этот хэндлер будет срабатывать на кнопку 'contacts'
# и отправлять в чат клавиатуру с инлайн-кнопками
@router.callback_query(F.data == 'btn_about_contacts_pressed')
async def process_btn_contacts_pressed(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text=LEXICON_RU['text_about_contacts'],
        reply_markup=contacts_kb
)



# Этот хэндлер будет срабатывать на кнопку 'services_prices'
# и отправлять в чат клавиатуру с инлайн-кнопками
@router.callback_query(F.data == 'btn_services_prices_pressed')
async def process_btn_services_prices_pressed(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        text=LEXICON_RU['text_services_prices'],
        reply_markup=services_prices_kb
)


# Этот хэндлер будет срабатывать на кнопку 'fotosessions'
# и отправлять в чат сообщение и 1  инлайн-кнопку c url
@router.callback_query(F.data == 'btn_fotosessions_pressed')
async def process_btn_fotosessions_pressed(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['text_about_fotosessions'],
        reply_markup=kb_fotosessions
    )


# Этот хэндлер будет срабатывать на кнопку 'certificates'
# и отправлять в чат сообщение и клавиатуру для сертификатов
@router.callback_query(F.data == 'btn_certificates_pressed')
async def process_btn_certificates_pressed(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['text_about_certificate'],
        reply_markup=kb_certificates
    )


# Этот хэндлер будет срабатывать на кнопку 'come_back'
# скрывать предыдущее сообщение и таким образом вернулись к первичному меню
@router.callback_query(F.data == 'btn_come_back_pressed')
async def process_btn_come_back_pressed(callback: CallbackQuery):
    await callback.message.delete()


# # Этот хэндлер срабатывает на любую из игровых кнопок
# @router.message(F.text.in_([LEXICON_RU['rock'],
#                             LEXICON_RU['paper'],
#                             LEXICON_RU['scissors']]))
# async def process_game_button(message: Message):
#     bot_choice = get_bot_choice()
#     await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
#                               f'- {LEXICON_RU[bot_choice]}')
#     winner = get_winner(message.text, bot_choice)
#     # score_service
#     list_counter.append(winner)
#     await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


# # Этот хэндлер будет срабатывать на кнопку '1', те 1 вопрос из FAQ
# # и отправлять в чат сообщение - ответ на 1 вопрос и  инлайн-кнопку Вернуться к списку вопросов
# @router.callback_query(F.data == 'btn_question_1_pressed')
# async def process_btn_question_1_pressed(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer(
#         text=LEXICON_FAQ_RU['1_faq_answer_text'],
#         reply_markup=faq_answer_keyboard
#     )

# В цикле создадим хэндлеры, которые срабатывают на кнопки вопросоов faq '1' - '11', те 1 вопрос из FAQ
# и отправлять в чат сообщение - ответ на i вопрос и  инлайн-кнопку Вернуться к списку вопросов
def create_faq_question_handler(i):
    @router.callback_query(F.data == f'btn_question_{i}_pressed')
    async def process_btn_question_pressed(callback: CallbackQuery):
        await callback.answer()
        await callback.message.answer(
            text=LEXICON_FAQ_RU[f'{i}_faq_answer_text'],
            reply_markup=faq_answer_keyboard
        )

for i in range(1, 12):
    create_faq_question_handler(i)

# Этот хэндлер будет срабатывать на кнопку 'btn_come_back_faq_list'
# скрывать предыдущее сообщение и таким образом вернулись к списку вопросов
@router.callback_query(F.data == 'btn_come_back_faq_list_pressed')
async def process_btn_come_back_pressed(callback: CallbackQuery):
    await callback.message.delete()