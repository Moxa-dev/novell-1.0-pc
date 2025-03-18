label act_3_2:
    play music feeling_good fadein 2.0

    scene office
    show black:
        alpha 0.5
    centered "Через две недели"
    centered "14 дней до сдачи проекта"

    scene office
    
    show lena normal at left
    show dima normal at left2
    show andrey normal at left1
    show maxim normal at right1
    show julia normal at right2
    show kostya normal at right

    m "Отлично, все в сборе."
    m "Я вернулся со встречи с инвесторами."
    m "Как вы помните, до сдачи проекта у нас две недели."
    
    show andrey happy
    m "Для начала. Инвесторы оказались довольны новым подходом Андрея."

    show maxim happy
    m "Да и что уж говорить, мне тоже стало куда удобнее отчитываться. Красавчик, Андрюха!"

    show maxim normal
    show andrey think
    show dima sad
    show lena sad
    show julia sad
    show kostya sad
    m "Из плохого.. Похоже, что мы не успеваем реализовать весь запланированный функционал."
    m "Их очень беспокоит возможность его сокращения, они хотят охватить как можно больше потребностей пользователей."

    k "И вот мы снова стоим перед выбором между функционалом и временем."
    d "Нужно ещё сократить наш MVP. Иначе пострадает стабильность."
    j "Либо придётся поработать больше перед релизом..."
    d "Но-но, на сверхурочную работу я не подписывался уж точно."
    a "Максим, может инвесторы согласятся сдвинуть сроки релиза?"
    
    show maxim sad
    m "Исключено. Они твёрдо дали это понять."

    stop music fadeout 2.0

    menu:
        m "Решение за тобой, капитан"

        "Сократим функционал":
            jump sacrifice_features
        "Поработаем сверхурочно":
            jump work_overtime

label sacrifice_features:
    play music feeling_good fadein 2.0

    show andrey normal
    show maxim normal
    show dima normal
    show lena normal
    show julia normal
    show kostya normal
    a "Сделаем меньше, но лучше. Инвесторы поймут, я уверен. Ты сможешь их убедить со своим красноречием."

    show maxim happy
    m "Сделаю всё возможное и невозможное!"

    a "Что ж, объявляю мозговой штурм..."
    
    stop music fadeout 2.0

    "..."

    jump ending_3

label work_overtime:
    play music feeling_good fadein 2.0

    show andrey sigh
    a "Потерять финансирование сейчас хочется меньше всего."

    stop music fadeout 2.0

    show lena sad
    show maxim sad
    show dima annoyed
    show kostya normal
    show julia sad
    a "Пусть нам придётся поработать сверхурочно, но я уверен, что результат будет того стоить. Отдохнём после релиза..."

    jump ending_4