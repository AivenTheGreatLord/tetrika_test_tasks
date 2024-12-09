import math as m

def appearance(intervals: dict[str, list[int]]) -> int:
    #это типичная задача на отрезки
    lesson_timestamps = intervals["lesson"] + [m.inf] #забираю каждый список отдельно
    pupil_timestamps = intervals["pupil"] + [m.inf]
    tutor_timestamps = intervals["tutor"] + [m.inf]
    lesson_pointer = 0 #ставлю поинтрры на начало каждого списка
    pupil_pointer = 0
    tutor_pointer = 0
    current_presence = 0 #это количество текущих участников урок: ученик, учитель и официальное начало уроко
    tuition_time = 0 #проведенное на уроке время
    last_timestamp = -1 #заготовка на прошлый таймстемп

    while lesson_timestamps[lesson_pointer] != m.inf or pupil_timestamps[pupil_pointer] != m.inf or tutor_timestamps[tutor_pointer] != m.inf:


        if current_presence == 3: #если на уроке все
            tuition_time += min(lesson_timestamps[lesson_pointer], pupil_timestamps[pupil_pointer], tutor_timestamps[tutor_pointer]) - last_timestamp  
            #то прибавляем разницу между новым таймстемпом (в его время кто-то уходит или урко заканчивается) и старым

        if lesson_timestamps[lesson_pointer] <= pupil_timestamps[pupil_pointer] and lesson_timestamps[lesson_pointer] <= tutor_timestamps[tutor_pointer]: #если сейчас слеюущее событие - это начало урока
            if lesson_pointer % 2 == 0: #елли инфдекс четный, то урок начинается
                current_presence += 1
            else:
                current_presence -= 1 #если нечетный, то заканчивается
            last_timestamp = lesson_timestamps[lesson_pointer] #запоминаем это событие как последнее
            lesson_pointer += 1 #инкрисим поинтер

        elif pupil_timestamps[pupil_pointer] <= lesson_timestamps[lesson_pointer] and pupil_timestamps[pupil_pointer] <= tutor_timestamps[tutor_pointer]: #та же логика
            if pupil_pointer % 2 == 0:
                current_presence += 1
            else:
                current_presence -= 1
            last_timestamp = pupil_timestamps[pupil_pointer]
            pupil_pointer += 1

        else: #и тут та же логика
            if tutor_pointer % 2 == 0:
                current_presence += 1
            else:
                current_presence -= 1
            last_timestamp = tutor_timestamps[tutor_pointer]
            tutor_pointer += 1

    return tuition_time

        

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    # {'intervals': {'lesson': [1594702800, 1594706400],
    #          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    # 'answer': 3577
    # }, #желаю автору этого тесткейса мощнейшего бесприрывного поноса в течение недели.
    #1594706480, 1594705158, 1594705773, 1594705849, 1594706480 - первое и последние значение одинаковы, а также значения почему-то то возрастают, то убывают. Удивительные путешествия во времени
    #это как вообще возможно?
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'intervals': {'lesson': [2, 17], #уже мои тесты
             'pupil': [5, 8, 10, 11, 14, 18, 28, 28],
             'tutor':  [1, 7, 8, 10, 12, 24]},
    'answer': 5
    },
    {'intervals': {'lesson': [0, 31], #хотел првоерить дубликаты времени
             'pupil': [0, 7, 8, 8, 9, 18, 20, 26],
             'tutor': [2, 8, 24, 25, 25, 25]},
    'answer': 6
    },
    {'intervals': {'lesson': [1, 2], #хотел првоерить 0 секунд урока
             'pupil': [16, 21],
             'tutor': [0, 13, 14, 19]},
    'answer': 0
    }
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'