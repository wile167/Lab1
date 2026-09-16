def run_task4():
    print("=== Завдання 4. Множини: унікальність та операції над наборами ===")
    
    list_a = ["ID101", "ID102", "ID103", "ID104", "ID101"]
    list_b = ["ID103", "ID104", "ID105", "ID106"]
    list_c = ["ID101", "ID102"]
    
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set(list_c)
    
    print(f"Множина A: {sorted(set_a)}")
    print(f"Множина B: {sorted(set_b)}")
    print(f"Множина C: {sorted(set_c)}\n")
    
    print(f"Перетин (A ∩ B): {sorted(set_a & set_b)}")
    print(f"Об'єднання (A ∪ B): {sorted(set_a | set_b)}")
    print(f"Симетрична різниця (A △ B): {sorted(set_a ^ set_b)}\n")
    
    print(f"Чи є C підмножиною A (C <= A)? {set_c <= set_a} (True)")
    print(f"Чи є B підмножиною A (B <= A)? {set_b <= set_a} (False)\n")

if __name__ == "__main__":
    run_task4()