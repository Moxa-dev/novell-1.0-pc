label act_2:
    play music lamp fadein 2.0
    
    show work
    show black:
        alpha 0.5
    centered "На следующий день"
    centered "28 дней до сдачи проекта"

    scene work
    show andrey normal
    a "{i}(Что ж, пора начинать!){/i}"
    a "{i}(Надо обойти ребят и узнать, какие задачи сейчас перед ними стоят.){/i}"

    $ checked = {'dima': False, 'lena': False, 'julia': False}

    while not all(checked.values()):
        menu:
            a "{i}(К кому сходить?..){/i}"
            
            "К Диме" if not checked['dima']:
                $ checked['dima'] = True
                
                scene office dima
                
                show dima normal at left2
                show andrey normal at right2
                a "Хэй?"
                d "Привет."
                a "Можешь рассказать какие задачи у тебя?"
                d "Хах. Да их вагон и маленькая тележка."
                
                show dima sad
                d "Я же один разработчик. На мне и фичи и баги и UI."
                
                show dima normal
                show andrey think
                a "Да, без системы трудно. Я сейчас как раз собираю данные для трекера задач."
                d "О, наконец-то! Тогда записывай..."
                "Андрей записал какие задачи у Димы в планах, над чем он сейчас работает и какие уже выполнил."
                a "Спасибо! Скоро скину ссылку в чат. Заходи смотреть."
                
                show dima happy
                show andrey happy
                d "А ты деловой."
            
            "К Лене" if not checked['lena']:
                $ checked['lena'] = True
                
                scene office lena
                
                show lena normal at left2
                show andrey normal at right2
                a "Лен?"
                l "О, заходи. Что такое?"
                a "Введи в курс дела по своим задачам."
                l "Так, дай-ка свериться с блокнотом..."
                "Андрей записал задачи Лены, параллельно выслушав о муках творческого выбора и трендах современного дизайна."
                a "Отлично, спасибо."
                l "Обращайся!"
                a "Сделаю трекер и ссылку отправлю в чат, не пропусти!"
                
                show andrey happy
                show lena happy
                l "Хорошо-хорошо!"
            
            "К Юле" if not checked['julia']:
                $ checked['julia'] = True
                
                scene office julia
                show julia normal at left2
                show andrey normal at right2
                j "О, Андрюшка! Чем обязана?"
                a "Привет. Я записываю задачи для трекера. Расскажи о своих."
                j "Хм..."
                "Андрей записал задачи Юли. Кажется, она и правда обожает свою работу."
                j "Ну как-то так."
                a "Спасибо. Не забудь присоединиться к трекеру!"
                
                show julia happy
                show andrey happy
                j "Так точно, капитан!"

    a "{i}(Кажется всё...){/i}"
    
    scene work
    show andrey normal
    a "{i}(Пора разобраться с трекером!){/i}"
    "Спустя пол часа Андрей заполнил канбан-доску."
    
    show andrey think
    a "Ничего себе... Мне кажется, что тут не успеть за месяц всё сделать."
    a "Надо бы посоветоваться с командой."

label choose_strategy:
    show office
    show black:
        alpha 0.5
    centered "Офис, спустя 10 минут"
    
    scene office
    
    show andrey normal
    show kostya normal at left
    show dima normal at left2
    show julia normal at right2
    show lena normal at right
    a "Итак, я проанализировал наши задачи. По моим расчётам мы не успеем к дедлайну."
    a "У нас много задач, некоторые противоречат друг другу."
    a "Нужно определиться с тем, как мы решим эту проблему."
    d "Можем выбрать только то, что действительно нужно, а остальное принести в обновлениях."
    k "Да, так называемый MVP."
    l "Или скорректируем наши пожелания и сделаем что запланировали."
    j "Твоё слово, босс."
    
    show dima happy
    show kostya happy
    show lena happy
    show andrey happy
    a "Приятно слышать, что вы мне так доверяете."
    
    show andrey think
    show kostya normal
    show dima normal
    show lena normal
    show julia normal
    
    stop music fadeout 2.0

    menu:
        a "{i}(Как же мне поступить?){/i}"
        
        "Давайте выделим главные задачи и реализуем их хорошо":
            jump do_mvp
        
        "Скорректируем и выполним, что запланировали":
            jump do_all

label do_mvp:
    play music lamp fadein 2.0
    a "Выберем самое нужное и хорошо реализуем."
    d "Отлично!"
    k "Я подготовлю список самого необходимого."
    d "И без меня?"
    
    show kostya happy
    show dima happy
    k "Куда ж я денусь..."
    
    stop music fadeout 2.0
    
    show julia happy
    show lena happy
    show andrey happy
    a "Тогда решили. Вперёд, у нас есть все шансы на классный результат!"
    
    jump act_3_1

label do_all:
    play music lamp fadein 2.0
    a "Если подправим задачи, сможем и фичи реализовать и со сдачей не опоздать."
    k "Хорошо, я предлагаю следующие правки..."
    "Команда бурно обсудила список задач, избавившись от неопределённостей."
    
    stop music fadeout 2.0

    show andrey happy
    show kostya happy
    show lena happy
    show dima happy
    show julia happy
    a "Тогда решили. Вперёд, у нас ещё есть время!"
    
    jump act_3_2