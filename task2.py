def print_student_info(record: tuple):
    """Розпакування кортежу та вивід даних."""
    surname, group, grades = record
    print(f"Студент: {surname:<10} | Група: {group} | Оцінки: {grades}")

def calculate_average(students: list[tuple]) -> float:
    """Обчислення середнього балу по всіх студентах."""
    all_grades = [grade for student in students for grade in student[2]]
    return round(sum(all_grades) / len(all_grades), 2)

def run_task2():
    print("=== Завдання 2. Кортежі та «розпакування» даних ===")
    
    students = [
        ("Шевченко", "КБ-21", [90, 85, 95]),
        ("Коваленко", "КБ-21", [75, 80, 70]),
        ("Бондаренко", "КБ-22", [92, 94, 89])
    ]
    
    print("1. Записи студентів:")
    for student in students:
        print_student_info(student)
        
    avg = calculate_average(students)
    print(f"\n2. Середній бал по всіх студентах: {avg} балів\n")
    
    print("3. Перевірка незмінності кортежу:")
    try:
        students[0][0] = "Мельник"
    except TypeError as e:
        print(f"   [Помилка] Кортеж іммутабельний: {e}")
        
    print("\n4. Зміна мутабельного елемента у кортежі (списку оцінок):")
    students[0][2].append(100)
    print(f"   Оновлений запис: {students[0]}\n")

if __name__ == "__main__":
    run_task2()