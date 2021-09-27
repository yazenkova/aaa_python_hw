from pyowm.owm import OWM
import time
from random import choices, choice
from PIL import Image


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


# влажность воздуха, на основе которой будем предсказывать осадки
def get_humidity():
    owm = OWM('584fe9e12a0d09ecd3d724add7a46a32')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Saint Petersburg,RU')
    weather = observation.weather
    return weather.humidity / 100


def step2_umbrella():
    humidity = get_humidity()
    rain_on_the_way = choices([0, 1], [1 - humidity, humidity], k=10)

    good_weather = [
        'Отличная погода, самое время прогуляться',
        'Как прекрасно на улице, можно и круг по дороге сделать',
        'Пока и тучек не видать, может и пронесет',
    ]

    good_weather_after_rain = [
        'Вот и распогодилось, даже посвежее стало',
        'Как здорово, все тучки мигом исчезли',
    ]

    rainy_weather = [
        'Ой, вот и дождь пошел, хорошо, что зонтик взяли',
        'Вот это ливень зарядил, хоть зонтик с собой есть',
        'Вот и капли на асфальте появились, пора доставать зонт',
    ]

    rainy_weather_after_rain = [
        'Радуга появилась, может скоро дождик закончится?',
        'Дождь все сильнее и сильнее, скоро придется плыть',
        'На улице темно, как глубокой ночью, еще и дождь сплошной стеной',
    ]

    was_rainy = False

    for i, step in enumerate(rain_on_the_way):
        print('Прошли ', (i + 1) * 10, '% пути')
        if not step and not was_rainy:
            print(choice(good_weather))
        elif not step and was_rainy:
            print(choice(good_weather_after_rain))
            was_rainy = False
        elif step and not was_rainy:
            print(choice(rainy_weather))
            was_rainy = True
        elif step and was_rainy:
            print(choice(rainy_weather_after_rain))
        time.sleep(2)

    if sum(rain_on_the_way) > 7:
        print('''А погода оказалась не сахар, и даже зонтик не сильно помог :(
Утка в итоге дошла до бара, но на следующее утро простудилась''')
        # если хочется посомтреть на картинку, можно раскомментировать
        # img = Image.open('flew_donald_duck.jpeg')
        # img.show()
    else:
        print('Утка дошла до бара в прекрасном настроении и весело провела вечер!')
        # если хочется посомтреть на картинку, можно раскомментировать
        # img = Image.open('donald_duck_drunk.jpeg')
        # img.show()


def step2_no_umbrella():
    humidity = get_humidity()
    rain_on_the_way = choices([0, 1], [1 - humidity, humidity], k=10)

    good_weather = [
        'Отличная погода, самое время прогуляться',
        'Как прекрасно на улице, можно и круг по дороге сделать',
        'Пока и тучек не видать, может и пронесет',
    ]

    good_weather_after_rain = [
        'Вот и распогодилось, даже посвежее стало',
        'Как здорово, все тучки мигом исчезли',
    ]

    rainy_weather = [
        'Ой, дождик пошел, а отступать уже некуда, быстрее в бар!',
        'Что за капли на асфальте?! Неужели дождь начинается?',
        'Что-то небо все темное, надо было брать с собой зонт :(',
    ]

    rainy_weather_after_rain = [
        'Дождь все сильнее и сильнее, можно уже плыть по лужам',
        'Как же мы так зонт-то забыли? Придется отогреваться в баре горячим глинтвейном!',
    ]

    was_rainy = False

    for i, step in enumerate(rain_on_the_way):
        print('Прошли ', (i + 1) * 10, '% пути')
        if not step and not was_rainy:
            print(choice(good_weather))
        elif not step and was_rainy:
            print(choice(good_weather_after_rain))
            was_rainy = False
        elif step and not was_rainy:
            if i < 5:
                print('''Ой, дождь пошел, пришлось вернуться домой, а возвращаться уже поздно :(
Будем сидеть дома, смотреть на дождь и грустить...''')
                # если хочется посомтреть на картинку, можно раскомментировать
                # img = Image.open('donald_duck_sad.png')
                # img.show()
                return
            else:
                print(choice(rainy_weather))
                was_rainy = True
        elif step and was_rainy:
            print(choice(rainy_weather_after_rain))
        time.sleep(2)

    if sum(rain_on_the_way) >= 3:
        print('''Кое-как мы добежали до бара, но утка все же успела простыть!
Следующий день для нее был совсем не сахар :(''')
        # если хочется посомтреть на картинку, можно раскомментировать
        # img = Image.open('flew_donald_duck.jpeg')
        # img.show()
    else:
        print('Фух, да нам повезло, утка успела добежать до бара, не попав под дождь, и прекрасно провела время!')
        # если хочется посомтреть на картинку, можно раскомментировать
        # img = Image.open('donald_duck_drunk.jpeg')
        # img.show()


if __name__ == '__main__':
    step1()
