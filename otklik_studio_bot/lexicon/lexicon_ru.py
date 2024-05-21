LEXICON_RU: dict[str, str] = {
    '/start': '<b>Привет!</b>\n\nЭто бот фотостудии автопортрета <b>"Отклик"</b>\n\n'
              'Я помогу вам узнать о наших услугах,\n'
              'ценах и подарочных сертификатах,\n'
              'как записаться на фотосессию и как нас найти!',
    'about_studio': '❓Что такое студия ОТКЛИК?',
    'video_guide': '🪄 Как происходит съемка (смотреть видео)',
    'faq': '❓Часто задаваемые вопросы',
    'book_a_photoshoot': '📅 Записаться на фотосессию',
    'bye_sertificate': '🎁 Купить сертификат',
    'services_prices': '🪙 Узнать об услугах и ценах',
    'location': '🧭 Локация, как добраться',
    'contacts': '☎ Контакты и соцсети',
    'email': 'Email',
    'instagram': 'Instagram',
    'whatsapp': 'WhatsApp',
    'telegram': 'Telegram',
    'vkontakte': 'ВКонта́кте',
    'fotosessions': 'Фотосессии',
    'certificates': 'Подарочные сертификаты',
    'text_services_prices': 'Чтобы ознакомиться с услугами и ценами, выберите кнопку ниже:',
    'choose_session_pay': '📸 Выбрать фотосессию и оплатить',
    'come_back': 'Вернуться назад',
    'mock_for_btn_next_question': 'mock_for_btn_next_question',
    'other_answer': 'Извините, это сообщение мне непонятно...',
    'text_about_studio': 'Фотостудия автопортрета ОТКЛИК,\n'
                         'первая студия в г. Обнинске, где ты сам себе фотограф.\n'
                         'Только Ты, пульт и Зеркало.\n\n'
                         'Любишь позировать перед зеркалом?\n'
                         'Тогда этот совершенно новый формат точно для тебя!\n'
                         'Просто смотри в зеркало и жми на кнопку!\n\n'
                         'Ты сразу увидишь отличный кадр,\n'
                         'потому что рядом с зеркалом установлен монитор!\n\n'
                         'Свет и камера уже профессионально настроены.\n'
                         'Осталось только позировать и кликать на кнопку  😉',
    'text_about_fotosessions': 'У нас есть 3 временных слота, планируя время,\n'
                               'пожалуйста, учтите дополнительно 15 минут на инструктаж:\n\n'
                               '<b>25 минут = 2500 рублей</b>\n'
                               'Подойдет, если вы просто хотите попробовать этот формат съемки и точно знаете,\n'
                               'что хотите снять (запись на эту фотосессию возможна только на первое посещение).\n'
                               'До 4 человек, за последующего 500.\n\n'
                               '<b>45 минут = 5000 рублей</b>\n'
                               'Оптимально для 1-2 человек, этого времени хватит, чтобы освоиться и войти во вкус.\n'
                               'Один фон на ваш выбор. До 4 человек, за последующего 1000.\n'
                               'Комплимент от студии – кофе и чай с вкусняшками.\n\n'
                               '<b>90 минут = 8500 рублей</b>\n'
                               'Подойдет, если у вас много образов и идей или вы пришли с семьей или с друзьями. Два фона на ваш выбор.\n'
                               'До 4 человек, за последующего 1000. Также дополнительно можем предложить экспресс-макияж.\n'
                               'Комплимент от студии – кофе и чай с вкусняшками.\n'
                               'В студии будет комфортно небольшой компании до 10 человек.\n'
                               'Большее количество посетителей возможно, оно обговаривается заранее с администратором студии.',
    'text_about_certificate': 'Подарочный сертификат на фотосессию в студию автопортрета «ОТКЛИК»\n'
                            'будет хорошим полноценным подарком или может стать отличным дополнением к основному\n\n'
                            '❤ Срок действия сертификата 3 месяца\n\n'
                            '👍 Есть электронный и печатный вариант сертификата\n\n'
                            '✅ Напечатанные сертификаты всегда в наличии\n\n'
                            '🚁 Бесплатная доставка по городу\n\n'
                            '🪙 Удобный для вас способ оплаты: карта, перевод, наличные',
    'text_about_contacts': 'Адрес: г.Обнинск, Долгининская улица, 20, офис 162\n\n'
                            'Время работы: ежедневно с 10:00 до 22:00\n\n'
                            'Телефон: +79605209672'
}

# В этом словаре хранятся команды и их описания command  description для кнопки menu
# и используются для установки команд меню в файле keyboards/set_menu
LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Запустить бот'
}

LEXICON_FAQ_RU: dict[str, str] = {
    'text_faq': '1. Сколько времени длится фотосессия?\n\n'
                '2. Можно ли сниматься в обуви?\n\n'
                '3. Можно ли приносить или заказывать еду и напитки в студию?\n\n'
                '4. Можно ли приводить на фотосессию домашних животных?\n\n'
                '5. Как подготовиться к съемке?\n\n'
                '6. Как перенести или отменить съемку?\n\n'
                '7. Сколько фотографий я получу в результате?\n\n'
                '8. Кто может увидеть мои фотографии?\n\n'
                '9. Кто обрабатывает мои фотографии?\n\n'
                '10. Как получить у вас консультацию по открытию студии автопортрета в своем городе?\n\n'
                '11. Что нельзя делать в студии?\n\n'
                'Чтобы получить ответ на интересующий вопрос,\n'
                'нажмите на кнопку cнизу, соответствующую номеру вопроса:',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    '11': '11',
    '1_faq_answer_text': '1. Сколько времени длится фотосессия?\n\n'
                    'У нас есть 3 временных слота, планируя время,\n'
                    'пожалуйста, учтите дополнительно 15 минут на инструктаж:\n\n'
                    '<b>25 минут = 2500 рублей</b>\n'
                    'Подойдет, если вы просто хотите попробовать этот формат съемки и точно знаете,\n'
                    'что хотите снять (запись на эту фотосессию возможна только на первое посещение).\n'
                    'До 4 человек, за последующего 500.\n\n'
                    '<b>45 минут = 5000 рублей</b>\n'
                    'Оптимально для 1-2 человек, этого времени хватит, чтобы освоиться и войти во вкус.\n'
                    'Один фон на ваш выбор. До 4 человек, за последующего 1000.\n'
                    'Комплимент от студии – кофе и чай с вкусняшками.\n\n'
                    '<b>90 минут = 8500 рублей</b>\n'
                    'Подойдет, если у вас много образов и идей или вы пришли с семьей или с друзьями. Два фона на ваш выбор.\n'
                    'До 4 человек, за последующего 1000. Также дополнительно можем предложить экспресс-макияж.\n'
                    'Комплимент от студии – кофе и чай с вкусняшками.\n'
                    'В студии будет комфортно небольшой компании до 10 человек.\n'
                    'Большее количество посетителей возможно, оно обговаривается заранее с администратором студии.',
    '2_faq_answer_text': '2. Можно ли сниматься в обуви?\n\n'
                         'В нашей студии можно сниматься в чистой сменной обуви.\n'
                         'Для этого надо проклеить подошву малярным скотчем\n'
                         '(это можно сделать заранее или в самой студии).\n\n'
                         'При съемке в обуви с темной или черной подошвой\n'
                         '(определение параметра цвета или оттенка закрепляется за администратором студии)\n'
                         'необходимо оставить залог в 2500 рублей.\n\n'
                         'Залог возвращается, если фон остался чистым\n'
                         '(чистоту фона определяет администратор студии).',
    '3_faq_answer_text': '3. Можно ли приносить или заказывать еду и напитки в студию?\n\n'
                         'Чтобы сохранить чистоту и порядок, пожалуйста, не приносите еду и напитки с собой.\n\n'
                         'Если вы все же хотите это сделать, предварительно согласуйте это с администратором студии.\n\n'
                         'Необходимо будет оставить залог в 2000 рублей.\n'
                         'Залог возвращается, если студия остается в чистом состоянии\n'
                         '(чистоту определяет администратор студии).',
    '4_faq_answer_text': '4. Можно ли приводить на фотосессию домашних животных?\n\n' 
                         'Оставьте, пожалуйста питомцев дома.\n'
                         'В нашей студии запрещено находиться с животными.',
    '5_faq_answer_text': '5. Как подготовиться к съемке?\n\n'
                         'Мы готовим для вас гайд, при записи на съемку вышлем его на электронную почту.\n\n'
                         'Дополнительно рекомендуем заранее продумать идею съемки, чтобы было легче воплощать самые крутые замыслы.\n'
                         'Мы всегда готовы поддержать вас.\n\n'
                         'Также вы можете принести свой реквизит, например, перчатки, головные уборы, костюмы, игрушки, очки и т.д.',
    '6_faq_answer_text': '6. Как перенести или отменить съемку?\n\n'
                         'Перенести съемку можно не позднее чем за 24 часа до назначенного времени, а отменить – за 72 часа.\n\n'
                         'Для этого вам нужно просто связаться с нами по доступным каналам, или просто позвонить 8-960-520-96-72\n\n'
                         'Возврат денежных средств при отмене бронирования до 48 часов - 100%.\n'
                         'При отмене за 24 часа – 50%\n'
                         'При отмене в день бронирования  - предоплата не возвращается.',
    '7_faq_answer_text': '7. Сколько фотографий я получу в результате?\n\n'
                         'Мы не ограничиваем наших гостей по количеству фотографий, и отдаем все фотографии в обработке.\n\n'
                         'Ведь даже из самых неудачных кадров – можно сделать крутое кадрирование деталей.\n\n'
                         'Ограничение только по времени, чем больше время съемки – тем больше фото. Мы отправляем вам все снимки. ',
    '8_faq_answer_text': '8. Кто может увидеть мои фотографии?\n\n'
                         'Никто, даже администратор не видит ваши фотографии. Фотосессия в нашей студии строго конфиденциальна.\n\n'
                         'Мы дорожим репутацией и выкладываем только тот контент, который разрешают нам гости студии.',
    '9_faq_answer_text': '9. Кто обрабатывает мои фотографии?\n\n'
                         'Ваши фотографии ретушируют несколько нейросетей, без участия человеческого глаза.\n'
                         'Весь процесс автоматизирован.',
    '10_faq_answer_text': '10. Как получить у вас консультацию по открытию студии автопортрета в своем городе?\n\n'
                          'Каждый месяц по России (и не только) мы помогаем людям открывать студии автопортретов.\n\n'
                          'Мы гордимся нашими клиентами, которые довели дело до конца и получили потрясающий результат!\n\n'
                          'У нас есть только одна консультация на город,\n'
                          'пишите в телеграм, может ваш город все еще доступен для этого бизнеса.',
    '11_faq_answer_text': '11. Что нельзя делать в студии?\n\n'
                          'Если вы опаздываете, то время не будет продлено на время опоздания,\n'
                          'мы всегда стараемся угодить нашим гостям, и если за вами следом не занято окошко, то постараемся добавить времени.\n\n'
                          'Нельзя находиться в студии в состоянии алкогольного или наркотического опьянения.\n'
                          'Администратор вправе не допускать в студию и удалять из студии за несоблюдение правила.\n\n'
                          'Нельзя использовать материалы, способные изменить облик фотостудии (мыльные пузыри, конфетти, перья, краски и т.п.).\n'
                          'Если ваша задумка требует использования чего-то подобного, то об этом нужно договориться заранее с администратором студии.\n'
                          'Штраф за невыполнение каждого из условий 3000 рублей.\n\n'
                          'Нельзя использовать огонь, а также горючие, взрывоопасные и токсичные вещества (свечи, бенгальские огни и т.п.).\n'
                          'Если вам необходимо зажечь свечки, то об этом нужно договориться заранее с администратором студии.\n'
                          'У нас запрещено курить электронные сигареты. Штраф за невыполнение каждого из условий 3000 рублей.\n'
                          'Мы соблюдаем технику безопасности.\n\n'
                          'Нельзя менять настройки оборудования, переставлять оборудование и самостоятельно устанавливать фоны.\n'
                          'Мы уже подготовили для вас профессиональный свет и настроили оборудование таким образом,\n'
                          'чтобы на выходе каждый гость получил качественную фотографию.\n'
                          'Штраф за невыполнение каждого из условий 3000 рублей.\n\n'
                          'Нельзя ходить по студии в грязной или уличной обуви. Мы предлагаем нашим гостям сменную обувь.\n'
                          'При нанесении фотостудии материального ущерба арендатор обязан возместить на месте стоимость ущерба.',
    'come_back_faq_list': 'Вернуться назад'
}