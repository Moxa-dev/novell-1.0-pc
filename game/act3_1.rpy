label act_3_1:
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
    m "Из плохого.. Инвесторы остались недовольны скудным функционалом приложения."
    m "Они хотят охватить как можно больше потребностей пользователей."
    k "Создать решение для всего и сразу в такой короткий срок?"
    d "Ну и тупость."
    d "Мы ведь даже ещё не до конца реализовали основные функции. Да и баги не все пофиксили..."
    
    show maxim sad
    m "Они считают, что двух недель более, чем достаточно."
    
    show dima annoyed
    d "А я считаю в столбик!"

    show maxim angry
    m "Дима!"

    show dima normal
    show maxim normal
    d "Извини."

    a "Ребята правы, если добавлять ещё функций мы пожертвуем стабильностью."
    a "Но если будем игнорировать пожелания инвесторов, то рискуем остаться без финансирования."
    a "Как думаешь, Максим, у тебя получится договориться с инвесторами и объяснить им нашу позицию?"

    show lena normal
    show julia normal
    show kostya normal
    show maxim sad
    m "Я не знаю. Могу попробовать."
    
    show andrey happy
    a "Да ладно, я ж тебя знаю, ты любого уговоришь."
    
    show maxim happy
    m "Ха-ха. Ладно, они были не настолько категоричны, да и всё ещё доверяют нашим решениям."

    show maxim normal
    show andrey normal
    
    stop music fadeout 2.0 

    menu:
        a "Что ж..."
        "Объясним инвесторам необходимость такого решения":
            jump choose_explain
        "У нас ещё есть время на пару новых функций":
            jump choose_features
        
label choose_explain:
    play music feeling_good fadein 2.0

    show andrey happy
    show maxim happy
    show dima happy
    show lena happy
    show julia happy
    show kostya happy
    a "В таком случае я рассчитываю на твоё красноречие, босс!"
    
    stop music fadeout 2.0

    m "Будет сделано, капитан!"

    jump ending_1

label choose_features:
    play music feeling_good fadein 2.0

    a "Потерять финансирование сейчас хочется меньше всего."
    a "Я думаю, что мы не много потеряем от пары-тройки функций, зато инвесторы будут довольны."

    show maxim happy
    m "Я рассчитываю на вас, ребята!"

    stop music fadeout 2.0

    d "Что ж, придётся поднапрячься..."

    jump ending_2