from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_keyboard(
    *btns: str,
    placeholder: str = None,
    request_contact: int = None,
    request_location: int = None,
    sizes: tuple[int] = (2,),
) -> ReplyKeyboardMarkup:
    """
    Создает reply клавиатуру с кнопками

    Args:
        *btns: Тексты кнопок
        placeholder: Подсказка в поле ввода
        request_contact: Индекс кнопки для запроса контакта
        request_location: Индекс кнопки для запроса местоположения
        sizes: Размеры строк (количество кнопок в каждой строке)

    Returns:
        ReplyKeyboardMarkup
    """
    keyboard = []
    current_row = []
    size_index = 0

    for index, text in enumerate(btns):
        if request_contact == index:
            current_row.append(KeyboardButton(text=text, request_contact=True))
        elif request_location == index:
            current_row.append(KeyboardButton(
                text=text, request_location=True))
        else:
            current_row.append(KeyboardButton(text=text))

        # Если текущая строка достигла нужного размера или это последняя кнопка
        if len(current_row) == sizes[size_index] or index == len(btns) - 1:
            keyboard.append(current_row)
            current_row = []
            if size_index < len(sizes) - 1:
                size_index += 1

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder=placeholder
    )
