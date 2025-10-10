from pathlib import Path

photo_path = Path(__file__).parent / "assets" / "532869931.jpg"

RECIPE_DATA = {
    "name": 'Бургер',
    "ingredient": 'булка',
    "amount": '1',
    "cooking_time": '15',
    "description": 'грустный бургер без котлетки',
    "photo": str(photo_path)
}