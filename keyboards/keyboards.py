from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

# yes | no keyboard
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Game keyboard
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
game_kb.row(button_1, button_2, button_3, width=3)
game_kb: ReplyKeyboardMarkup = game_kb.as_markup(
    resize_keyboard=True
)
