label early_bad_ending:
    play music breeze
    a "{i}(Такая ответственность... Не хочу их подводить.){/i}"
    
    show andrey sigh
    a "Простите, ребят. Мне кажется, я пока не готов к такой ответственности."

    show lena sad
    show dima sad
    show maxim sad
    show julia sad
    show kostya sad
    m "Ладно. В любом случае спасибо за советы, которые ты нам дал!"
    a "Удачи вам."

    scene black
    centered "Андрей вернулся к учёбе."
    centered "Время близилось к выпуску, а он так и не понял, чем бы хотел заниматься в жизни."
    centered "День за днём Максим становился всё мрачнее."
    hide black

    show living room
    show black:
        alpha 0.5
    centered "Месяцем позже. Квартира Максима и Андрея."

    scene living room
    show andrey normal at left2
    a "..."

    play sound door_closed

    show maxim sad at right2
    a "О, привет!"
    m "Привет..."
    
    show maxim cry
    m "Всё-таки у меня не получилось. Проект провалился..."
    
    show andrey sad
    a "Мне очень жаль..."
    a "{i}(Интересно, как бы всё сложилось, если бы я согласился...){/i}"

    jump credits

label ending_beginning:
    scene office openspace
    show black:
        alpha 0.5
    centered "Спустя две с половиной недели"
    centered "Офис инвесторов"

    scene office openspace

    show lena normal at left
    show dima normal at left2
    show andrey normal at left1
    show maxim normal at right1
    show julia normal at right2
    show kostya normal at right

    m "Для начала хочу вас всех поздравить со сдачей проекта!"

    return

label reflection_beginning:
    scene work
    show black:
        alpha 0.5
    centered "Этим же вечером"
    scene work

    show andrey sigh
    a "{i}(Фух.. Ну и месяцок выдался.){/i}"
    
    show andrey normal
    a "{i}(Тем не менее... Мой первый в жизни проект сдан!){/i}"

    return


label ending_1:
    play music familiar_places fadein 2.0

    call ending_beginning from _call_ending_beginning
    
    show kostya happy
    show lena happy
    show dima happy
    show julia happy
    m "Нам удалось создать хороший стабильный продукт."

    m "Пусть инвесторы и поворчали на ограниченность функционала, мне удалось их убедить, что, для такой команды как мы, это не проблема."

    show maxim happy
    show andrey happy
    m "Нам увеличили финансирование, и вообще возлагают на нас большие надежды."
    m "Вперёд, команда, покажем на что мы способны!"
    e "УРА!"

    call reflection_beginning from _call_reflection_beginning

    show andrey happy
    a "{i}(Всё обернулось так хорошо, даже удивительно...){/i}"
    a "{i}(Сам процесс принёс мне кучу удовольствия, хоть и был довольно напряжённым.){/i}"
    a "{i}(Я чувствую, что наконец-то сделал что-то полезное!){/i}"
    a "{i}(Кажется, я нашёл, чем хочу заниматься в своей жизни.){/i}"

    jump credits

label ending_2:
    play music familiar_places fadein 2.0

    call ending_beginning from _call_ending_beginning_1
    
    show kostya happy
    show lena happy
    show dima happy
    m "Нам удалось создать хороший продукт."

    show julia sad
    m "К сожалению, пользователи часто жалуются на баги."
    m "Однако критических среди них нет, это радует."
    
    show julia normal
    m "К тому же мы только запустились, с кем не бывает."

    show julia happy
    show maxim happy
    show andrey happy
    m "Нам сильно увеличили финансирование, и вообще возлагают на нас большие надежды."
    m "Вперёд, команда, покажем на что мы способны!"
    e "УРА!"

    call reflection_beginning from _call_reflection_beginning_1

    show andrey happy
    a "{i}(Всё обернулось так хорошо, даже удивительно...){/i}"
    a "{i}(Сам процесс принёс мне кучу удовольствия, хоть и был довольно напряжённым.){/i}"

    show andrey sigh
    a "Даже несмотря на то, что пользователи жалуются на баги..."
    
    show andrey happy
    a "{i}(Я чувствую, что наконец-то сделал что-то полезное!){/i}"
    a "{i}(Кажется, я нашёл, чем хочу заниматься в своей жизни.){/i}"

    jump credits

label ending_3:   
    play music familiar_places fadein 2.0
    
    call ending_beginning from _call_ending_beginning_2

    show dima happy
    show lena happy
    show kostya happy
    m "Несмотря на трудности, с которыми мы столкнулись, мы дошли до финала."

    show julia sad
    m "К сожалению, пользователи часто жалуются на баги."

    show andrey sad
    show maxim sad
    show dima sad
    show kostya sad
    show lena sad
    m "Инвесторы остались очень недовольны уменьшением функционала, из-за этого урезали нам бюджет."
    m "Однако, они всё ещё верят в наш проект и готовы дать нам время на исправление ситуации."

    show dima happy
    show kostya happy
    d "Что ж, по крайней мере, всё не так уж и плохо, можно выдохнуть. Выше нос!"

    show lena happy
    show julia happy
    j "Да, покажем им на что мы способны! Выкатим такую обнову, что они закачаются!"

    show andrey happy
    show maxim happy
    a "С такой-то классной командой? Естественно у нас всё будет круто!"
    
    call reflection_beginning from _call_reflection_beginning_2

    show andrey sad
    a "{i}(Столько багов, ещё и финансирование сократили...){/i}"
    a "{i}(Непростая это работа.){/i}"

    show andrey normal
    a "{i}(В любом случае... Это ли не повод совершенствоваться?! Если я и дальше продолжу, то смогу делать действительно классные вещи со своей командой.){/i}"
    a "{i}(Быть может, это и есть дело моей жизни?){/i}"
    
    jump credits

label ending_4:
    play music breeze fadein 2.0
    
    call ending_beginning from _call_ending_beginning_3

    m "Нам удалось создать хороший стабильный продукт."
    
    show maxim happy
    m "Нам сильно увеличили финансирование, и вообще возлагают на нас большие надежды."

    show maxim sad
    m "..."

    show kostya sad
    show lena sad
    show julia sad
    show dima sad
    show andrey sad
    e "..."

    d "Не знаю, Макс, останусь ли я с вами дальше."
    d "Как минимум ищи второго разраба."
    l "Кажется, у меня произошло выгорание. Я буду рада остаться, но мне нужно отдохнуть..."
    j "Та же штука."

    m "Вот как..."
    m "Не переживайте, можете хорошо отдохнуть, с остальным я разберусь. Даю слово."
    
    show kostya normal
    show dima normal
    show maxim normal
    show lena normal
    show julia normal
    show andrey think
    m "Мы – команда. Прорвёмся."
  
    call reflection_beginning from _call_reflection_beginning_3
    
    show andrey sad
    a "{i}(Кажется, я облажался.){/i}"
    a "{i}(Да, проект вышел, но какой ценой?){/i}"
    a "{i}(Максим ничего плохого мне не говорил, но я чувствую, что на произошедшем лежит только моя вина.){/i}"
    
    show andrey sigh
    a "{i}(Не знаю, стоит ли продолжать этот путь дальше...){/i}"

    jump credits

label credits:
    scene black with fade

    centered "Работу выполнил студент первого курса\nМурашев Иван Андреевич"
    centered """
    В проекте использованы работы\n
    Alexandra Gorn\n
    Christopher Gower\n
    Matt Hoffman\n
    Farzad\n
    Jason Goodman\n
    Mikey Harris\n
    lsa Noblet\n
    Alexandru Acea\n
    по лицензии Unsplash
    """

    centered """
    В проекте использована музыка\n
    Feeling Good by Pufino\n
    Animal Friends by Lukrembo\n
    Lamp by Lukrembo\n
    familiar places by massobeats\n
    breeze by massobeats\n
    по лицензии {a=https://freetouse.com/music}freetouse.com{/a}
    """

    stop music fadeout 2.0

    centered "конец"