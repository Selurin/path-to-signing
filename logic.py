class Official:
    def __init__(self, name, bribe):
        self.name = name
        self.bribe = bribe
        self.subordinates = []
        
        # Для хранения результатов расчета
        self.min_cost = 0
        self.chain_length = 0      # Количество человек в цепочке подписей
        self.best_subordinate = None # Ссылка на лучшего подчиненного для восстановления пути

    def add_subordinate(self, official):
        self.subordinates.append(official)

    def calculate_min_cost(self):
        """
        Рекурсивный расчет.
        Выбирает подчиненного с минимальной стоимостью.
        Если стоимости равны, выбирает того, у кого короче цепочка (меньше chain_length).
        """
        if not self.subordinates:
            # Лист дерева: платим только ему, длина цепочки 1
            self.min_cost = self.bribe
            self.chain_length = 1
            self.best_subordinate = None
        else:
            # Сначала рекурсивно считаем для всех детей
            for sub in self.subordinates:
                sub.calculate_min_cost()
            
            # Ищем лучшего подчиненного
            best_sub = None
            min_sub_cost = float('inf')
            min_sub_length = float('inf')
            
            for sub in self.subordinates:
                # Критерий 1: Минимальная цена
                # Критерий 2: Если цены равны, минимальная длина цепочки
                if (sub.min_cost < min_sub_cost) or \
                   (sub.min_cost == min_sub_cost and sub.chain_length < min_sub_length):
                    min_sub_cost = sub.min_cost
                    min_sub_length = sub.chain_length
                    best_sub = sub
            
            self.best_subordinate = best_sub
            self.min_cost = self.bribe + best_sub.min_cost
            self.chain_length = 1 + best_sub.chain_length