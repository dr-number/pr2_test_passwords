import math

def default_input(text: str, default_value: str) -> str:
    inp = input(f"{text} [{default_value}]: ")
    if not inp:
        return default_value
    
    return inp


def format_time(seconds):
    """Convert seconds to human readable format"""
    if seconds < 60:
        return f"{seconds:.2f} сек"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f} мин"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f} ч"
    elif seconds < 31536000:  # 365 дней
        days = seconds / 86400
        return f"{days:.2f} дн"
    else:
        years = seconds / 31536000
        return f"{years:.2f} лет"
    
def format_time_detailed(seconds):
    """Convert seconds to detailed format: days, hours, minutes, seconds"""
    if seconds < 0:
        return "0 сек"
    
    # Целое количество секунд
    total_seconds = int(seconds)
    
    years = total_seconds // 31536000  # 365 дней
    remaining = total_seconds % 31536000
    
    days = remaining // 86400
    remaining = remaining % 86400
    
    hours = remaining // 3600
    remaining = remaining % 3600
    
    minutes = remaining // 60
    secs = remaining % 60
    
    # Формируем строку результата
    parts = []
    
    if years > 0:
        parts.append(f"{years} {'год' if years == 1 else 'года' if 2 <= years <= 4 else 'лет'}")
    if days > 0:
        parts.append(f"{days} {'день' if days == 1 else 'дня' if 2 <= days <= 4 else 'дней'}")
    if hours > 0:
        parts.append(f"{hours} {'час' if hours == 1 else 'часа' if 2 <= hours <= 4 else 'часов'}")
    if minutes > 0:
        parts.append(f"{minutes} {'минута' if minutes == 1 else 'минуты' if 2 <= minutes <= 4 else 'минут'}")
    if secs > 0 or not parts:  # добавляем секунды, если есть или если других единиц нет
        parts.append(f"{secs} {'секунда' if secs == 1 else 'секунды' if 2 <= secs <= 4 else 'секунд'}")
    
    return ", ".join(parts)

def task1():
    """Задача 1: Интерактивный режим с паузами"""
    print("\n" + "="*60)
    print("ЗАДАЧА 1: Интерактивный режим (с паузами после неудачных попыток)")
    print("="*60)
    
    n = int(default_input("Введите количество символов в алфавите (n): ", "11"))
    k = int(default_input("Введите длину пароля (k): ", "7"))
    s = float(default_input("Введите скорость перебора (паролей/сек): ", "50"))
    m = int(default_input("Введите количество неправильных попыток до паузы (m): ", "7"))
    v = float(default_input("Введите длительность паузы (сек): ", "12"))
    
    total_passwords = n ** k
    print(f"\nОбщее количество возможных паролей: {n}^{k} = {total_passwords:,}")
    
    # Время без пауз
    time_without_pause = total_passwords / s
    
    # Количество пауз
    num_pauses = total_passwords // m
    if total_passwords % m == 0:
        num_pauses -= 1  # последняя успешная попытка не требует паузы
    
    total_pause_time = num_pauses * v
    
    total_time = time_without_pause + total_pause_time
    
    print(f"\nРезультаты:")
    print(f"Время перебора всех паролей (без учета пауз): {format_time(time_without_pause)} ({format_time_detailed(time_without_pause)})")
    print(f"Общее время пауз: {format_time(total_pause_time)} ({format_time_detailed(total_pause_time)})")
    print(f"ИТОГОВОЕ ВРЕМЯ ПЕРЕБОРА: {format_time(total_time)}  ({format_time_detailed(total_time)})")

def task2():
    """Задача 2: Минимальная длина пароля для заданного времени"""
    print("\n" + "="*60)
    print("ЗАДАЧА 2: Определение минимальной длины пароля")
    print("="*60)
    
    n = int(default_input("Введите количество символов в алфавите (n): ", "11"))
    t = float(default_input("Введите требуемое время перебора (лет): ", "90"))
    s = float(default_input("Введите скорость перебора (паролей/сек): ", "50"))
    
    # Переводим годы в секунды
    total_seconds = t * 365 * 24 * 3600
    
    # Общее количество паролей = n^k
    # n^k >= s * total_seconds
    # k >= log(s * total_seconds) / log(n)
    
    required_passwords = s * total_seconds
    min_k = math.ceil(math.log(required_passwords) / math.log(n))
    
    # Проверяем, что получилось
    actual_passwords = n ** min_k
    actual_time = actual_passwords / s
    actual_time_years = actual_time / (365 * 24 * 3600)
    
    print(f"\nРезультаты:")
    print(f"Требуемое количество паролей для перебора: {required_passwords:.2e}")
    print(f"Минимальная длина пароля: {min_k} символов")
    print(f"Фактическое количество паролей: {actual_passwords:,}")
    print(f"Фактическое время перебора: {format_time(actual_time)} ({actual_time_years:.2f} лет) ({format_time_detailed(actual_time)})")

def task3():
    """Задача 3: Минимальная мощность алфавита"""
    print("\n" + "="*60)
    print("ЗАДАЧА 3: Определение минимальной мощности алфавита")
    print("="*60)
    
    k = int(default_input("Введите длину пароля (k): ", "11"))
    t = float(default_input("Введите требуемое время перебора (лет): ", "90"))
    s = float(default_input("Введите скорость перебора (паролей/сек): ", "50"))
    
    # Переводим годы в секунды
    total_seconds = t * 365 * 24 * 3600
    
    # n^k >= s * total_seconds
    # n >= (s * total_seconds)^(1/k)
    
    required_passwords = s * total_seconds
    min_n = math.ceil(required_passwords ** (1/k))
    
    # Проверяем
    actual_passwords = min_n ** k
    actual_time = actual_passwords / s
    actual_time_years = actual_time / (365 * 24 * 3600)
    
    print(f"\nРезультаты:")
    print(f"Требуемое количество паролей для перебора: {required_passwords:.2e}")
    print(f"Минимальная мощность алфавита: {min_n} символов")
    print(f"Фактическое количество паролей: {actual_passwords:,}")
    print(f"Фактическое время перебора: {format_time(actual_time)} ({actual_time_years:.2f} лет) ({format_time_detailed(actual_time)})")

def main():
    print("\n" + "="*60)
    print("РАСЧЕТ ПАРАМЕТРОВ ПАРОЛЬНОЙ СИСТЕМЫ ЗАЩИТЫ")
    print("="*60)
    
    while True:
        print("\nВыберите задачу:")
        print(
            "1 - Определить время перебора всех паролей с учетом пауз после неудачных попыток ввода (интерактивный режим).\n"
            "Определить время перебора всех паролей с параметрами. Алфавит состоит из n символов.\n"
            "Длина пароля символов k. Скорость перебора s паролей в секунду. После каждого из m неправильно введенных паролей идет пауза в v секунд.\n\n"
        )
        print(
            "2 - Определить минимальную длину пароля, обеспечивающую заданное время перебора (неинтерактивный режим).\n"
            "Определить минимальную длину пароля, алфавит которого состоит из n символов, время перебора которого было не меньше t лет. Скорость перебора s паролей в секунду.\n\n"
        )
        print(
            "3 - Определить минимальную мощность алфавита (количество символов), обеспечивающую заданное время перебора при фиксированной длине пароля.\n"
            "Определить количество символов алфавита, пароль состоит из k символов, время перебора которого было не меньше t лет. Скорость перебора s паролей в секунду.\n\n"
        )
        print("4 - Выполнить все задачи")
        print("0 - Выход")
        
        choice = input("\nВаш выбор: ")
        
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            print("\n" + "="*60)
            print("ВЫПОЛНЕНИЕ ВСЕХ ЗАДАЧ")
            print("="*60)
            
            # Общий ввод данных
            print("\n--- Ввод общих данных ---")
            n = int(input("Введите количество символов в алфавите (n): "))
            k = int(input("Введите длину пароля (k): "))
            s = float(input("Введите скорость перебора (паролей/сек): "))
            t = float(input("Введите требуемое время перебора (лет): "))
            m = int(input("Введите количество неправильных попыток до паузы (m): "))
            v = float(input("Введите длительность паузы (сек): "))
            
            print("\n" + "="*60)
            print("ЗАДАЧА 1")
            print("="*60)
            total_passwords = n ** k
            time_without_pause = total_passwords / s
            num_pauses = total_passwords // m
            if total_passwords % m == 0:
                num_pauses -= 1
            total_pause_time = num_pauses * v
            total_time = time_without_pause + total_pause_time
            
            print(f"Общее количество паролей: {total_passwords:,}")
            print(f"Время без пауз: {format_time(time_without_pause)} ({format_time_detailed(time_without_pause)})")
            print(f"Время пауз: {format_time(total_pause_time)} ({format_time_detailed(total_pause_time)})")
            print(f"ИТОГО: {format_time(total_time)} ({format_time_detailed(total_time)})")
            
            print("\n" + "="*60)
            print("ЗАДАЧА 2")
            print("="*60)
            total_seconds = t * 365 * 24 * 3600
            required_passwords = s * total_seconds
            min_k = math.ceil(math.log(required_passwords) / math.log(n))
            print(f"Минимальная длина пароля: {min_k} символов")
            
            print("\n" + "="*60)
            print("ЗАДАЧА 3")
            print("="*60)
            min_n = math.ceil(required_passwords ** (1/k))
            print(f"Минимальная мощность алфавита: {min_n} символов")
            
        elif choice == '0':
            break
        else:
            print("\nНеверный выбор. Пожалуйста, попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
