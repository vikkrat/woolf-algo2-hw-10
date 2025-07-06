from task_1_quicksort.quicksort_analysis import test_quick_sorts
from task_2_greedy_schedule.greedy_schedule import create_schedule, Teacher

def run_all():
    print("\n=== ТЕСТУВАННЯ QUICK SORT ===")
    test_quick_sorts()
    print("\n=== ТЕСТУВАННЯ ЖАДІБНОГО РОЗКЛАДУ ===")
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]
    schedule = create_schedule(subjects, teachers)
    if schedule:
        for t in schedule:
            print(f"{t.first_name} {t.last_name} -> {t.assigned_subjects}")
    else:
        print("Неможливо покрити всі предмети.")

if __name__ == "__main__":
    run_all()
