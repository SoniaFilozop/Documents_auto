from docxtpl import DocxTemplate
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


class Sovetskiy:
    def __init__(self, ul):
        self.rayon = 'Советском'

    def get_rayon(self):
        return self.rayon


class Sovuch1S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = ['Генерала Перхоровича', 'Дорожная', 'Краснодонская', 'Юлюса Янониса']
        self.per = []
        self.pr = ['Поселок Придонской']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch2S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = ['Домостроителей', 'Бульвар Пионеров',
                   'Космонавтов']
        self.per = ['Бригадный', 'Дозорный', 'Попутный', 'Производственный', 'Уютный', 'Чистый']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch3S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['Волнистая', 'Бородина', 'Пешестрелецкая',
                   'Холмистая',
                   'Семилукская']
        self.per = ['Автоматчиков', 'Газовый', 'Газопроводный']
        self.pr = ['Село Подклетное']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            if self.u in self.ul or self.u in self.per:
                return True
            return False


class Sovuch4S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['Молодогвардейцев', 'Олеко Дундича', 'Поселковая', 'Песчаная']
        self.per = ['Поселковый, Песчаный']
        self.pr = ['Поселок Шилово']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num, number):
        if num in self.pr:
            self.ul = ['Братьев Петровых', 'Вяземская', 'Генерала Платонова', 'Генерала Раевского', 'Генерала Халютина',
                       'Дубравная', 'Бульвар Воинской Славы', 'Генерала Шатилова', 'Долинная', 'Инженерная',
                       'Курчатова',
                       'Лазарева', 'Леонида Утесова',
                       'Малышевская', 'Междуреченская', 'Обнинская', 'Пойменная', 'Привольная', 'Розовая', 'Рубежная',
                       'Сусанинская', 'Теплоэнергетиков', 'Хохольская']
            self.per = ['Капитана Мягкова', 'Полковника Старкова']
            self.prochee = ['Фрунзе', 'в/ч 32891', 'в/ч 51025']
            if self.u in self.ul and number == 1:
                return True
            elif self.u in self.per and number == 2:
                return True
            elif self.u in self.prochee and number == 3:
                return True
            else:
                return False
        else:
            if self.u in self.ul or self.u in self.per or self.u:
                return True


class Sovuch5S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Героев Сибиряков', 'Крымская', 'Жигулевская']
        self.per = []
        self.pr = ['Село Малышево', 'Поселок 1 Мая']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            if self.u in self.ul or self.u in self.per:
                return True
            else:
                return False


class Sovuch6S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '6'
        self.ul = ['Богачева', 'Краснозвездная', 'Путиловская', 'Чеботарева', 'Проспект Патриотов',
                   'Бульвар Фестивальный']
        self.per = ['Дружный', 'Жигулевский']
        self.pr = ['Поселок Шилово', 'Шиловский массив', 'Пост ДПС ГИБДД на 214 км автодороги Курск - Саратов',
                   'Поселок Западный']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            if num == 'Поселок Шилово':
                self.ul = ['Буданцева', 'Ключникова',
                           'Полковника Богомолова', 'Шибилкина']
                if self.u in self.ul:
                    return True
            else:
                return True
        else:
            if self.u in self.ul:
                return True
            return False


class Sovuch7S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '7'
        self.ul = [
            'Антокольского', 'Изобретателей', 'Писателя Маршака',
            'Конструкторов',
            'Магнитогорская', 'Малявина', 'Меркулова',
            'Нестерова', 'Шендрикова']
        self.per = ['Ани Скоробогатько', 'Антокольского', 'Архипова', 'Дьякова', 'И.Земнухова', 'Любы Шевцовой',
                    'Магнитогорский', 'Мухиной', 'Нестерова', 'Путиловский', 'Сергея Тюленина', 'Смирнова',
                    'Ульяны Громовой']
        self.pr = ['Поселок Тенистый', "Ветеран",
                   'Лазурит Тепличный',
                   'Придонье',
                   'Радуга',
                   'Тихий Дон',
                   'Тихий Дон-2',
                   'Тихий Дон-3',
                   'Тихий Дон-4']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch8S(Sovetskiy):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '8'
        self.ul = [
            'Любы Шевцовой', 'Пешеходная', 'Урожайная',
            'Депутатская', 'Космонавта Комарова', 'Олега Кошевого', 'Якира', 'Южно-Моравская']
        self.per = []
        self.pr = ['Поселок Подпольный']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Zheleznodorozhny:
    def __init__(self, ul):
        self.rayon = 'Железнодорожном'

    def get_rayon(self):
        return self.rayon


class Sovuch1Z(Zheleznodorozhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = ['19 Стрелковой дивизии', '19 Стрелковой Дивизии', '19-й Стрелковой Дивизии',
                   '19-й Стрелковой дивизии', '25 Января', '25-го Января', 'Артёма', 'Барбюса', 'Береговая',
                   'Белгородская', 'Беломорская', 'Богатырская', 'Богучарская', 'Боровская', 'Братская', 'Вагонная',
                   'Венская', 'Восточная', 'Гоголевская', 'Деповская', 'Диспетчерская', 'Добрый Путь',
                   'Калининградская',
                   'Колхозный Путь', 'Коммунальная', 'Красина', 'Кубанская', 'Кузнечная', 'Куйбышева', 'К. Цеткин',
                   'Лермонтова', 'Листопадная', 'Литейная', 'Локомотивная', 'Луговая', 'Малиновского', 'Машинистов',
                   'Механическая', 'Молодежная', 'Моховая', 'Нариманова', 'Новая', 'Новый быт', 'Панфилова',
                   'Паровозная',
                   'Пионерская', 'Планетная', 'Пугачева', 'Р. Люксембург', 'Санникова', 'Северная', 'Сенная',
                   'Солидарности', 'Столярная', 'С. Халтурина', 'Салтыкова-Щедрина', 'Тепловозная', 'Токарная',
                   'Тургенева',
                   'Черноморская', 'Электровозная', 'Юности', 'Южная', 'Серафимовича']
        self.per = ['Артёма', 'Береговой', 'Гоголя', 'Деповский', 'Диспетчерский', 'Еловый', 'Инютинский',
                    'Колхозный', 'Кольцевой', 'Малярный', 'Молодежный', 'Нариманова', 'Пионерский', 'Прибрежный',
                    'Солнечный', 'Сретенский', 'Червонный', 'Проезд Богучарский', 'Серафимовича']
        self.pr = ['Тупик Деповский']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch2Z(Zheleznodorozhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = ['Артамонова', 'Гаршина', 'Добролюбова', 'Запорожская']
        self.per = ['Добролюбова', 'Запорожский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch3Z(Zheleznodorozhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['Архитектора Троицкого', 'Богдана Хмельницкого', 'Изыскателей', 'Лизы Чайкиной', 'Троицкого',
                   'Б.Хмельницкого', 'Б. Хмельницкого', 'Л.Чайкиной', 'Суворова']
        self.per = ['Богдана Хмельницкого', 'Проезд Рационализаторов', 'Суворовский']
        self.pr = ['Боровской', 'Ближний Бор', 'Веселый', 'Дальний Бор', 'Кожевенный',
                   'Нижний', 'Маяки', 'Усманский', 'Пески', 'нп. Госзаповедник', 'Поселок Боровое', 'Поселок Водокачка',
                   'Поселок Краснолесный', 'Поселок Репное']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch4Z(Zheleznodorozhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['Одинцова', 'Переверткина']
        self.per = ['Поселковый', 'Песчаный']
        self.pr = ['Поселок Сомово', 'Поселок Полыновка']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch5Z(Zheleznodorozhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Багратиона', 'Весенняя', 'Витрука', 'Гончаровская', 'Грибоедова', 'З. Космодемьянской',
                   'Зои Космодемьянской', 'Землячки',
                   'Зубрилова', 'Жуковского', 'Измайловская', 'Комсомольская', 'Котовского',
                   'Краснофлотская', 'Красная Поляна', 'Куликовская',
                   'Набережная', 'Нахимовская', 'Остужева', 'Перекопская',
                   'Полтавская', 'Севастопольская', 'Спартаковская', 'Урывского',
                   'Филатова', 'Фурмановская', 'Грибоедова', 'Тракторная', 'Ушакова', 'Рокоссовского']
        self.per = ['Альпийский', 'Гранитный', 'Доблести', 'З. Космодемьянской', 'Измайловский', 'Колхозный',
                    'Корниловский', 'Морской', 'Международный', 'Нахимовский', 'Полтавский', 'Севастопольский',
                    'Флотский']
        self.pr = ['ПМС 81', 'Путевая машинная станция N 81']

        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Kominternovsky:
    def __init__(self, ul):
        self.rayon = 'Коминтерновском'

    def get_rayon(self):
        return self.rayon


class Sovuch1K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = ['Академика Басова', 'Болховитинова', 'Веселая', 'Гайдара',
                   'Дачный поселок', 'Донская', 'Жемчужная', 'Загородная', 'Леваневского', 'Маршала Жукова', 'Павлова',
                   'Покровская', 'Просвещения', 'Победы', 'Республиканская', 'Ракитинская', 'Славы', 'Тульская',
                   'Чернышова']
        self.per = ['8 Марта', 'Александровский', 'Березки', 'Вокзальный', 'Зеленый', 'Исполкомовский', 'Ленина',
                    'Радиозаводской', 'Свердлова']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        return False


class Sovuch2K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = ['5-й танковой армии', 'Актрисы Рощиной', 'Беспаловой',
                   'Историка Веселовского', 'Веселовского', 'Краеведа Зверевой', 'Маршала Катукова', 'Зверевой',
                   ' Катукова', 'Нагорная', 'Подгоренская',
                   'Радиозаводская', 'Танковая', 'Шолохова']
        self.per = ['Бабушкина', 'Веселый', 'Колодезный', 'Коминтерновский', 'Политехнический', 'Полковой', 'Полынный',
                    'Свободы']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch3K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['Абызова', 'Айдаровская', 'Беговая', 'Алексея Геращенко', 'Дмитрия Горина', 'Дружинников',
                   'Ипподромная', 'Карпинского', 'Красных Зорь', 'Независимости', 'Очаковская', 'Преображенская',
                   'Троепольского', 'Чкалова', 'Фруктовая', 'Электросигнальная']
        self.per = ['Калинина', 'Пугачева', 'Самойловский', 'Ученический']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch4K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['Бульвар Победы', 'Архитектора Быховского', 'Архитектурная', 'Березовская', 'Багрицкого',
                   'Екатерины Зеленко', 'Малаховского', 'Остроухова', 'Серафима Саровского', 'Товарищеская']
        self.per = ['Дачный', 'Камышовый', 'Ясный проезд', 'Ясный Проезд', 'Партизанский', 'Пейзажный', 'Правды',
                    'Студеный']
        self.pr = ['Бульвар Победы']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch5K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Вокзальная', 'Гжельская', 'Головина', 'Дружеская',
                   'Ивана Туркенича', 'Курортная', 'Керамическая',
                   'Солнечная',
                   'Урицкого', 'Утренняя', 'Школьная']
        self.per = ['Анненский', 'Валуйский', 'Вольный', 'Грибановский', 'Дружеский', 'Красно-Лимановский',
                    'Краснолиманский', 'Станичный']
        self.pr = ['Территория Аэропорт']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch6K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '6'
        self.ul = ['Ведугская', 'Героев Бреста', 'Лебедянская', 'Миронова', 'Скляевой', 'Связистов', 'Сочинская']
        self.per = ['Елочный', 'Осинки', 'Прохоровский', 'Республиканский', 'Федеративный']
        self.pr = ['Жилой массия Ясенки']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch7K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '7'
        self.ul = ['45 Стрел.Дивизии', '45 Стрелковой Дивизии', '45-й Стрелковой Дивизии', '45 Стрелковой дивизии',
                   '45-й Стрелковой дивизии', '45-щй Стрелковой Дивизии', '45-ой Стрелковой дивизии', 'Елецкая',
                   'Историка Костомарова' 'Кораблинова', 'Криворучко', 'Терешковой', 'Художника Лихачева',
                   'Художника Пономарева',
                   'Пономарева']
        self.per = ['Автогенный', 'Верещагина', 'Гагарина', 'Дроздовый', 'Коллективный', 'Лискинский',
                    'Приветливый',
                    'Путейский Городок']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch8K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '8'
        self.ul = ['Проспект Труда', 'Пр.Труда',
                   '1 Мая',
                   'Верещагина', 'Вольная', 'Десантников', 'Землянская', 'Задонская', 'Композитора Ставонина',
                   'Минеров', 'Мордасовой', 'Новгородская', 'Овражная', 'Питомник', 'Правды', 'Свердлова',
                   'Социалистическая', 'Шукшина']
        self.per = ['Заветный', 'Загорский', 'Закатный', 'Здоровья', 'Клинический', 'Новоселов', 'Осетровский',
                    'Спокойный', 'Станкостроительный', 'Ракетный']
        self.pr = ['Жилой массив Задонье', 'Площадь Советов']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch9K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '9'
        self.ul = ['303 Стрелковой Дивизии', '60 Армии', '303 Стрелковой дивизии', '60-й Армии',
                   '303-й Стрелковой Дивизии', '60-ой Армии', 'Антонова-Овсеенко', 'Апраксина', 'Брянская', 'Ватутина',
                   'Генерала Ефремова', 'Княжеская', 'Лидии Рябцевой',
                   'Поэта Прасолова', 'Рязанская', 'Строителей', 'Тамбовская', 'Федора Сушкова', 'Фрегатная']
        self.per = ['Настасьинский', 'Брянский проезд', 'Брянский Проезд', 'Октябрьский', 'Подклетенский', 'Рамонский',
                    'Солнечный',
                    'Школьный', 'Ямской']
        self.pr = ['Жилой массив Хвойный']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch10K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '10'
        self.ul = ['Багряная', 'Братьев Мариных', 'Веневитинская', 'Любимая',
                   'Окружная', 'Строительная', 'Торпедо', 'Текстильщиков', 'Чудесная']
        self.per = ['Дальний', 'Космонавтов', 'Надежды', 'Озерный', 'Хреновской']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        return False


class Sovuch11K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '11'
        self.ul = ['65 лет Победы', 'Академика Королева', 'Варейкиса', 'Еремеева',
                   'Киевская', 'Крайняя', 'Курская', 'Маршала Голикова', 'Народная', 'Подклетенская', 'Церковная']
        self.per = ['Мечникова', 'Славы', 'Сливовый', 'Транспортный', 'Чесменский']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        return False


class Sovuch12K(Kominternovsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '12'
        self.ul = ['60 лет ВЛКСМ', 'Лесхозная',
                   'Новый поселок', 'Олифиренко']
        self.per = ['Ботанический', 'Снежный']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        return False


class Levoberezhny:
    def __init__(self, ul):
        self.rayon = 'Левобережном'

    def get_rayon(self):
        return self.rayon


class Sovuch1Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = ['Азовская', 'Волжская', 'Донецкая', 'Костромская', 'Летчика Небольсина', 'Новороссийская',
                   'Просторная', 'Рижская', 'Ржевская', 'Чебышева', 'Шубина']
        self.per = ['Новороссийский', 'Прохладный', 'Ростовский', 'Цимлянский']
        self.pr = ['Воронежсинтезкаучук ', 'Поселок Алексеевка', 'Южная подстанция']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch2Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = ['Глинки', 'Дубровина', 'Корольковой']
        self.per = []
        self.pr = ['Совхоз Никольский', 'Поселок Буденный', 'Поселок Масловка', 'Поселок Подклетный', 'Село Никольское',
                   'Семилукские Выселки', 'Село Таврово', 'Воронежский гидроузел']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch3Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['Балашовская', 'Барнаульская', 'Варшавская',
                   'Венецианова', 'Волгодонская', 'Волкова', 'Вологодская', 'Воронихина', 'Вьетнамская', 'Дружбы',
                   'Заслонова', 'Ковалевской', 'Корейская', 'Кронштадтская', 'Ленская', 'Макаренко', 'Мечникова',
                   'Новикова', 'Нововоронежская', 'Пекинская', 'Печерская',
                   'Путилина', 'Саврасова', 'Третьякова', 'Цимлянская', 'Читинская',
                   'Шахтинская', 'Шинников']
        self.per = ['Баженова', 'Балашовский', 'Заслонова', 'Ковыльный', 'Химический', 'Шубина']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch4Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['Беляевой', 'Героев Стратосферы', 'Кулибина', 'Лебедева', 'Левитана',
                   'Лихачева', 'Менделеева', 'Меркулова', 'Полины Осипенко',
                   'Осоавиахимовская', 'Сеченова', 'Танеева', 'Тельмана', 'Ярославская']
        self.per = ['Русанова', 'Сеченова', 'Тельмана']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch5Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Арзамасская',
                   'Круглая', 'МОПРА', 'Нижняя', 'Порт-Артурская', 'Набережная Спортивная', 'Тихая', 'Щорса']
        self.per = ['Арзамасский', 'Гвардейский', 'Заречный', 'Кавказский', 'Казанский', 'Мостостроителей', 'Ольховый',
                    'Парашютистов', 'Планерный', 'Сквозной', 'Сторожевой']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch6Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '6'
        self.ul = ['Брусилова',
                   'Веры Засулич', 'Красногвардейская', 'Огарева',
                   'Озерная', 'Саперная', 'Серова']
        self.per = ['Бобровский', 'Гражданский', 'Крамского', 'Международный', 'Набережный', 'Ольховатский',
                    'Поленова' 'Репина', 'Усманский', 'Хоперский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch7Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '7'
        self.ul = ['17 Сентября', '17-го Сентября', 'Витебская', 'Волгоградская', 'Героев Хасана', 'Гомельская',
                   'Дальневосточная',
                   'Ивановская', 'Калачеевская', 'Клинская', 'Новохоперская',
                   'Обручева', 'Окружная', 'Тверская', 'Туполева', 'Уточкина']
        self.per = ['Бродского', 'Брусилова', 'Витебский', 'Волочаевский', 'Димитрова', 'Ивановский',
                    'Путевой', 'Россошанский', 'Таловский',
                    'Томский', 'Уточкина', 'Чаплыгина', 'Челябинский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch8Lv(Levoberezhny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '8'
        self.ul = ['Адмирала Чурсина', 'Айвазовского', 'Алданская', 'Базовая', 'Баррикадная', 'Владимира Высоцкого',
                   'Гаражный тупик', 'Ермака', 'Ильюшина', 'Иркутская', 'Красного Октября', 'Омская', 'Писарева',
                   'Ползунова', 'Славянская', 'Уральская', 'Циолковского', 'Шидловского', 'Черепанова', 'Черниговская']
        self.per = ['Монтажный', 'Отличников']
        self.pr = ['Монтажный', 'Придача', 'СМП N 808', 'СМП N 863', 'Озерки']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Leninsky:
    def __init__(self, ul):
        self.rayon = 'Ленинском'

    def get_rayon(self):
        return self.rayon


class Sovuch1Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = [
            '40-Летия Октября', 'Бакунина',
            'Девицкий выезд',
            'Пограничная', 'Промышленная',
            'Профсоюзная', 'Радищева']
        self.per = ['Бакунинский', 'Кабельный', 'Мало - Московский', 'Маломосковский', 'Слесарный', 'Специалистов',
                    'Электронный']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        return False


class Sovuch2Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = [
            'Белинского', 'Бестужева',
            'Большая Стрелецкая',
            'Гора Металлистов', 'Кирова',
            'Коперника',
            'Красных Партизан', 'Крупской',
            'Льва Толстого', 'Мало-Стрелецкая', 'Молострелецкая', 'Нарвская',
            'Петра Сазонова',
            'Платонова', 'Ремесленная Гора',
            'Севастьяновский съезд', 'Серго',
            'Фрунзе',
            'Шевченко']
        self.per = ['Белинского', 'Бестужева', 'Свечной', 'Муравьева', 'Корабельный', 'Красных Партизан',
                    'Печатников',
                    'Рабкоровский', 'Сазонова', 'Севастьяновский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch3Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['20-Летия Октября',
                   'Артековская', 'Бетховена',
                   'Волоколамская',
                   'Державина',
                   'Донбасская', 'Карамзина',
                   'Красная Горка', 'Красноярская',
                   'Кубанская Гора', 'Лескова', 'Майкова', 'Марата', 'Народных Ополченцев',
                   'Песчаная Гора', 'Свободная', 'Скрибиса', 'Саратовская', 'Станкевича',
                   'Челюскинцев', 'Чернышевский бугор', 'Черновицкая']
        self.per = ['Алтайский', 'Ангарский', 'Веры Фигнер', 'Городской', 'Жасминный', 'Заозерный',
                    'Карпатский', 'Лескова', 'Марата', 'Мурманский', 'Нансена', 'Невский',
                    'Поворотный', 'Полярный', 'Свободный', 'Снайперский', 'Цветной', 'Челюскинцев']
        self.pr = ['Маяковского', 'Балтийский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch4Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['100 Стрелковой Дивизии', '100-й Стрелковой Дивизии', '100-ой Стрелковой Дивизии',
                   '100-й Стрелковой дивизии', '100-ой Стрелковой дивизии', '100 Стрелковой дивизии', 'Аксакова',
                   'Возрождения', 'Верхняя', 'Грамши', 'Дзотова',
                   'Звенигородская', 'Курганская',
                   'Лишенко',
                   'Маленькая', 'Маяковского', 'Направника', 'Общественная',
                   'Профессора Харина', 'Харина', 'Римского-Корсакова', 'Серпуховская',
                   'Солодовникова', 'Средняя', 'Степана Панкова', 'Тушинская', 'Ульяновская',
                   'Уфимская', 'Уфимский тупик', 'Чижовская']
        self.per = ['Аксакова', 'Байкальский', 'Виноградова', 'Вишневый', 'Возрождения', 'Грамши', 'Даргомыжского',
                    'Керченский', 'Кирпичный', 'Коллективизации', 'Ленский', 'Можайский', 'Симферопольский',
                    'Сивашский', 'Солодовникова', 'Чапаева', 'Черкасский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch5Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Артиллерийская',
                   'Выборгская',
                   'Демьянова', 'Енисеевская', 'Енисеевский бугор',
                   'Злобина', 'Конноармейская',
                   'Конно-Стрелецкая', 'Кропоткина',
                   'Молдавская', 'Маршала Неделина',
                   'Малокрасноармейская', 'Пестеля',
                   'Набережная Петровская',
                   'Пушкарская',
                   'Сергея Лазо', 'Танкистов',
                   'Черняховского', 'Щербакова']
        self.per = ['Амурский', 'Благодатный', 'Бессарабский', 'Карельский', 'Казарменный', 'Краснознамённый',
                    'Кедровый', 'Кишиневский', 'Конноармейский',
                    'Люлина', 'Конно-Стрелецкий', 'Коннострелецкий', 'Минина', 'Молдавский',
                    'Малокрасноармейский', 'Ново-Слободский', 'Новослободский', 'Новый', 'Ореховый', 'Пушкарский',
                    'Пестеля',
                    'Пожарского', 'Пролетарский', 'Раздольный', 'Танкистов', 'Штурмовой']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch6Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '6'
        self.ul = ['121 Стрелковой Дивизии', '121 Стрелковой дивизии', '121-й Стрелковой Дивизии',
                   '121-й Стрелковой дивизии', '121-ой Стрелковой дивизии', '121-ой Стрелковой Дивизии',
                   'Андреева',
                   'Волнухина', 'Врубеля', 'Газетчиков',
                   'Голубиный тупик',
                   'Гремяченская', 'Журналистов', 'Калужская', 'Камская',
                   'Ладожская', 'Ладожский проезд',
                   'Новаторов',
                   'Новогодняя', 'Орловская',
                   'Острогожский проезд',
                   'Охотничий тупик',
                   'Праздничная', 'проезд Яблочный', 'Рабочий тупик', 'Рыбачий тупик',
                   'Соколиный тупик', 'Туркменский проезд', 'Ударная',
                   'Херсонская', 'Маршала Шапошникова', 'Шиловская',
                   'Энтузиастов']
        self.per = ['30-Летия Октября', 'Астраханский', 'Госпитальный', 'Грибной', 'Журналистов', 'Короткий',
                    'Кривошеина', 'Кленовый', 'Каштановый', 'Корпусный', 'Кривоколенный', 'Камский', 'Летний',
                    'Лиственный', 'Летчиков', 'Лучевой', 'Малый', 'Одесский', 'Орловский',
                    'Острогожский', 'Прямой', 'Рябиновый', 'Стрелковый', 'Соколиный',
                    'Хвойный', 'Херсонский', 'Ялтинский', 'Яблочный']
        self.pr = ['30-Летия Октября', 'Иртышский', 'Летний', 'Ялтинский', 'Малый']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch7Ln(Leninsky):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '7'
        self.ul = ['Астраханская', 'Базарная Гора', 'Бархатный Бугор', 'Броневая', 'Есенина',
                   'Красноармейская',
                   'Некрасова',
                   'Одесская',
                   '30-Летия Октября', '30-летия Октября']
        self.per = ['Бакинский', 'Балтийский', 'Днепровский', 'K.Булавина', 'Красноармейский', 'Передовой', 'Старинный']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Сentralny:
    def __init__(self, ul):
        self.rayon = 'Центральном'

    def get_rayon(self):
        return self.rayon


class Sovuch1Cn(Сentralny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '1'
        self.ul = ['Академика Конопатова', 'Конопатова', 'Берёзовая Роща', 'Бунакова', 'Бурденко', 'Гастелло',
                   'Дарвина', 'Докучаева',
                   'Дуговая', 'Железноводская', 'Казакова', 'Калинина', 'Келлера', 'Кисловодская',
                   'Кисловодский проезд', 'Красной Работницы', 'Красовского', 'Ленина', 'Лесной поселок',
                   'Лобачевского', 'Ломоносова', 'Набережная Максима Горького', 'Мичурина', 'Морозова',
                   'Октябрьской Революции', 'Поспеева', 'Прянишникова',
                   'Пятигорская', 'Рабочего класса',
                   'Рылеева', 'Серебрякова', 'Советская', 'Студенческая дом N 17', 'Тимирязева', 'Ушинского',
                   'Фронтовая', 'Цветущая', 'Швейников']
        self.per = ['Бауманский', 'Дуговой', 'Ессентуки', 'Курортный', 'Лесной', 'Лесокультурный', 'Лечебный',
                    'Опытный', 'Проходной', 'Советский', 'Спортивный', 'Учебный']
        self.pr = ['Санаторий им. Горького', 'Лесная поляна', 'Ботанический сад', 'Учебный кордон', 'Рыбачье', 'Ветряк',
                   'Олимпик']
        super().__init__(ul)

    def get(self):
        return self.sovuch

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get_pr(self, num):
        if num in self.pr:
            return True
        else:
            return False


class Sovuch2Cn(Сentralny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '2'
        self.ul = ['Площадь Университетская', 'Университетская Площадь', 'Университетская площадь',
                   'Бульвар Олимпийский', 'Олимпийский бульвар', 'Олимпийский Бульвар', '20-Летия ВЛКСМ', '25 Октября',
                   '20-летия ВЛКСМ', '25-го Октября',
                   'Авиационная', 'Алексеевского', 'Белинского',
                   'Бехтерева',
                   'Василия Пескова',
                   'Герцена', 'Декабристов',
                   'Детей', 'Дзержинского', 'Загоровского', 'Кардашова', 'Кости Стрелюка', 'К.Стрелюка',
                   'Левая Суконовка',
                   'Петра Алексеева', 'Первомайская',
                   'Правая Суконовка', 'Помяловского',
                   'Сакко и Ванцетти', 'Театральная', 'Чернышевского']
        self.per = ['Бехтерева', 'Горный', 'Детский', 'Мордовцева', 'Рабфаковский', 'Скорняжный',
                    'Старомосковский',
                    'Тимуровцев']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch3Cn(Сentralny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '3'
        self.ul = ['Академика Першина', 'Бовкуна', 'Бунина', 'Вавилова', 'Героев Красной Армии', 'Горького',
                   'Кавалерийская',
                   'Коммунаров', 'Короленко', 'Красненькая', 'Крестьянская', 'Крутая', 'Марии Копыловой', 'Линейная',
                   'Логвиновская', 'Луначарского', 'Пятницкого', 'Сиреневая',
                   'Софьи Перовской', 'Таранченко']
        self.per = ['Академика Гмелина']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        return False


class Sovuch4Cn(Сentralny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '4'
        self.ul = ['Генерала Черняховского',
                   'Городовикова', 'Желябова',
                   'Козо-Полянского',
                   'Мира', 'Нарядная',
                   'Обороны Революции', 'Полевая',
                   'Ср.Московская', 'Среднемосковская', 'Средне-Московская', 'Студенческая',
                   'Феоктистова', 'Чайковского', 'Юных Натуралистов',
                   'Коммунистической молодежи.']
        self.per = ['Героев Революции', 'Индустриальный', 'Купянский', 'Мельничный', 'Оранжерейный', 'Отрадный',
                    'Разведчиков', 'Учительский']
        self.pr = ['Жилой массив Олимпийский']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


class Sovuch5Cn(Сentralny):
    def __init__(self, ul):
        self.u = ul
        self.sovuch = '5'
        self.ul = ['Арсенальная', 'Батуринская',
                   'Большая Манежная', 'Большая Чернавская', 'Бучкури', 'Вайцеховского',
                   '8 Марта', 'Героев Революции', 'Героев Труда', 'Демократии', 'Дзиньковского', 'Достоевского',
                   'Дурова', 'Жилина', 'Замкина', 'Каляева',
                   'Комиссаржевской',
                   'Летчика Филипова', 'Малая Манежная', 'Мало-Смоленская', 'Мало-Терновая', 'Набережная Массалитинова',
                   'Ольминского', 'Освобождения Труда', 'Пролетарская',
                   'Пролетарской Диктатуры', 'Смоленская', 'Ст.Разина', 'Трудовая', 'Целинная', 'Цюрупы', 'Эртеля']
        self.per = ['Пряничный', 'Солдатский', 'Фабричный', 'Целинный', 'Эртеля']
        self.pr = ['Рабочий городок']
        super().__init__(ul)

    def get_sovuch(self, number):
        if self.u in self.ul and number == 1:
            return True
        elif self.u in self.per and number == 2:
            return True
        else:
            return False

    def get(self):
        return self.sovuch

    def get_pr(self, num):
        if num in self.pr:
            return self.sovuch
        else:
            return False


def main():
    x = ''
    dom = ''
    num = 0
    family = ''
    print('Есть ли в адресе указания на административные единицы(поселок, село, в/ч, ДНТ, СНТ, Жилой массив)?')
    print('Да - нажмите "1"')
    print('Нет - нажмите "Enter"')
    v = input()
    if v == '1':
        family = ''
        index = ''
        rayon = ''
        site = ''
        print('Введите наименование')
        print('Например: "Послелок Шилово", "Шиловский массив"; либо название СНТ или ДНТ без абревиатуры "СНТ", "ДНТ"')
        num = input()
        ul = ''
        if num == 'Поселок Шилово':
            print('Введите название улицы или переулка или чего-то другого')
            ul = input()
            print(
                'Если это улица, проспект, проезд, набережная или бульвар, нажмите "1", если переулок - "2", что-то другое - "3"')
            number = int(input())
            if number == 1:
                x = 'г. Воронеж, ул.'
            elif number == 2:
                x = 'г. Воронеж, пер.'
            s1 = Sovuch1S(ul)
            s2 = Sovuch2S(ul)
            s3 = Sovuch3S(ul)
            s4 = Sovuch4S(ul)
            s5 = Sovuch5S(ul)
            s6 = Sovuch6S(ul)
            s7 = Sovuch7S(ul)
            s8 = Sovuch8S(ul)
            ray = Sovetskiy(ul)
            if s1.get_pr(number):
                num = s1.get()
                rayon = ray.get_rayon()
                family = 'Пономаренко Елена Владимировна'
                index = '394038, г. Воронеж, ул. Домостроителей, д. 13'
                site = 'http://sovetsk1.vrn.msudrf.ru'
            elif s2.get_pr(number):
                num = s2.get()
                rayon = ray.get_rayon()
                family = 'Кульнева Наталья Николаевна'
                index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                site = 'http://sovetsk2.vrn.msudrf.ru'
            elif s3.get_pr(number):
                num = s3.get()
                rayon = ray.get_rayon()
                family = 'Берлева Наталья Валентиновна'
                index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                site = 'http://sovetsk3.vrn.msudrf.ru/'
            elif s4.get_pr(ul, number):
                num = s4.get()
                rayon = ray.get_rayon()
                family = 'Корпусова Ольга Игоревна'
                index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                site = 'http://sovetsk4.vrn.msudrf.ru/'
            elif s5.get_pr(number):
                num = s5.get()
                rayon = ray.get_rayon()
                family = 'Бессонов Виктор Сергеевич'
                index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                site = 'http://sovetsk5.vrn.msudrf.ru/'
            elif s6.get_pr(number):
                num = s6.get()
                rayon = ray.get_rayon()
                family = 'Касаева Ирина Сергеевна'
                index = '394026, г. Воронеж, ул. Плехановская, д. 53 (пристройка, 2-й эт.)'
                site = 'http://sovetsk6.vrn.msudrf.ru/'
            elif s7.get_pr(number):
                num = s7.get()
                rayon = ray.get_rayon()
                family = 'Пешков Вячеслав Вячеславович'
                index = '394062, г. Воронеж, ул. Краснозвездная, д. 4'
                site = 'http://sovetsk7.vrn.msudrf.ru/'
            elif s8.get_pr(number):
                num = s8.get()
                rayon = ray.get_rayon()
                family = 'Пидусова Елена Валерьевна'
                index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                site = 'http://sovetsk8.vrn.msudrf.ru/'
            if ul == 'Острогожская':
                dom = int(input('Введите номер дома\n'))
                if dom % 2 == 0 and dom >= 146:
                    num = s6.get()
                    rayon = ray.get_rayon()
                    family = 'Касаева Ирина Сергеевна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53 (пристройка, 2-й эт.)'
                    site = 'http://sovetsk2.vrn.msudrf.ru/'
        else:
            number = 0
        s1 = Sovuch1S(ul)
        s2 = Sovuch2S(ul)
        s3 = Sovuch3S(ul)
        s4 = Sovuch4S(ul)
        s5 = Sovuch5S(ul)
        s6 = Sovuch6S(ul)
        s7 = Sovuch7S(ul)
        s8 = Sovuch8S(ul)
        ray = Sovetskiy(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Пономаренко Елена Владимировна'
            index = '394038, г. Воронеж, ул. Домостроителей, д. 13'
            site = 'http://sovetsk1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Кульнева Наталья Николаевна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Берлева Наталья Валентиновна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Корпусова Ольга Игоревна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Бессонов Виктор Сергеевич'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Касаева Ирина Сергеевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53 (пристройка, 2-й эт.)'
            site = 'http://sovetsk6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Пешков Вячеслав Вячеславович'
            index = '394062, г. Воронеж, ул. Краснозвездная, д. 4'
            site = 'http://sovetsk7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Пидусова Елена Валерьевна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk8.vrn.msudrf.ru'
        s1 = Sovuch1Z(ul)
        s2 = Sovuch2Z(ul)
        s3 = Sovuch3Z(ul)
        s4 = Sovuch4Z(ul)
        s5 = Sovuch5Z(ul)
        ray = Zheleznodorozhny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Долгих Наталья Викторовна'
            index = '394007, г. Воронеж, ул. Ленинский проспект, д. 99'
            site = 'http://zhelezn1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Селищева Ангелина Алексеевна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Лепендина Наталья Владимировна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Филатова Наталия Ивановна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Сиухина Марина Валерьевна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn5.vrn.msudrf.ru'
        s1 = Sovuch1K(ul)
        s2 = Sovuch2K(ul)
        s3 = Sovuch3K(ul)
        s4 = Sovuch4K(ul)
        s5 = Sovuch5K(ul)
        s6 = Sovuch6K(ul)
        s7 = Sovuch7K(ul)
        s8 = Sovuch8K(ul)
        s9 = Sovuch9K(ul)
        s10 = Sovuch10K(ul)
        s11 = Sovuch11K(ul)
        s12 = Sovuch12K(ul)
        ray = Kominternovsky(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Косарева Елена Васильевна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Карабкова Ирина Митрофановна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Шульгина Людмила Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Азарова Екатерина Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Авраменко Светлана Александровна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Волкова Ирина Ивановна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Зайцева Ирина Дмитриевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Артамонов Дмитрий Викторович'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern8.vrn.msudrf.ru'
        elif s9.get_sovuch(number):
            num = s9.get()
            rayon = ray.get_rayon()
            family = 'Сурина Елена Рудольфовна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern9.vrn.msudrf.ru'
        elif s10.get_sovuch(number):
            num = s10.get()
            rayon = ray.get_rayon()
            family = 'Шурухина Елена Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern10.vrn.msudrf.ru'
        elif s11.get_sovuch(number):
            num = s11.get()
            rayon = ray.get_rayon()
            family = 'Похиль Елена Анатольевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern11.vrn.msudrf.ru'
        elif s12.get_sovuch(number):
            num = s12.get()
            rayon = ray.get_rayon()
            family = 'Шнибаева Юлия Евгеньевна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern12.vrn.msudrf.ru'
        s1 = Sovuch1Lv(ul)
        s2 = Sovuch2Lv(ul)
        s3 = Sovuch3Lv(ul)
        s4 = Sovuch4Lv(ul)
        s5 = Sovuch5Lv(ul)
        s6 = Sovuch6Lv(ul)
        s7 = Sovuch7Lv(ul)
        s8 = Sovuch8Lv(ul)
        ray = Levoberezhny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Барсуков Александр Юрьевич'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Суслова Ольга Викторовна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Козьякова Мария Юрьевна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Садчикова Ирина Викторовна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Костылева Татьяна Борисовна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Самойлова Людмила Владимировна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Голубцова Алия Сальмановна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Чумак Ирина Валерьевна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober8.vrn.msudrf.ru'
        s1 = Sovuch1Ln(ul)
        s2 = Sovuch2Ln(ul)
        s3 = Sovuch3Ln(ul)
        s4 = Sovuch4Ln(ul)
        s5 = Sovuch5Ln(ul)
        s6 = Sovuch6Ln(ul)
        s7 = Sovuch7Ln(ul)
        ray = Leninsky(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Гущина Светлана Васильевна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Николенко Елена Александровна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Полянская Ирина Викторовна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Шутейникова Вера Сергеевна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Самофалова Наталья Владимировна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Филимонова Татьяна Викторовна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Булгаков Сергей Николаевич'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky7.vrn.msudrf.ru'
        s1 = Sovuch1Cn(ul)
        s2 = Sovuch2Cn(ul)
        s3 = Sovuch3Cn(ul)
        s4 = Sovuch4Cn(ul)
        s5 = Sovuch5Cn(ul)
        ray = Сentralny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Глебова Людмила Владимировна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53(5 этаж)'
            site = 'http://centr1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Лихачева Елена Витальевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53(пристройка 3 этаж)'
            site = 'http://centr2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Бородинов Виталий Владимирович'
            index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
            site = 'http://centr3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Швырева Екатерина Анатольевна'
            index = '394026, г. Воронеж , ул. Плехановская, д. 53(5 этаж)'
            site = 'http://centr4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Клишина  Галина Васильевна'
            index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
            site = 'http://centr5.vrn.msudrf.ru'
    else:
        family = ''
        index = ''
        rayon = ''
        site = ''
        print('Введите название улицы или переулка, если это проспект, бульвар, набережная или проезд, '
              'пишите название вместе с этими словами')
        ul = input()
        s1 = Sovuch1S(ul)
        s2 = Sovuch2S(ul)
        s3 = Sovuch3S(ul)
        s4 = Sovuch4S(ul)
        s5 = Sovuch5S(ul)
        s6 = Sovuch6S(ul)
        s7 = Sovuch7S(ul)
        s8 = Sovuch8S(ul)
        print('Если это улица, нажмите "1", если переулок - "2"')
        number = int(input())
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г. Воронеж, пер.'
        ray = Sovetskiy(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Пономаренко Елена Владимировна'
            index = '394038, г. Воронеж, ул. Домостроителей, д. 13'
            site = 'http://sovetsk1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Кульнева Наталья Николаевна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Берлева Наталья Валентиновна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Корпусова Ольга Игоревна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Бессонов Виктор Сергеевич'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Касаева Ирина Сергеевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53 (пристройка, 2-й эт.)'
            site = "http://sovetsk6.vrn.msudrf.ru"
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Пешков Вячеслав Вячеславович'
            index = '394062, г. Воронеж, ул. Краснозвездная, д. 4'
            site = 'http://sovetsk7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Пидусова Елена Валерьевна'
            index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
            site = 'http://sovetsk8.vrn.msudrf.ru'
        s1 = Sovuch1Z(ul)
        s2 = Sovuch2Z(ul)
        s3 = Sovuch3Z(ul)
        s4 = Sovuch4Z(ul)
        s5 = Sovuch5Z(ul)
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г. Воронеж, пер.'
        ray = Zheleznodorozhny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Долгих Наталья Викторовна'
            index = '394007, г. Воронеж, ул. Ленинский проспект, д. 99'
            site = "http://zhelezn1.vrn.msudrf.ru"
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Селищева Ангелина Алексеевна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Лепендина Наталья Владимировна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Филатова Наталия Ивановна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Сиухина Марина Валерьевна'
            index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
            site = 'http://zhelezn5.vrn.msudrf.ru'
        s1 = Sovuch1K(ul)
        s2 = Sovuch2K(ul)
        s3 = Sovuch3K(ul)
        s4 = Sovuch4K(ul)
        s5 = Sovuch5K(ul)
        s6 = Sovuch6K(ul)
        s7 = Sovuch7K(ul)
        s8 = Sovuch8K(ul)
        s9 = Sovuch9K(ul)
        s10 = Sovuch10K(ul)
        s11 = Sovuch11K(ul)
        s12 = Sovuch12K(ul)
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г.Воронеж, пер.'
        ray = Kominternovsky(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Косарева Елена Васильевна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Карабкова Ирина Митрофановна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern2.vrn.msudrf.ru/'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Шульгина Людмила Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Азарова Екатерина Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Авраменко Светлана Александровна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Волкова Ирина Ивановна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Зайцева Ирина Дмитриевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Артамонов Дмитрий Викторович'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern8.vrn.msudrf.ru'
        elif s9.get_sovuch(number):
            num = s9.get()
            rayon = ray.get_rayon()
            family = 'Сурина Елена Рудольфовна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern9.vrn.msudrf.ru'
        elif s10.get_sovuch(number):
            num = s10.get()
            rayon = ray.get_rayon()
            family = 'Шурухина Елена Викторовна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern10.vrn.msudrf.ru'
        elif s11.get_sovuch(number):
            num = s11.get()
            rayon = ray.get_rayon()
            family = 'Похиль Елена Анатольевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53'
            site = 'http://komintern11.vrn.msudrf.ru'
        elif s12.get_sovuch(number):
            num = s12.get()
            rayon = ray.get_rayon()
            family = 'Шнибаева Юлия Евгеньевна'
            index = '394026, г. Воронеж, пр. Ясный, д. 2'
            site = 'http://komintern12.vrn.msudrf.ru'
        s1 = Sovuch1Lv(ul)
        s2 = Sovuch2Lv(ul)
        s3 = Sovuch3Lv(ul)
        s4 = Sovuch4Lv(ul)
        s5 = Sovuch5Lv(ul)
        s6 = Sovuch6Lv(ul)
        s7 = Sovuch7Lv(ul)
        s8 = Sovuch8Lv(ul)
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г. Воронеж, пер.'
        ray = Levoberezhny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Барсуков Александр Юрьевич'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Суслова Ольга Викторовна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Козьякова Мария Юрьевна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Садчикова Ирина Викторовна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Костылева Татьяна Борисовна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Самойлова Людмила Владимировна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Голубцова Алия Сальмановна'
            index = '394007, г. Воронеж, ул. Серова, д. 1'
            site = 'http://levober7.vrn.msudrf.ru'
        elif s8.get_sovuch(number):
            num = s8.get()
            rayon = ray.get_rayon()
            family = 'Чумак Ирина Валерьевна'
            index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
            site = 'http://levober8.vrn.msudrf.ru'
        s1 = Sovuch1Ln(ul)
        s2 = Sovuch2Ln(ul)
        s3 = Sovuch3Ln(ul)
        s4 = Sovuch4Ln(ul)
        s5 = Sovuch5Ln(ul)
        s6 = Sovuch6Ln(ul)
        s7 = Sovuch7Ln(ul)
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г.Воронеж, пер.'
        ray = Leninsky(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Гущина Светлана Васильевна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Николенко Елена Александровна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Полянская Ирина Викторовна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Шутейникова Вера Сергеевна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Самофалова Наталья Владимировна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky5.vrn.msudrf.ru'
        elif s6.get_sovuch(number):
            num = s6.get()
            rayon = ray.get_rayon()
            family = 'Филимонова Татьяна Викторовна'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky6.vrn.msudrf.ru'
        elif s7.get_sovuch(number):
            num = s7.get()
            rayon = ray.get_rayon()
            family = 'Булгаков Сергей Николаевич'
            index = '394006, г. Воронеж, ул. Станкевича, д. 36'
            site = 'http://leninsky7.vrn.msudrf.ru'
        s1 = Sovuch1Cn(ul)
        s2 = Sovuch2Cn(ul)
        s3 = Sovuch3Cn(ul)
        s4 = Sovuch4Cn(ul)
        s5 = Sovuch5Cn(ul)
        if number == 1:
            x = 'г. Воронеж, ул.'
        else:
            x = 'г. Воронеж, пер.'
        ray = Сentralny(ul)
        if s1.get_sovuch(number):
            num = s1.get()
            rayon = ray.get_rayon()
            family = 'Глебова Людмила Владимировна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53(5 этаж)'
            site = 'http://centr1.vrn.msudrf.ru'
        elif s2.get_sovuch(number):
            num = s2.get()
            rayon = ray.get_rayon()
            family = 'Лихачева Елена Витальевна'
            index = '394026, г. Воронеж, ул. Плехановская, д. 53(пристройка 3 этаж)'
            site = 'http://centr2.vrn.msudrf.ru'
        elif s3.get_sovuch(number):
            num = s3.get()
            rayon = ray.get_rayon()
            family = 'Бородинов Виталий Владимирович'
            index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
            site = 'http://centr3.vrn.msudrf.ru'
        elif s4.get_sovuch(number):
            num = s4.get()
            rayon = ray.get_rayon()
            family = 'Швырева Екатерина Анатольевна'
            index = '394026, г. Воронеж , ул. Плехановская, д. 53(5 этаж)'
            site = 'http://centr4.vrn.msudrf.ru'
        elif s5.get_sovuch(number):
            num = s5.get()
            rayon = ray.get_rayon()
            family = 'Клишина  Галина Васильевна'
            index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
            site = 'http://centr5.vrn.msudrf.ru'
        if rayon == '':
            dom = input('Введите номер дома\n')
            if '.' not in str(dom) and 'Г' not in str(dom) and 'В' not in str(dom) and 'А' not in \
                    str(dom) and 'Б' not in \
                    str(dom) and '/' not in str(dom) and 'Д' not in str(dom) and 'Е' not in str(dom) and 'Ж' not in str(
                dom) and 'З' not in str(dom) and 'а' not in str(dom) and 'б' not in str(dom) and 'в' not in str(
                dom) and 'г' not in str(dom) and 'д' not in str(dom) and 'е' not in str(dom) and 'ж' not in str(
                dom) and 'з' not in str(dom):
                dom = int(dom)
                s1 = Sovuch1S(ul)
                s3 = Sovuch3S(ul)
                s5 = Sovuch5S(ul)
                s6 = Sovuch6S(ul)
                s7 = Sovuch7S(ul)
                s8 = Sovuch8S(ul)
                ray = Sovetskiy(ul)
                if (ul == 'Ворошилова' and dom % 2 != 0 and (
                        19 >= dom >= 3)) or (
                        ul == 'Ворошилова' and dom % 2 == 0 and (
                        136 >= dom >= 16)) or (
                        ul == 'Пирогова' and dom % 2 != 0 and (
                        dom >= 23)) or (
                        ul == 'Пирогова' and dom % 2 == 0 and dom >= 8):
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Пономаренко Елена Владимировна'
                    index = '394038, г. Воронеж, ул. Домостроителей, д. 13'
                    site = 'http://sovetsk1.vrn.msudrf.ru'
                elif (ul == '9 Января' and dom % 2 != 0 and (dom >= 81)) or (
                        ul == 'Торпедо' and dom % 2 == 0 and (
                        9 >= dom >= 1)):
                    num = s3.get()
                    rayon = ray.get_rayon()
                    family = 'Берлева Наталья Валентиновна'
                    index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                    site = 'http://sovetsk3.vrn.msudrf.ru'
                elif (ul == 'Машиностроителей' and dom % 2 == 0 and (
                        94 >= dom >= 82)) or (
                        ul == 'Машиностроителей' and dom == 57) or (
                        ul == 'Свободы' and dom % 2 != 0 and (
                        89 >= dom >= 79)):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Бессонов Виктор Сергеевич'
                    index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                    site = 'http://sovetsk5.vrn.msudrf.ru'
                elif ul == 'Бахметьева' and dom % 2 != 0:
                    num = s6.get()
                    rayon = ray.get_rayon()
                    family = 'Касаева Ирина Сергеевна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53 (пристройка, 2-й эт.)'
                    site = 'http://sovetsk6.vrn.msudrf.ru'
                elif (ul == 'Газовая' and dom % 2 != 0 and (
                        23 >= dom >= 1)) or (
                        ul == 'Газовая' and dom % 2 == 0 and (
                        16 >= dom >= 2)) or (
                        ul == 'Кривошеина' and dom % 2 == 0 and (
                        dom >= 66)):
                    num = s7.get()
                    rayon = ray.get_rayon()
                    family = 'Пешков Вячеслав Вячеславович'
                    index = '394062, г. Воронеж, ул. Краснозвездная, д. 4'
                    site = 'http://sovetsk7.vrn.msudrf.ru'
                elif (ul == 'Карла Либкнехта' and dom % 2 != 0 and (
                        57 >= dom >= 53)) or (
                        ul == 'Карла Либкнехта' and dom == 74) or (
                        ul == 'Карла Либкнехта' and dom == 76) or (
                        ul == 'Летчика Колесниченко' and dom % 2 == 0 and (
                        dom >= 42)) or (
                        ul == 'Моисеева' and dom % 2 == 0 and (
                        84 >= dom >= 40)):
                    num = s8.get()
                    rayon = ray.get_rayon()
                    family = 'Пидусова Елена Валерьевна'
                    index = '394065, г. Воронеж, ул. Героев Сибиряков, д. 46'
                    site = 'http://sovetsk8.vrn.msudrf.ru'
                s1 = Sovuch1Z(ul)
                s2 = Sovuch2Z(ul)
                s3 = Sovuch3Z(ul)
                s4 = Sovuch4Z(ul)
                s5 = Sovuch5Z(ul)
                ray = Zheleznodorozhny(ul)
                if ul == 'Ленинский проспект' and dom % 2 != 0 and dom >= 119:
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Долгих Наталья Викторовна'
                    index = '394007, г. Воронеж, ул. Ленинский проспект, д. 99'
                    site = 'http://zhelezn1.vrn.msudrf.ru'
                elif ul == 'Ленинский проспект' and dom % 2 == 0 and dom >= 124:
                    num = s2.get()
                    rayon = ray.get_rayon()
                    family = 'Селищева Ангелина Алексеевна'
                    index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
                    site = 'http://zhelezn2.vrn.msudrf.ru'
                elif ul == 'Димитрова' and dom % 2 != 0 and dom <= 95:
                    num = s3.get()
                    rayon = ray.get_rayon()
                    family = 'Лепендина Наталья Владимировна'
                    index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
                    site = 'http://zhelezn3.vrn.msudrf.ru'
                elif (ul == 'Минская' and dom % 2 != 0 and dom <= 43) or (
                        ul == 'Минская' and dom % 2 == 0):
                    num = s4.get()
                    rayon = ray.get_rayon()
                    family = 'Филатова Наталия Ивановна'
                    index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
                    site = 'http://zhelezn4.vrn.msudrf.ru'
                elif (ul == 'Ильича' and 42 >= dom >= 1) or (
                        ul == 'Минская' and dom / 2 != 0 and dom >= 43) or (
                        ul == 'Старых Большевиков ' and dom <= 69) or (
                        ul == 'Ленинградская' and dom == 1):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Сиухина Марина Валерьевна'
                    index = '394033, г. Воронеж, ул. Ленинский проспект, д. 174'
                    site = 'http://zhelezn5.vrn.msudrf.ru'
                s1 = Sovuch1K(ul)
                s2 = Sovuch2K(ul)
                s5 = Sovuch5K(ul)
                s6 = Sovuch6K(ul)
                s7 = Sovuch7K(ul)
                s8 = Sovuch8K(ul)
                s9 = Sovuch9K(ul)
                s10 = Sovuch10K(ul)
                s11 = Sovuch11K(ul)
                s12 = Sovuch12K(ul)
                ray = Kominternovsky(ul)
                if (ul == 'Московский проспект' and dom % 2 != 0) or (ul == 'Московский Проспект' and dom % 2 != 0):
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Косарева Елена Васильевна'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern1.vrn.msudrf.ru'
                elif (ul == 'Генерала Лизюкова' and dom % 2 != 0) or (ul == 'Лизюкова' and dom % 2 != 0) or (ul ==
                                                                                                             'Г.Лизюкова' and dom % 2 != 0):
                    num = s2.get()
                    rayon = ray.get_rayon()
                    family = 'Карабкова Ирина Митрофановна'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern2.vrn.msudrf.ru'
                elif (ul == '9 Января' and dom % 2 == 0 and dom >= 102) or (
                        ul == 'Краснодонская' and dom % 2 != 0 and dom >= 21) or (
                        ul == 'Краснодонская' and dom % 2 == 0 and dom >= 14):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Авраменко Светлана Александровна'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern5.vrn.msudrf.ru'
                elif (ul == 'Хользунова' and dom % 2 == 0) or (
                        ul == 'Хользунова' and dom % 2 != 0 and dom >= 107):
                    num = s6.get()
                    rayon = ray.get_rayon()
                    family = 'Волкова Ирина Ивановна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53'
                    site = 'http://komintern6.vrn.msudrf.ru'
                elif ul == 'Владимира Невского' and dom % 2 == 0:
                    num = s7.get()
                    rayon = ray.get_rayon()
                    family = 'Зайцева Ирина Дмитриевна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53'
                    site = 'http://komintern7.vrn.msudrf.ru'
                elif (ul == 'Рабочий проспект' and dom % 2 != 0 and dom >= 47) or (
                        ul == 'Рабочий проспект' and dom % 2 == 0 and dom >= 62) or (
                        ul == 'Транспортная' and dom % 2 != 0) or (
                        ul == 'Рабочий Проспект' and dom % 2 != 0 and dom >= 47) or (
                        ul == 'Рабочий Проспект' and dom % 2 == 0 and dom >= 62):
                    num = s8.get()
                    rayon = ray.get_rayon()
                    family = 'Артамонов Дмитрий Викторович'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern8.vrn.msudrf.ru'
                elif (ul == 'Машиностроителей' and dom % 2 == 0 and 80 >= dom >= 2) or (
                        ul == 'Машиностроителей' and dom % 2 != 0 and 51 >= dom >= 1):
                    num = s9.get()
                    rayon = ray.get_rayon()
                    family = 'Сурина Елена Рудольфовна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53'
                    site = 'http://komintern9.vrn.msudrf.ru'
                elif ul == 'Владимира Невского' and dom % 2 != 0:
                    num = s10.get()
                    rayon = ray.get_rayon()
                    family = 'Шурухина Елена Викторовна'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern10.vrn.msudrf.ru'
                elif (ul == 'Генерала Лизюкова' and dom % 2 == 0) or (
                        ul == 'Шишкова' and dom % 2 != 0 and 83 >= dom >= 1):
                    num = s11.get()
                    rayon = ray.get_rayon()
                    family = 'Похиль Елена Анатольевна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53'
                    site = 'http://komintern11.vrn.msudrf.ru'
                elif (ul == 'Московский проспект' and dom % 2 == 0 and 116 >= dom >= 2) or (
                        ul == 'Московский Проспект' and dom % 2 == 0 and 116 >= dom >= 2) or (
                        ul == 'Газовая' and dom % 2 == 0 and dom >= 18) or (
                        ul == 'Газовая' and dom % 2 != 0 and dom >= 25) or (
                        ul == 'Хользунова' and dom % 2 != 0 and 105 >= dom >= 1) or (
                        ul == 'Шишкова' and dom % 2 == 0 and 136 >= dom >= 2):
                    num = s12.get()
                    rayon = ray.get_rayon()
                    family = 'Шнибаева Юлия Евгеньевна'
                    index = '394026, г. Воронеж, пр. Ясный, д. 2'
                    site = 'http://komintern12.vrn.msudrf.ru'
                s1 = Sovuch1Lv(ul)
                s2 = Sovuch2Lv(ul)
                s3 = Sovuch3Lv(ul)
                s4 = Sovuch4Lv(ul)
                s5 = Sovuch5Lv(ul)
                s6 = Sovuch6Lv(ul)
                s7 = Sovuch7Lv(ul)
                ray = Levoberezhny(ul)
                if ul == 'Новосибирская' and dom % 2 != 0:
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Барсуков Александр Юрьевич'
                    index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
                    site = 'http://levober1.vrn.msudrf.ru'
                elif ul == 'Ростовская' and dom % 2 == 0:
                    num = s2.get()
                    rayon = ray.get_rayon()
                    family = 'Суслова Ольга Викторовна'
                    index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
                    site = 'http://levober2.vrn.msudrf.ru'
                elif (ul == 'Набережная Авиастроителей' and 22 >= dom >= 1) or (
                        ul == 'Новосибирская' and dom % 2 == 0) or (
                        ul == 'Ростовская' and dom % 2 != 0):
                    num = s3.get()
                    rayon = ray.get_rayon()
                    family = 'Козьякова Мария Юрьевна'
                    index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
                    site = 'http://levober3.vrn.msudrf.ru'
                elif (ul == 'Ильича' and dom >= 42) or (
                        ul == 'Ленинградская' and dom >= 2):
                    num = s4.get()
                    rayon = ray.get_rayon()
                    family = 'Садчикова Ирина Викторовна'
                    index = '394007, г. Воронеж, ул. Серова, д. 1'
                    site = 'http://levober4.vrn.msudrf.ru'
                elif (ul == 'Ленинский проспект' and dom % 2 == 0) or (ul == 'Ленинский Проспект' and dom % 2 == 0) or (
                        ul == 'Набережная Авиастроителей' and dom >= 23):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Костылева Татьяна Борисовна'
                    index = '394007, г. Воронеж, ул. Серова, д. 1'
                    site = 'http://levober5.vrn.msudrf.ru'
                elif (ul == 'Ленинский проспект' and dom % 2 != 0 and 117 >= dom) or (
                        ul == 'Ленинский Проспект' and dom % 2 != 0 and 117 >= dom) or (
                        ul == 'Димитрова' and dom % 2 == 0 and 102 >= dom >= 2) or (
                        ul == 'Старых Большевиков' and dom >= 83):
                    num = s6.get()
                    rayon = ray.get_rayon()
                    family = 'Самойлова Людмила Владимировна'
                    index = '394028, г. Воронеж, ул. Волгоградская, д. 30'
                    site = 'http://levober6.vrn.msudrf.ru'
                elif (ul == 'Димитрова' and dom >= 103) or (
                        ul == 'Павловский' and dom != 56):
                    num = s7.get()
                    rayon = ray.get_rayon()
                    family = 'Голубцова Алия Сальмановна'
                    index = '394007, г. Воронеж, ул. Серова, д. 1'
                    site = 'http://levober7vrn.msudrf.ru'
                s1 = Sovuch1Ln(ul)
                s2 = Sovuch2Ln(ul)
                s3 = Sovuch3Ln(ul)
                s4 = Sovuch4Ln(ul)
                s5 = Sovuch5Ln(ul)
                s6 = Sovuch6Ln(ul)
                s7 = Sovuch7Ln(ul)
                ray = Leninsky(ul)
                if (ul == '3-Го Интерн.' and dom % 2 != 0 and dom >= 35) or (
                        ul == '3-Го Интерн.' and dom % 2 == 0 and dom >= 26) or (
                        ul == 'Бахметьева' and dom % 2 == 0 and 10 >= dom >= 2) or (
                        ul == 'Войкова' and dom % 2 != 0 and dom >= 17) or (
                        ul == 'Войкова' and dom % 2 == 0 and dom >= 22) or (
                        ul == 'Куколкина' and dom % 2 != 0 and dom >= 31) or (
                        ul == 'Куколкина' and dom % 2 == 0 and dom >= 28) or (
                        ul == 'Пирогова' and dom % 2 == 0 and 6 >= dom >= 2) or (
                        ul == 'Пирогова' and dom % 2 != 0 and 21 >= dom >= 1) or (
                        ul == 'Революции 1905 г.' and dom % 2 != 0 and dom >= 23) or (
                        ul == 'Революции 1905 г.' and dom % 2 == 0 and dom >= 62) or (
                        ul == 'Революции 1905 Г.' and dom % 2 != 0 and dom >= 23) or (
                        ul == 'Революции 1905 Г.' and dom % 2 == 0 and dom >= 62):
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Гущина Светлана Васильевна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky1.vrn.msudrf.ru'
                elif (ul == '9 Января' and dom % 2 == 0 and 40 >= dom >= 2) or (
                        ul == '9 Января' and dom % 2 != 0 and 47 >= dom >= 1) or (
                        ul == 'Белостокская' and 14 >= dom >= 1) or (
                        ul == 'Белостокская' and dom >= 23) or (
                        ul == 'Бетховена' and dom % 2 == 0) or (
                        ul == 'Веры Фигнер' and dom % 2 == 0 and dom >= 112) or (
                        ul == 'Веры Фигнер' and dom % 2 != 0 and dom >= 91) or (
                        ul == 'Володарского' and 37 >= dom >= 1) or (
                        ul == 'Клубная' and dom % 2 != 0 and dom >= 51) or (
                        ul == 'Клубная' and dom % 2 == 0 and dom >= 52) or (
                        ul == 'Куколкина' and dom % 2 != 0 and 29 >= dom >= 1) or (
                        ul == 'Куколкина' and dom % 2 == 0 and 26 >= dom >= 2) or (
                        ul == 'Куцыгина' and dom >= 32) or (
                        ul == 'Никитинская' and dom % 2 != 0 and 49 >= dom >= 29) or (
                        ul == 'Орджоникидзе' and dom % 2 != 0 and dom >= 35) or (
                        ul == 'Орджоникидзе' and dom % 2 == 0 and dom >= 28) or (
                        ul == 'Свободы' and dom % 2 == 0 and 24 >= dom) or (
                        ul == 'Свободы' and dom % 2 != 0 and dom <= 59) or (
                        ul == 'Софьи Перовской' and dom % 2 != 0 and 73 >= dom >= 67) or (
                        ul == 'Софьи Перовской' and dom % 2 == 0 and 108 >= dom >= 100) or (
                        ul == 'С.Перовской' and dom % 2 != 0 and 73 >= dom >= 67) or (
                        ul == 'С.Перовской' and dom % 2 == 0 and 108 >= dom >= 100):
                    num = s2.get()
                    rayon = ray.get_rayon()
                    family = 'Николенко Елена Александровна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky2.vrn.msudrf.ru'
                elif (ul == '5 Декабря' and dom % 2 == 0 and 36 >= dom >= 2) or (
                        ul == '5 Декабря' and dom % 2 != 0 and 39 >= dom >= 1) or (
                        ul == 'Белостокская' and 22 >= dom >= 15) or (
                        ul == 'Бетховена' and dom % 2 != 0) or (
                        ul == 'Веры Фигнер' and dom % 2 == 0 and 110 >= dom >= 2) or (
                        ul == 'Веры Фигнер' and dom % 2 != 0 and 89 >= dom >= 1) or (
                        ul == 'В.Фигнер' and dom % 2 == 0 and 110 >= dom >= 2) or (
                        ul == 'В.Фигнер' and dom % 2 != 0 and 89 >= dom >= 1) or (
                        ul == 'Гродненская' and dom % 2 == 0 and 38 >= dom >= 2) or (
                        ul == 'Гродненская' and dom % 2 != 0 and 91 >= dom >= 1) or (
                        ul == 'Клубная' and dom % 2 == 0 and 50 >= dom >= 2) or (
                        ul == 'Клубная' and dom % 2 != 0 and 49 >= dom >= 1) or (
                        ul == 'Краснознамённая' and dom % 2 != 0 and 45 >= dom >= 1) or (
                        ul == 'Одоевского' and 13 >= dom >= 1) or (
                        ul == 'Ф.Энгельса' and dom % 2 != 0 and dom >= 39) or (
                        ul == 'Ф.Энгельса' and dom % 2 == 0 and dom >= 58) or (
                        ul == 'Фридриха Энгельса' and dom % 2 != 0 and dom >= 39) or (
                        ul == 'Фридриха Энгельса' and dom % 2 == 0 and dom >= 58) or (
                        ul == 'Каховский' and 43 >= dom >= 1):
                    num = s3.get()
                    rayon = ray.get_rayon()
                    family = 'Полянская Ирина Викторовна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky3.vrn.msudrf.ru'
                elif (ul == 'Иртышская' and dom % 2 == 0) or (
                        ul == 'Крылова' and dom % 2 == 0 and 94 >= dom >= 28) or (
                        ul == 'Крылова' and 93 >= dom >= 27) or (
                        ul == 'Краснознамённая' and dom % 2 != 0 and 171 >= dom >= 99) or (
                        ul == 'Куцыгина' and 31 >= dom >= 1) or (
                        ul == 'Одоевского' and dom % 2 == 0 and dom >= 28) or (
                        ul == 'Одоевского' and dom % 2 != 0 and dom >= 15) or (
                        ul == 'Онежская' and dom % 2 != 0) or (
                        ul == 'Островского' and dom % 2 == 0 and dom >= 26) or (
                        ul == 'Островского' and dom % 2 != 0 and dom >= 27) or (
                        ul == 'Плехановская' and dom % 2 != 0) or (
                        ul == 'Успенского' and dom % 2 == 0 and dom >= 28) or (
                        ul == 'Успенского' and dom % 2 != 0 and dom >= 27) or (
                        ul == 'Херсонская' and dom % 2 == 0 and 62 >= dom >= 2) or (
                        ul == 'Чапаева' and dom % 2 == 0 and dom >= 42) or (
                        ul == 'Чехова' and dom % 2 == 0 and dom >= 22) or (
                        ul == 'Чехова' and dom % 2 != 0 and dom >= 25):
                    num = s4.get()
                    rayon = ray.get_rayon()
                    family = 'Шутейникова Вера Сергеевна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky4.vrn.msudrf.ru'
                elif (ul == '5 Декабря' and dom % 2 == 0 and dom >= 38) or (
                        ul == '5 Декабря' and dom % 2 != 0 and dom >= 41) or (
                        ul == 'Ворошилова' and dom % 2 == 0 and 14 >= dom >= 2) or (
                        ul == 'Госпитальная' and dom % 2 == 0 and 76 >= dom >= 2) or (
                        ul == 'Госпитальная' and dom % 2 != 0 and 57 >= dom >= 1) or (
                        ul == 'Гродненская' and dom % 2 == 0 and 88 >= dom >= 40) or (
                        ul == 'Карла Либкнехта' and dom % 2 == 0 and 72 >= dom >= 2) or (
                        ul == 'Карла Либкнехта' and dom % 2 != 0 and 51 >= dom >= 1) or (
                        ul == 'К.Либкнехта' and dom % 2 == 0 and 72 >= dom >= 2) or (
                        ul == 'К.Либкнехта' and dom % 2 != 0 and 51 >= dom >= 1) or (
                        ul == 'Карельская' and dom % 2 == 0 and 58 >= dom >= 2) or (
                        ul == 'Карельская' and dom % 2 != 0 and 65 >= dom >= 1) or (
                        ul == 'Краснознамённая' and dom % 2 == 0 and 158 >= dom >= 12) or (
                        ul == 'Краснознамённая' and dom % 2 != 0 and 97 >= dom >= 47) or (
                        ul == 'Колесниченко' and dom % 2 != 0) or (
                        ul == 'Колесниченко' and dom % 2 == 0 and 40 >= dom >= 2) or (
                        ul == 'Крылова' and dom % 2 == 0 and 26 >= dom >= 2) or (
                        ul == 'Крылова' and dom % 2 != 0 and 25 >= dom >= 1) or (
                        ul == 'Моисеева' and dom % 2 != 0) or (
                        ul == 'Моисеева' and dom % 2 == 0 and 40 >= dom >= 84) or (
                        ul == 'Одоевского' and dom % 2 == 0 and 26 >= dom >= 2) or (
                        ul == 'Островского' and dom % 2 == 0 and 24 >= dom >= 2) or (
                        ul == 'Островского' and dom % 2 != 0 and 25 >= dom >= 1) or (
                        ul == 'Петрозаводская' and dom % 2 != 0 and dom >= 13) or (
                        ul == 'Петрозаводская' and dom % 2 == 0 and dom >= 14) or (
                        ul == 'Успенского' and dom % 2 == 0 and 26 >= dom >= 2) or (
                        ul == 'Успенского' and dom % 2 != 0 and 25 >= dom >= 1) or (
                        ul == 'Чапаева' and dom % 2 == 0 and 40 >= dom >= 2) or (
                        ul == 'Чапаева' and dom % 2 != 0 and 29 >= dom >= 1) or (
                        ul == 'Чехова' and dom % 2 == 0 and 20 >= dom >= 2) or (
                        ul == 'Чехова' and dom % 2 != 0 and 23 >= dom >= 1) or (
                        ul == 'Каховского' and dom >= 44) or (
                        ul == 'Летчиков' and dom % 2 == 0) or (
                        ul == 'Туркменский' and 28 >= dom >= 1):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Самофалова Наталья Владимировна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky5.vrn.msudrf.ru'
                elif (ul == '9 Января' and dom % 2 != 0 and 79 >= dom >= 49) or (
                        ul == '9 Января' and dom % 2 == 0 and 100 >= dom >= 42) or (
                        ul == 'Ворошилова' and dom % 2 != 0 and dom >= 21) or (
                        ul == 'Госпитальная' and dom % 2 == 0 and dom >= 78) or (
                        ul == 'Госпитальная' and dom % 2 != 0 and dom >= 59) or (
                        ul == 'Иртышская' and dom % 2 != 0) or (
                        ul == 'Карельская' and dom % 2 == 0 and dom >= 60) or (
                        ul == 'Карельская' and dom % 2 != 0 and dom >= 67) or (
                        ul == 'Краснознамённая' and dom % 2 == 0 and 214 >= dom >= 160) or (
                        ul == 'Краснознамённая' and dom % 2 != 0 and dom >= 173) or (
                        ul == 'Кривошеина' and dom % 2 != 0) or (
                        ul == 'Кривошеина' and dom % 2 == 0 and 64 >= dom >= 2) or (
                        ul == 'Львовская' and dom % 2 != 0 and 11 >= dom >= 1) or (
                        ul == 'Львовская' and dom % 2 == 0 and 12 >= dom >= 2) or (
                        ul == 'Матросова' and dom % 2 == 0 and dom >= 8) or (
                        ul == 'Матросова' and dom % 2 != 0 and 207 >= dom >= 73) or (
                        ul == 'Онежская' and dom % 2 == 0) or (
                        ul == 'Острогожская' and dom % 2 == 0 and 158 >= dom) or (
                        ul == 'Острогожская' and dom % 2 != 0 and 91 >= dom >= 57) or (
                        ul == 'Петрозаводская' and dom % 2 != 0 and 11 >= dom >= 1) or (
                        ul == 'Петрозаводская' and dom % 2 == 0 and 12 >= dom >= 2) or (
                        ul == 'Пушкинская' and 45 >= dom >= 8) or (
                        ul == 'Херсонская' and dom % 2 == 0 and dom >= 64) or (
                        ul == 'Херсонская' and dom % 2 != 0) or (
                        ul == 'Моисеева' and dom % 2 == 0 and 40 >= dom >= 84) or (
                        ul == 'Туркменский' and dom >= 29):
                    num = s6.get()
                    rayon = ray.get_rayon()
                    family = 'Филимонова Татьяна Викторовна'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky6.vrn.msudrf.ru'
                elif (ul == 'Кольцовская' and dom % 2 != 0 and dom >= 33) or (
                        ul == 'Кольцовская' and dom % 2 == 0 and dom >= 52) or (
                        ul == 'Краснознамённая' and dom % 2 == 0 and 10 >= dom >= 2) or (
                        ul == 'Львовская' and dom % 2 != 0 and dom >= 13) or (
                        ul == 'Львовская' and dom % 2 == 0 and dom >= 14) or (
                        ul == 'Матросова' and dom % 2 != 0 and 73 >= dom >= 1) or (
                        ul == 'Матросова' and dom % 2 == 0 and 6 >= dom >= 2) or (
                        ul == 'Никитинская' and dom % 2 == 0 and 54 >= dom >= 36) or (
                        ul == 'Острогожская' and dom % 2 != 0 and 55 >= dom >= 1) or (
                        ul == 'Свободы' and dom % 2 != 0 and dom >= 65) or (
                        ul == 'Свободы' and dom % 2 == 0 and dom >= 26) or (
                        ul == 'Чапаева' and dom % 2 != 0 and dom >= 31):
                    num = s7.get()
                    rayon = ray.get_rayon()
                    family = 'Булгаков Сергей Николаевич'
                    index = '394006, г. Воронеж, ул. Станкевича, д. 36'
                    site = 'http://leninsky7.vrn.msudrf.ru'
                s1 = Sovuch1Cn(ul)
                s2 = Sovuch2Cn(ul)
                s3 = Sovuch3Cn(ul)
                s4 = Sovuch4Cn(ul)
                s5 = Sovuch5Cn(ul)
                ray = Сentralny(ul)
                if (ul == 'Плехановская' and dom % 2 == 0 and 38 >= dom >= 12) or (
                        ul == 'Рабочий проспект' and dom % 2 != 0 and 45 >= dom >= 1) or (
                        ul == 'Рабочий проспект' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'Рабочий Проспект' and dom % 2 != 0 and 45 >= dom >= 1) or (
                        ul == 'Рабочий Проспект' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'Шишкова' and dom % 2 != 0 and dom >= 85):
                    num = s1.get()
                    rayon = ray.get_rayon()
                    family = 'Глебова Людмила Владимировна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53(5 этаж)'
                    site = 'http://centr1.vrn.msudrf.ru'
                elif (ul == 'Берег реки' and 82 >= dom >= 47) or (
                        ul == 'Проспект Революции' and dom / 2 != 0 and 55 >= dom >= 21) or (
                        ul == 'Володарского' and dom % 2 == 0) or (
                        ul == 'Володарского' and dom % 2 != 0 and dom >= 38) or (
                        ul == 'Орджоникидзе' and 37 >= dom >= 1) or (
                        ul == 'Плехановская' and dom % 2 == 0 and 10 >= dom >= 2) or (
                        ul == 'Транспортная' and dom % 2 == 0):
                    num = s2.get()
                    rayon = ray.get_rayon()
                    family = 'Лихачева Елена Витальевна'
                    index = '394026, г. Воронеж, ул. Плехановская, д. 53(пристройка 3 этаж)'
                    site = 'http://centr2.vrn.msudrf.ru'
                elif (ul == 'Карла Маркса' and dom % 2 != 0 and dom >= 47) or (
                        ul == 'Карла Маркса' and dom >= 62) or (
                        ul == 'Пушкинская' and 7 >= dom >= 1) or (
                        ul == 'Ф.Энгельса' and dom % 2 != 0 and 37 >= dom >= 1) or (
                        ul == 'Ф.Энгельса' and dom % 2 == 0 and 56 >= dom >= 2) or (
                        ul == 'Фридриха Энгельса' and dom % 2 != 0 and 37 >= dom >= 1) or (
                        ul == 'Фридриха Энгельса' and dom % 2 == 0 and 56 >= dom >= 2) or (
                        ul == 'Шишкова' and dom % 2 == 0 and dom >= 140):
                    num = s3.get()
                    rayon = ray.get_rayon()
                    family = 'Бородинов Виталий Владимирович'
                    index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
                    site = 'http://centr3.vrn.msudrf.ru'
                elif (ul == 'Войкова' and dom % 2 != 0 and 15 >= dom >= 1) or (
                        ul == 'Войкова' and dom % 2 == 0 and 20 >= dom >= 2) or (
                        ul == 'Кольцовская' and dom % 2 != 0 and 31 >= dom >= 1) or (
                        ul == 'Кольцовская' and dom % 2 == 0 and 46 >= dom >= 2) or (
                        ul == 'Никитинская' and dom % 2 != 0 and 27 >= dom >= 1) or (
                        ul == 'Никитинская' and dom % 2 == 0 and 34 >= dom >= 2) or (
                        ul == 'Революции 1905 Г.' and dom % 2 != 0 and 11 >= dom >= 1) or (
                        ul == 'Революции 1905 Г.' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'Революции 1905 г.' and dom % 2 != 0 and 11 >= dom >= 1) or (
                        ul == 'Революции 1905 г.' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'Республиканская' and dom % 2 != 0 and 25 >= dom >= 1) or (
                        ul == 'Республиканская' and dom % 2 == 0 and 30 >= dom >= 2) or (
                        ul == 'Свердлова' and 6 >= dom >= 5) or (
                        ul == 'Студенческая' and dom != 17) or (
                        ul == 'Урицкого' and 5 >= dom >= 1):
                    num = s4.get()
                    rayon = ray.get_rayon()
                    family = 'Швырева Екатерина Анатольевна'
                    index = '394026, г. Воронеж , ул. Плехановская, д. 53(5 этаж)'
                    site = 'http://centr4.vrn.msudrf.ru'
                elif (ul == 'Проспект Революции' and dom % 2 != 0 and 19 >= dom >= 1) or (
                        ul == 'Проспект Революции' and dom % 2 == 0 and 58 >= dom >= 2) or (
                        ul == 'Московский проспект' and dom % 2 == 0 and dom >= 118) or (
                        ul == 'Московский Проспект' and dom % 2 == 0 and dom >= 118) or (
                        ul == 'Берег реки' and 50 >= dom >= 1) or (
                        ul == 'Карла Маркса' and dom % 2 != 0 and 45 >= dom >= 1) or (
                        ul == 'Карла Маркса' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'К.Маркса' and dom % 2 != 0 and 45 >= dom >= 1) or (
                        ul == 'К.Маркса' and dom % 2 == 0 and 60 >= dom >= 2) or (
                        ul == 'Плехановская' and dom % 2 == 0 and dom >= 40) or (
                        ul == '3-Го Интерн.' and dom % 2 != 0 and 33 >= dom) or (
                        ul == '3-Го Интерн.' and dom % 2 == 0 and 24 >= dom) or (
                        ul == '3 Интернационала.' and dom % 2 != 0 and 33 >= dom) or (
                        ul == '3 Интернационала' and dom % 2 == 0 and 24 >= dom):
                    num = s5.get()
                    rayon = ray.get_rayon()
                    family = 'Клишина  Галина Васильевна'
                    index = '394018, г. Воронеж, ул. Фридриха Энгельса, д. 72а'
                    site = 'http://centr5.vrn.msudrf.ru'
    print(num)
    print(rayon)
    file_name = input('Введите имя файла - шаблона с обозначением формата. Пример: file.docx\n')
    ndol = int(input('Введите кол-во должников\n'))
    if ndol == 1:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
    elif ndol == 2:
        name = input('Введите ФИО должника\n')
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 3:
        name = input('Введите ФИО должника\n')
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 4:
        name = input('Введите ФИО должника\n')
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 5:
        name = input('Введите ФИО должника\n')
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 6:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 7:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 8:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 9:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 10:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 11:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
        name11 = input('Введите ФИО должника\n')
        date11 = input('Введите дату рождения должника\n')
        place11 = input('Введите место рождения должника\n')
        ser11 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 12:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
        name11 = input('Введите ФИО должника\n')
        date11 = input('Введите дату рождения должника\n')
        place11 = input('Введите место рождения должника\n')
        ser11 = input('Введите серию и номер паспорта должника\n')
        name12 = input('Введите ФИО должника\n')
        date12 = input('Введите дату рождения должника\n')
        place12 = input('Введите место рождения должника\n')
        ser12 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 13:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
        name11 = input('Введите ФИО должника\n')
        date11 = input('Введите дату рождения должника\n')
        place11 = input('Введите место рождения должника\n')
        ser11 = input('Введите серию и номер паспорта должника\n')
        name12 = input('Введите ФИО должника\n')
        date12 = input('Введите дату рождения должника\n')
        place12 = input('Введите место рождения должника\n')
        ser12 = input('Введите серию и номер паспорта должника\n')
        name13 = input('Введите ФИО должника\n')
        date13 = input('Введите дату рождения должника\n')
        place13 = input('Введите место рождения должника\n')
        ser13 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 14:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
        name11 = input('Введите ФИО должника\n')
        date11 = input('Введите дату рождения должника\n')
        place11 = input('Введите место рождения должника\n')
        ser11 = input('Введите серию и номер паспорта должника\n')
        name12 = input('Введите ФИО должника\n')
        date12 = input('Введите дату рождения должника\n')
        place12 = input('Введите место рождения должника\n')
        ser12 = input('Введите серию и номер паспорта должника\n')
        name13 = input('Введите ФИО должника\n')
        date13 = input('Введите дату рождения должника\n')
        place13 = input('Введите место рождения должника\n')
        ser13 = input('Введите серию и номер паспорта должника\n')
        name14 = input('Введите ФИО должника\n')
        date14 = input('Введите дату рождения должника\n')
        place14 = input('Введите место рождения должника\n')
        ser14 = input('Введите серию и номер паспорта должника\n')
    elif ndol == 15:
        print('Введите ФИО должника')
        name = input()
        date = input('Введите дату рождения должника\n')
        place = input('Введите место рождения должника\n')
        ser = input('Введите серию и номер паспорта должника\n')
        name2 = input('Введите ФИО должника\n')
        date2 = input('Введите дату рождения должника\n')
        place2 = input('Введите место рождения должника\n')
        ser2 = input('Введите серию и номер паспорта должника\n')
        name3 = input('Введите ФИО должника\n')
        date3 = input('Введите дату рождения должника\n')
        place3 = input('Введите место рождения должника\n')
        ser3 = input('Введите серию и номер паспорта должника\n')
        name4 = input('Введите ФИО должника\n')
        date4 = input('Введите дату рождения должника\n')
        place4 = input('Введите место рождения должника\n')
        ser4 = input('Введите серию и номер паспорта должника\n')
        name5 = input('Введите ФИО должника\n')
        date5 = input('Введите дату рождения должника\n')
        place5 = input('Введите место рождения должника\n')
        ser5 = input('Введите серию и номер паспорта должника\n')
        name6 = input('Введите ФИО должника\n')
        date6 = input('Введите дату рождения должника\n')
        place6 = input('Введите место рождения должника\n')
        ser6 = input('Введите серию и номер паспорта должника\n')
        name7 = input('Введите ФИО должника\n')
        date7 = input('Введите дату рождения должника\n')
        place7 = input('Введите место рождения должника\n')
        ser7 = input('Введите серию и номер паспорта должника\n')
        name8 = input('Введите ФИО должника\n')
        date8 = input('Введите дату рождения должника\n')
        place8 = input('Введите место рождения должника\n')
        ser8 = input('Введите серию и номер паспорта должника\n')
        name9 = input('Введите ФИО должника\n')
        date9 = input('Введите дату рождения должника\n')
        place9 = input('Введите место рождения должника\n')
        ser9 = input('Введите серию и номер паспорта должника\n')
        name10 = input('Введите ФИО должника\n')
        date10 = input('Введите дату рождения должника\n')
        place10 = input('Введите место рождения должника\n')
        ser10 = input('Введите серию и номер паспорта должника\n')
        name11 = input('Введите ФИО должника\n')
        date11 = input('Введите дату рождения должника\n')
        place11 = input('Введите место рождения должника\n')
        ser11 = input('Введите серию и номер паспорта должника\n')
        name12 = input('Введите ФИО должника\n')
        date12 = input('Введите дату рождения должника\n')
        place12 = input('Введите место рождения должника\n')
        ser12 = input('Введите серию и номер паспорта должника\n')
        name13 = input('Введите ФИО должника\n')
        date13 = input('Введите дату рождения должника\n')
        place13 = input('Введите место рождения должника\n')
        ser13 = input('Введите серию и номер паспорта должника\n')
        name14 = input('Введите ФИО должника\n')
        date14 = input('Введите дату рождения должника\n')
        place14 = input('Введите место рождения должника\n')
        ser14 = input('Введите серию и номер паспорта должника\n')
        name15 = input('Введите ФИО должника\n')
        date15 = input('Введите дату рождения должника\n')
        place15 = input('Введите место рождения должника\n')
        ser15 = input('Введите серию и номер паспорта должника\n')
    plat = input('Введите номер платёжного поручения\n')
    dplat = input('Введите дату платёжного поручения\n')
    lschet = input('Введите лицевой счет\n')
    fam = [[[]], [[]], [[]]]
    if family == '':
        fam[1] = ['']
        fam[2] = ['']
        fam[0] = ''
    else:
        fam = family.split()
    d = [x, ul]
    address = ' '.join(d) + ' д.' + str(dom)
    print('Если адрес корректен нажмите "Enter", иначе введите недостающие сведения')
    print(address)
    m = input()
    if m != '\n':
        address += ' ' + m
    print('Введите сумму долга')
    sum = input()
    print('Введите начало периода')
    begin = input()
    print('Введите конец периода')
    end = input()
    doc = DocxTemplate(file_name)
    if float(sum) >= 20001:
        poshl = 400 + (float(sum) - 20000) * 0.015
        if (poshl % 1) * 10 >= 5:
            poshl = int((poshl - (poshl % 1)) + 1)
        else:
            poshl = int(poshl)
    else:
        poshl = float(sum) * 0.02
        if (poshl % 1) * 10 >= 5:
            poshl = int((poshl - (poshl % 1)) + 1)
        else:
            poshl = int(poshl)
        if poshl < 200:
            poshl = 200
    if ndol == 1:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'place': place,
            'ser': ser,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 2:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'place': place,
            'place2': place2,
            'ser': ser,
            'ser2': ser2,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 3:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'place': place,
            'place2': place2,
            'place3': place3,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 4:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 5:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 6:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 7:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 8:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 9:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 10:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 11:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'name11': name11,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'date11': date11,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'place11': place11,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'ser11': ser11,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 12:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'name11': name11,
            'name12': name12,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'date11': date11,
            'date12': date12,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'place11': place11,
            'place12': place12,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'ser11': ser11,
            'ser12': ser12,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 13:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'name11': name11,
            'name12': name12,
            'name13': name13,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'date11': date11,
            'date12': date12,
            'date13': date13,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'place11': place11,
            'place12': place12,
            'place13': place13,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'ser11': ser11,
            'ser12': ser12,
            'ser13': ser13,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 14:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'name11': name11,
            'name12': name12,
            'name13': name13,
            'name14': name14,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'date11': date11,
            'date12': date12,
            'date13': date13,
            'date14': date14,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'place11': place11,
            'place12': place12,
            'place13': place13,
            'place14': place14,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'ser11': ser11,
            'ser12': ser12,
            'ser13': ser13,
            'ser14': ser14,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    elif ndol == 15:
        context = {
            'num': str(num),
            'poshl': (str(round(poshl, 2)) + ' руб.'),
            'name': name,
            'name2': name2,
            'name3': name3,
            'name4': name4,
            'name5': name5,
            'name6': name6,
            'name7': name7,
            'name8': name8,
            'name9': name9,
            'name10': name10,
            'name11': name11,
            'name12': name12,
            'name13': name13,
            'name14': name14,
            'name15': name15,
            'rayon': rayon,
            'address': address,
            'sum': str(sum),
            'begin': begin,
            'end': end,
            'date': date,
            'date2': date2,
            'date3': date3,
            'date4': date4,
            'date5': date5,
            'date6': date6,
            'date7': date7,
            'date8': date8,
            'date9': date9,
            'date10': date10,
            'date11': date11,
            'date12': date12,
            'date13': date13,
            'date14': date14,
            'date15': date15,
            'place': place,
            'place2': place2,
            'place3': place3,
            'place4': place4,
            'place5': place5,
            'place6': place6,
            'place7': place7,
            'place8': place8,
            'place9': place9,
            'place10': place10,
            'place11': place11,
            'place12': place12,
            'place13': place13,
            'place14': place14,
            'place15': place15,
            'ser': ser,
            'ser2': ser2,
            'ser3': ser3,
            'ser4': ser4,
            'ser5': ser5,
            'ser6': ser6,
            'ser7': ser7,
            'ser8': ser8,
            'ser9': ser9,
            'ser10': ser10,
            'ser11': ser11,
            'ser12': ser12,
            'ser13': ser13,
            'ser14': ser14,
            'ser15': ser15,
            'plat': plat,
            'dplat': dplat,
            'lschet': lschet,
            'family': family,
            'fam': (fam[1][0] + '.' + fam[2][0] + '.' + fam[0]),
            'index': index,
            'site': site
        }
    doc.render(context)
    fine = input('Введите имя, под которым сохранить документ\n')
    if rayon == '':
        print('Участок не определился')
    doc.save(fine)


main()
