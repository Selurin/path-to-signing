import os
from logic import Official

def read_tree_from_file(filename):
    """Читает данные из файла и строит дерево чиновников"""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден!")

    officials = {}
    #original_names = {}
    root = None
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    root_count = 0
    
    for i, line in enumerate(lines, 1):
        parts = line.strip().split()
        if len(parts) != 3:
            print(f'Недостает или слишком много данных в строке {i}. Пожалуйста, введите в формате "Фамилия взятка Начальник"')
            continue 
            
        name = parts[0]
        try:
            bribe = int(parts[1])
        except ValueError:
            print(f"Некорректная взятка у {name} в строке {i}")
            continue
        if bribe < 0:
            print(f"Некорректная взятка у {name} в строке {i}")
            continue
            
        boss_name = parts[2]

        name_lower = name.lower()
        
        if name_lower not in officials:
            officials[name_lower] = Official(name, bribe)
        else:
            officials[name_lower].bribe = bribe
            
        if boss_name == '-':
            root_count += 1
            if root_count > 1:
                raise ValueError("В файле главный чиновник должен быть только один (с символом '-')")
            root = officials[name_lower]
        else:
            boss_name_lower = boss_name.lower()
            if boss_name_lower not in officials:
                officials[boss_name_lower] = Official(boss_name, 0)
                #original_names[boss_name_lower] = boss_name

            officials[boss_name_lower].add_subordinate(officials[name_lower])

    if not officials:
        raise ValueError("Файл пуст или не содержит корректных данных")
    if not root:
        raise ValueError("В файле не указан главный чиновник (с символом '-')")
        
    return officials,root

def get_path_bottom_up(official):
    """
    Восстанавливает путь от подчиненного к главному.
    Возвращает список имен.
    """
    path = []
    current = official
    
    # Спускаемся вниз до самого последнего подчиненного
    while current is not None:
        path.append(current.name)
        current = current.best_subordinate
        
    # Сейчас путь: [Главный, ..., Последний]. Разворачиваем его.
    path.reverse()
    return path