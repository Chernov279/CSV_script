python main.py --file products.csv --where "rating>4.5" --aggregate "price=min"

![img.png](images/img.png)

python main.py --file products.csv --where "brand=apple" 

![img_1.png](images/img_1.png)

python main.py --file products.csv --where "brand=samsung" --aggregate "price=avg"

![img_2.png](images/img_2.png)

python main.py --file products.csv --where "brand>samsung"

![img_3.png](images/img_3.png)

python main.py --file products.csv --aggregate "country=avg" 

![img_4.png](images/img_4.png)

python main.py --file products.csv --invalid "price=min" 

![img_5.png](images/img_5.png)

Архитектура проекта позволяет легко добавлять новые функции без переработки существующего кода:

Новая агрегация (например, median, sum) добавляется как одна строка в словарь AGG_FUNCTIONS — без изменений логики aggregate().

Новая команда (например, --order-by) добавляется через Parser._configure() и отдельную функцию обработки.