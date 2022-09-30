user_name = input("Введите ваше имя: ")
user_surname = input("Введите вашу фамилию: ")
user_age = int(input("Введите год рождения: "))
user_city = input("Введите город проживания: ")
user_hobby = input("На что уделяете свободное время: ")
user_quiz = input("Выберите любую тему, которая вас интерисует (Машины, Кино, Программирование): ")

print("Обрабатываю информацию...")

if user_quiz == "Машины":
    questionsAvto1 = input("Какие ваши любиме марки автомобилей?: ")
    questionsAvto2 = input("Предпочитаете скорость или комфорт в машине?: ")
    questionsAvto3 = input("Дорого ли обходится обслуживание автомолиля?: ")

if user_quiz == "Кино":
    questionsKino1 = input("Любите смотреть фантастику: ")
    if questionsKino1 == "да":
        questionsKinoMVDC = input("Марвел или DC?: ")
        if questionsKinoMVDC == "Марвел":
            print("Тони Старк рулит :)")
        else:
            print("Зак Снайдер рулит :)")
    else: questionsKino2 = input("А какой предпочитаете жанр кино?: ")
    questionsKino3 = input("Мечтали сняться в нем?: ")

if user_quiz == "Программирование":
    questionsProg1 = int(input("Сколько языков программирования знаете или хотели бы знать?: "))
    questionsProg2 = input("Чем именно хотели или уже занимаетесь в области программирования?: ")
    questionsProg3 = input("Надеемся вы не умрете его изучать так, как я)))  (Нажмите Enter)")

print("Обработка информации...")

age = 2022 - user_age

print(" Имя: ", user_name,"\n",
      "Фамилия: ", user_surname,"\n",
      "Возраст: ", age,"\n",
      "Город: ", user_city,"\n",
      "Хобби: ", user_hobby)

if user_quiz == "Машины":
    if questionsAvto1 == "Зарубежные":
        if questionsAvto2 == "Скорость":
            print("Пользователь любит зарубежные спортивные автомобили.")
        else:
            print("Пользователь любит зарубежные автомобили класса кофморт.")
    else:
        if questionsAvto2 == "Скорость":
            print("Пользователь любит отечественные спортивные автомобили.")
        else:
            print("Пользователь любит отечественные автомобили класса кофморт.")

if user_quiz == "Кино":
    if questionsKino1 == "да":
        if questionsKinoMVDC == "Марвел":
            print("Пользователь обожает смотреть киновселенную Марвел.")
        else:
            print("Пользователь любит смотреть киновселенную DC.")
    else:
        print("Пользователь любит смотреть кино с жанром ", questionsKino2)

if user_quiz == "Программирование":
    print("Пользователь знает или хочет знать ", questionsProg1, " языков программирования. \n",
          "А также уже или планирует заниматься", questionsProg2)