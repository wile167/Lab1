def run_task1():
    print("=== Завдання 1. Списки: індексація, зрізи та мутації ===")
    
    # 1. Початкові дані (детерміновано)
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"Початковий список: {numbers} (довжина: {len(numbers)})\n")
    
    # 2. Звернення за індексами
    print(f"Елемент за додатним індексом [2]: {numbers[2]}")
    print(f"Елемент за від'ємним індексом [-2]: {numbers[-2]}\n")
    
    # 3. Три різні зрізи (один з кроком != 1)
    print(f"Зріз 1 (з 2 по 6): {numbers[2:6]}")
    print(f"Зріз 2 (перші 5): {numbers[:5]}")
    print(f"Зріз 3 (з кроком 2): {numbers[1:9:2]}\n")
    
    # 4. Мутації «на місці» з діагностикою довжини
    numbers.append(110)
    print(f"Після append(110): {numbers} | Довжина: {len(numbers)}")
    
    numbers.insert(0, 5)
    print(f"Після insert(0, 5): {numbers} | Довжина: {len(numbers)}")
    
    numbers[2:4] = [25, 35]
    print(f"Після заміни [2:4]: {numbers} | Довжина: {len(numbers)}")
    
    numbers.remove(110)
    print(f"Після remove(110): {numbers} | Довжина: {len(numbers)}\n")

if __name__ == "__main__":
    run_task1()