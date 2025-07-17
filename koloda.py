import random

# генерим колоду карт
def createDeck(is54):
    deck = list() # пока пустая колода карт
    suits = "♡♢♣♠" # все масти
    seniority = ("6", "7", "8", "9", "10", "J", "Q", "K", "A") # все значения карт
    if is54:
        seniority = ("2", "3", "4", "5") + seniority
        deck = ["RedJoker", "BlackJoker"]

    # создаем каждую карту (масть + значение)
    for senior in seniority: # проходимся по всем мастям
        for suit in suits: # проходимся по всем значениям
            card = suit + senior # создаем карту из масти и значения
            deck.append(card) # добавляем карту в колоду

    random.shuffle(deck) # рандомно перемешиваю колоду
    return deck

# я мешаю колоду
def shuffleBySerafim(deck):

    count = random.randint(3, 8) # сколько раз я буду перемешивать
    for i in range(count):

        # сначала беру от 22 до 27 карт включительно
        firstPick = random.randint(22, 27) 
        firstPicked = deck[:firstPick]
        deck = deck[firstPick:]
        deck = deck[::-1]
        firstPicked = firstPicked[::-1]

        # дальше скидываю все взятые карты за несколько сбросов
        while firstPicked:
            secPick = random.randint(5, 13) # сколько я карт скину при броске
            if secPick > len(firstPicked):
                secPick = len(firstPicked)

            # беру карты, которые буду скидывать и скидываю их :/
            secPicked = firstPicked[:secPick]
            firstPicked = firstPicked[secPick:]
            deck = secPicked + deck

    return deck[::-1]

# функция, чтобы сравнивать колоды
def compareDecks(deck1, deck2):
    for shift in range(36):
        deck2 = deck2[shift:] + deck2[:shift]
        
        count = 0
        countSenior = 0

        for j in range(36):
            if deck1[j] == deck2[j]:
                count += 1
        
        for j in range(36):
            if deck1[j][1:] == deck2[j][1:]:
                countSenior += 1

        print(f"Сдвиг влево: {shift}    Общих совпадений: {count}   Совпадений по значению: {countSenior}")

deck = createDeck(True)
print(*deck)

deck2 = shuffleBySerafim(deck)
print(*deck2)

compareDecks(deck, deck2)

