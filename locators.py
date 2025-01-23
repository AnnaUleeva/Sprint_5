from selenium.webdriver.common.by import By

class Locators:
    # Ссылка Конструктор в хедере
    app_header_constructor = (By.XPATH, ".//header[contains(@class, 'AppHeader_header__X9aJA')]//a[@class='AppHeader_header__link__3D_hX']")
    # Лого в хедере
    app_header_logo = (By.XPATH, ".//header[contains(@class, 'AppHeader_header__X9aJA')]//div[@class='AppHeader_header__logo__2D0X2']//a")
    # Ссылка Входа/Личный кабинет в хедере
    app_header_enter_link = (By.XPATH, ".//header[contains(@class, 'AppHeader_header__X9aJA')]//a[@href='/account']")

    # Кнопка входа на главной странице
    main_screen_enter_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Кнопка оформления заказа на главной странице
    main_screen_checkout_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Заголовок на главной странице
    main_screen_title = (By.XPATH, ".//h1[text()='Соберите бургер']")
    # Вкладка Булки на главной странице
    main_screen_buns_tab = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Булки']")
    # Заголовок Булки на главной странице
    main_screen_buns_title = (By.XPATH, ".//h2[text()='Булки']")
    # Вкладка Соусы на главной странице
    main_screen_sauces_tab = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Соусы']")
    # Заголовок Соусы на главной странице
    main_screen_sauces_title = (By.XPATH, ".//h2[text()='Соусы']")
    # Вкладка Начинки на главной странице
    main_screen_fillings_tab = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Начинки']")
    # Заголовок Начинки на главной странице
    main_screen_fillings_title = (By.XPATH, ".//h2[text()='Начинки']")

    # Заголовок на странице входа
    login_screen_title = (By.XPATH, ".//h2[text()='Вход']")
    # Инпут имейла на странице входа
    login_screen_email_input = (By.XPATH, ".//input[@name='name']")
    # Заголовок пароля на странице входа
    login_screen_password_input = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка подтверждения на странице входа
    login_screen_submit_button = (By.XPATH, ".//button[text()='Войти']")

    # Инпут имени на странице регистрации
    register_screen_name_input = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@name='name']")
    # Инпут имейла на странице регистрации
    register_screen_email_input = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@name='name']")
    # Инпут пароля на странице регистрации
    register_screen_password_input = (By.XPATH, ".//input[@name='Пароль']")
    # Ошибка инпута пароля на странице регистрации
    register_screen_password_input_error = (By.XPATH, ".//input[@name='Пароль']/parent::*/following-sibling::p[contains(@class, 'input__error')]")
    # Кнопка подтверждения на странице регистрации
    register_screen_submit_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Ссылка входа на странице регистрации
    register_screen_enter_link = (By.XPATH, ".//a[text()='Войти']")

    # Ссылка входа на странице восстановления пароля
    forgot_password_screen_enter_link = (By.XPATH, ".//a[text()='Войти']")

    # Заголовок на странице профиля
    user_screen_title = (By.XPATH, ".//a[text()='Профиль']")
    # Кнопка выхода на странице профиля
    user_screen_logout_button = (By.XPATH, ".//button[text()='Выход']")
