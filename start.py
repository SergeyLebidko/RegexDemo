import re


# Функция match ищет совпадение с шаблоном начиная с первого символа строки
def _match():
    regex = re.compile(r'\w+')
    result = regex.match('Питон - хороший язык программирования')
    print(result)


# Функция search также первое совпадение с шаблоном, при этом оно может находится в любом месте строки
def _search():
    regex = re.compile(r'(\w)*род(\w)*')
    result = regex.search('лопата родители порождение порода окно огород')
    print(result)


# Функция findall возвращает список совпадений с шаблоном
def _findall():
    regex = re.compile(r'\w*род\w*')
    result = regex.findall('лопата родители порождение порода окно огород')
    print(result)


# Функция split делит строку на части. В качестве разделителя выступает часть строки, соотвествующая шаблону
def _split():
    regex = re.compile(r'\s*раздел\s*')
    result = regex.split('лопата раздел   родители раздел порождение порода   раздел окно огород')
    print(result)


# Функция sub заменяет части строки, соответствующие шаблону на другую строку
def _sub():
    regex = re.compile(r'\s*раздел\s*')
    result = regex.sub('$', 'лопата раздел   родители раздел порождение порода   раздел окно огород')
    print(result)


def main():
    _match()
    _search()
    _findall()
    _split()
    _sub()


if __name__ == '__main__':
    main()
