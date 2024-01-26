import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

def combine_cables(sorted_cables):
    total_cost = 0
    connections = []

    while len(sorted_cables) > 1:
        # Беремо два найменших кабелі та об'єднуємо їх
        min_length1 = heapq.heappop(sorted_cables)
        min_length2 = heapq.heappop(sorted_cables)
        combined_length = min_length1 + min_length2

        # Додаємо витрати на з'єднання до загальних витрат
        total_cost += combined_length

        # Додаємо пару об'єднаних кабелів до списку з'єднань
        connections.append((min_length1, min_length2))

        # Додаємо новий об'єднаний кабель назад до списку
        heapq.heappush(sorted_cables, combined_length)

    return total_cost, connections

# Приклад використання:
cables = [4, 3, 2, 6]
sorted_cables = heap_sort(cables)
total_cost, connections = combine_cables(sorted_cables)

print("Сортований список кабелів:", sorted_cables)
print("Загальні витрати:", total_cost)
print("Порядок з'єднань для мінімізації витрат:", connections)
