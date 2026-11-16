# Tomita Parser News Corpus / Корпус новостей (Томита-парсер)

*[Read in Russian / Читать на русском](#русский-язык)*

## English

**Tomita Parser News Corpus** is a web application designed to extract structured facts from a custom text corpus using the Yandex Tomita Parser. The current dataset consists of approximately 2,000 parsed news articles focused on physics and astronomy, collected from `ab-news.ru`.

This project integrates a C++ based NLP binary tool with a modern web interface, utilizing a PostgreSQL database for corpus management and Docker for seamless deployment.

### Features
* **Custom Grammar & Dictionaries:** Fact extraction rules written in `.cxx` and `.gzt` for specialized entity recognition.
* **Corpus Navigation:** Fast search and filtering across 2,000 scientific news articles (by text, lemma, category, and date).
* **Web Interface:** A Flask-based UI that sends text to the Tomita Parser without page reloads and visualizes the extracted facts.
* **Containerization:** Fully dockerized environment for both the web application and the PostgreSQL database.

### Tech Stack
* **Backend:** Python, Flask, Pandas (ETL)
* **NLP / Data:** Yandex Tomita Parser, Mystem / pymorphy2 (for lemmatization), BeautifulSoup4 (scraping)
* **Database:** PostgreSQL
* **Infrastructure:** Docker, Docker Compose, Git

---

<a name="русский-язык"></a>
## Русский язык

**Tomita Parser News Corpus** — это веб-приложение для извлечения структурированных фактов из текстового корпуса с помощью Yandex Tomita Parser. Текущий датасет включает около 2000 новостных статей по физике и астрономии, собранных с портала `ab-news.ru`.

Проект демонстрирует интеграцию бинарного NLP-инструмента с веб-интерфейсом, использование базы данных PostgreSQL для управления корпусом и упаковку всей инфраструктуры в Docker.

### Основной функционал
* **Собственные грамматики:** Правила извлечения фактов, написанные на `.cxx` и `.gzt`.
* **Навигация по корпусу:** Быстрый поиск и фильтрация по 2000 научным статьям (по тексту, лемме, рубрике и дате).
* **Веб-интерфейс:** UI на Flask, который отправляет текст в парсер без перезагрузки страницы и визуализирует найденные сущности.
* **Контейнеризация:** Полностью изолированная среда с использованием Docker для приложения и БД.

### Стек технологий
* **Бэкенд:** Python, Flask, Pandas (ETL)
* **NLP / Данные:** Yandex Томита-парсер, Mystem / pymorphy2 (для лемматизации), BeautifulSoup4 (парсинг)
* **База данных:** PostgreSQL
* **Инфраструктура:** Docker, Docker Compose, Git