import numpy as np


def calculate(numbers):
    # Перевіряємо, чи список містить 9 елементів
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Перетворюємо список у numpy масив 3x3
    matrix = np.array(numbers).reshape(3, 3)

    # Створюємо словник з потрібними статистичними значеннями
    result = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    # Виведення результату на окремих рядках
    for key, value in result.items():
        print(f"{key}: {value}")

    return result

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(numbers)
