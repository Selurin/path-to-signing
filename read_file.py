import os
from logic import Official

def read_tree_from_file(filename):
    """Читает данные из файла и строит дерево чиновников"""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл {filename} не найден!")

    officials = {}
    root = None
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 3:
            continue 
            
        name = parts[0]
        try:
            bribe = int(parts[1])
        except ValueError:
            print(f"Некорректная взятка у {name}")
            continue
            
        boss_name = parts[2]
        
        if name not in officials:
            officials[name] = Official(name, bribe)
        else:
            officials[name].bribe = bribe
            
        if boss_name == '-':
            root = officials[name]
        else:
            if boss_name not in officials:
                officials[boss_name] = Official(boss_name, 0)

            officials[boss_name].add_subordinate(officials[name])

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