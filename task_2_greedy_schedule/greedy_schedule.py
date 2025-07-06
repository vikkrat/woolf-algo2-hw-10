import os
import matplotlib.pyplot as plt

# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    schedule = []

    while uncovered:
        best = None
        best_covers = set()

        for teacher in teachers:
            can_cover = teacher.can_teach_subjects & uncovered
            if len(can_cover) > len(best_covers) or (
                len(can_cover) == len(best_covers) and (best is None or teacher.age < best.age)
            ):
                best = teacher
                best_covers = can_cover

        if not best_covers:
            return None

        best.assigned_subjects = best_covers
        uncovered -= best_covers
        schedule.append(best)

    return schedule

if __name__ == "__main__":
    # Вхідні дані
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
        print("Розклад занять:")
        for t in schedule:
            print(f"{t.first_name} {t.last_name}, {t.age} років, email: {t.email}")
            print(f"   Викладає предмети: {', '.join(t.assigned_subjects)}\n")

        # Візуалізація результату
        os.makedirs("screenshots", exist_ok=True)
        names = [f"{t.first_name} {t.last_name}" for t in schedule]
        counts = [len(t.assigned_subjects) for t in schedule]

        plt.figure(figsize=(8, 5))
        plt.bar(names, counts)
        plt.xlabel("Викладачі")
        plt.ylabel("Кількість предметів")
        plt.title("Розподіл предметів між викладачами")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("screenshots/schedule_output.png")
        plt.show()
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
