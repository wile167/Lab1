def normalize_text(text: str) -> list[str]:
    """Очищення тексту та розбиття на слова."""
    for char in ".,!?:;—":
        text = text.replace(char, "")
    return text.lower().split()

def run_task3():
    print("=== Завдання 3. Словники та облік частот / довідників ===")
    
    sample_text = "Python це чудова мова. Мова Python дозволяє швидко писати ефективний код."
    words = normalize_text(sample_text)
    
    # Підрахунок частот слів
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
        
    print("1. Частота слів (відсортовано за спаданням):")
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_freq:
        print(f"   {word:<10}: {count}")
        
    # Dict comprehension для відбору слів із частотою >= 2
    filtered_dict = {w: c for w, c in freq_dict.items() if c >= 2}
    print(f"\n2. Похідний словник (частота >= 2): {filtered_dict}\n")

if __name__ == "__main__":
    run_task3()