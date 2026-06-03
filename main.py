from read_file import read_tree_from_file,get_path_bottom_up

def main_menu():
    print('\nДобро пожаловать в программу! Вы предприниматель, и для получения лицензии Вам нужно получить подпись на документе у главного чиновника, пройдя через его подчиненных')
    print('Не забудьте сохранить текстовый файл input.txt с чиновниками в формате "Фамилия взятка Начальник". У главного начальника в третьем поле поставьте "-"')
    print("\n=== МИНИСТЕРСТВО ЧИНОВНИКОВ ===")
    print("1. Рассчитать минимальную сумму")
    print("2. Показать главного чиновника")
    print("0. Выход")
    
    choice = input("Выберите действие: ")
    return choice

if __name__ == "__main__":
    FILENAME = "input.txt"
    root = None
    officials_dict = {}
    is_calculated = False
    
    while True:
        try:
            choice = main_menu()
            
            if not officials_dict and choice != '0':
                try:
                    officials_dict,root = read_tree_from_file(FILENAME)
                except Exception as e:
                    print(f"❌ Ошибка загрузки файла: {e}")
                    continue

            if choice == '1':
                if root:
                    root.calculate_min_cost()
                    is_calculated = True
                    print(f"\n► Минимальная сумма: {root.min_cost} у.е.")
                    
                    path = get_path_bottom_up(root)
                    print(f"► Порядок получения подписей: {' -> '.join(path)}")
                else:
                    print("❌ Данные не загружены.")
                

            elif choice == '2':
                if root:
                    print(f"\n► Главный чиновник: {root.name}")
                else:
                    print("❌ Данные не загружены.")

                    
            elif choice == '0':
                print("До свидания!")
                break
            else:
                print("❌ Неверный ввод. Попробуйте снова.\n")
            
                
        except KeyboardInterrupt:
            print("\nПрограмма была прервана. До свидания!")
            break
        except Exception as e:
            print(f"❌ Ошибка: {e}")