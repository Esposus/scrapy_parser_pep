## Описание проекта
Асинхронный парсер, собирающий данные (номер, название и статус) о Python Enhancement Proposals (PEP) с сайта https://www.python.org/, а также формирующий сводку по количеству PEP каждого статуса в отдельный .csv файл.

### Технологии
- Python 3.11.0
- Scrapy 2.5.1

**Для работы с парсером**:
>Скопировать проект командой: 
```bash
git clone git@github.com:Esposus/scrapy_parser_pep.git
```
>Установить и активировать виртуальное окружение
```bash
python3 -m venv venv

source venv/Scripts/activate
```
>Установить зависимости:
```bash
pip install -r requirements.txt
```
>Запустить из директории scrapy_parser_pep:
```bash
scrapy crawl pep
```

### Автор: [Дмитрий Морозов](https://github.com/Esposus "GitHub аккаунт")