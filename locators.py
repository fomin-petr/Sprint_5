class StartPageLocators:
    LOGIN_BUTTON = '//button[ text()="Войти в аккаунт" ]' # кнопка 'Войти в аккаунт'
    PRIVATE_PAGE_BUTTON = '//p[ text()="Личный Кабинет" ]' # кнопка 'Личный кабинет'
    CREATE_ORDER_BUTTON = '//button[ text()="Оформить заказ"]' # кнопка 'Оформить заказ'
    CONSTRUCTOR_BUTTON = '//p[ contains(@class, "AppHeader") and text()="Конструктор" ]' # кнопка Конструктор
    LOGO_BUTTON = '//div[ contains(@class, "header__logo")]/a' #кнопка Логотип
    SAUCE_TAB = '//span[text()="Соусы"]/parent::div' #вкладка Соусы
    INGREDIENTS_TAB = '//span[text()="Начинки"]/parent::div' #вкладка Начинка
    BUN_TAB = '//span[text() = "Булки"] / parent::div' #вкладка Булочка


class LoginPageLocators:
    EMAIL_INPUT_FIELD = '//input[ contains(@type, "text") ]' # поле ввода Email
    PASSWORD_INPUT_FIELD = '//input[ contains(@type, "password") ]' # поле ввода пароля
    REGISTRATION_BUTTON = '//a[ text() = "Зарегистрироваться" ]' # Кнопка Зарегистрироваться
    LOGIN_BUTTON = '//button[ text() = "Войти" ]'  # Кнопка Зарегистрироваться
    FORGOT_PASSWORD_BUTTON = '//a[ contains(@href, "/forgot-password") ]' # кнопка Восстановить пароль


class RegistrationPageLocators:
    NAME_INPUT_FIELD = '//label[ text()="Имя" ]/parent::div/input' # Поле ввода Имя
    EMAIL_INPUT_FIELD = '//label[ text()="Email" ]/parent::div/input' # Поле ввода Email
    PASSWORD_INPUT_FIELD = '//label[ text()="Пароль" ]/parent::div/input' # Поле ввода Пароля
    REGISTRATION_BUTTON = '//button[ text()="Зарегистрироваться" ]' # кнопка регистриации
    LOGIN_BUTTON = '//a[ contains(@href, "/login") ]' # кнопка Войти
    ERROR_MESSAGE = '//p[ contains(@class, "input__error")]'


class PrivatePageLocators:
    NAME_FIELD = '//label[ text()="Имя"]/parent::div/input' # поле Имя
    LOGIN_FIELD = '//label[ text()="Логин"]/parent::div/input' # поле Логин
    EXIT_BUTTON = '//button[ text()="Выход"]' # кнопка Выйти


class ForgotPasswordPageLocators:
    LOGIN_BUTTON = '//a[ contains(@href, "/login") ]' # кнопка Войти
