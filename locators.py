# Ссылка Конструктор в хедере
app_header_constructor = ".//header[contains(@class, 'AppHeader_header__X9aJA')]//a[@class='AppHeader_header__link__3D_hX']"
# Лого в хедере
app_header_logo = ".//header[contains(@class, 'AppHeader_header__X9aJA')]//div[@class='AppHeader_header__logo__2D0X2']//a"
# Ссылка Входа/Личный кабинет в хедере
app_header_enter_link = ".//header[contains(@class, 'AppHeader_header__X9aJA')]//a[@href='/account']"

# Кнопка входа на главной странице
main_screen_enter_button = ".//button[text()='Войти в аккаунт']"
# Заголовок на главной странице
main_screen_title = ".//h1[text()='Соберите бургер']"
# Вкладка Булки на главной странице
main_screen_buns_tab = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Булки']/parent::div"
# Заголовок Булки на главной странице
main_screen_buns_title = ".//h2[text()='Булки']"
# Вкладка Соусы на главной странице
main_screen_sauces_tab = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Соусы']/parent::div"
# Заголовок Соусы на главной странице
main_screen_sauces_title = ".//h2[text()='Соусы']"
# Вкладка Начинки на главной странице
main_screen_fillings_tab = ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Начинки']/parent::div"
# Заголовок Начинки на главной странице
main_screen_fillings_title = ".//h2[text()='Начинки']"

# Заголовок на странице входа
login_screen_title = ".//h2[text()='Вход']"
# Ссылка регистрации на странице входа
login_screen_register_link_text = "Зарегистрироваться"
# Инпут имейла на странице входа
login_screen_email_input = ".//input[@name='name']"
# Заголовок пароля на странице входа
login_screen_password_input = ".//input[@name='Пароль']"
# Кнопка подтверждения на странице входа
login_screen_submit_button = ".//button[text()='Войти']"
# Ссылка восстановления пароля на странице входа
login_screen_forgot_password_link = ".//a[text()='Восстановить пароль']"

# Заголовок на странице регистрации
register_screen_title = ".//h2[text()='Регистрация']"
# Инпут имени на странице регистрации
register_screen_name_input = ".//label[text()='Имя']/following-sibling::input[@name='name']"
# Инпут имейла на странице регистрации
register_screen_email_input = ".//label[text()='Email']/following-sibling::input[@name='name']"
# Инпут пароля на странице регистрации
register_screen_password_input = ".//input[@name='Пароль']"
# Кнопка подтверждения на странице регистрации
register_screen_submit_button = ".//button[text()='Зарегистрироваться']"
# Ссылка входа на странице регистрации
register_screen_enter_link = ".//a[text()='Войти']"

# Заголовок на странице восстановления пароля
forgot_password_screen_title = ".//h2[text()='Восстановление пароля']"
# Ссылка входа на странице восстановления пароля
forgot_password_screen_enter_link = ".//a[text()='Войти']"

# Заголовок на странице профиля
user_screen_title = ".//a[text()='Профиль']"
# Кнопка выхода на странице профиля
user_screen_logout_button = ".//button[text()='Выход']"
