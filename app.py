import os
import codecs
import subprocess
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def load_data():
    """Загрузка данных из CSV и подготовка уникальных значений для фильтров"""
    csv_path = os.path.join(BASE_DIR, 'abnews.csv')
    try:
        df = pd.read_csv(csv_path)
        # Если каких-то колонок нет в CSV, pandas создаст пустые для совместимости
        for col in ['title', 'text', 'class_name', 'author_name', 'pub_date']:
            if col not in df.columns:
                df[col] = "Неизвестно" if col != 'text' else ""
        return df
    except:
        return pd.DataFrame()

@app.route("/")
def index():
    df = load_data()
    if df.empty:
        return render_template("index.html", articles=[], error="Файл базы данных не найден")

    # Получаем параметры поиска из URL
    search_query = request.args.get('q', '').lower()
    search_mode = request.args.get('mode', 'text') # text или lemma
    category = request.args.get('category', '')
    
    # Примитивная фильтрация (заменится на SQL WHERE)
    if search_query:
        # В реальной БД здесь будет поиск по wform или lemma
        df = df[df['text'].str.lower().str.contains(search_query, na=False)]
    if category and category != 'Все рубрики':
        df = df[df['class_name'] == category]

    articles = df.to_dict('records')
    categories = df['class_name'].unique().tolist()
    
    return render_template("index.html", 
                           articles=articles, 
                           categories=categories,
                           q=search_query,
                           mode=search_mode,
                           selected_cat=category)

@app.route("/extract", methods=["POST"])
def extract():
    """Теперь возвращает только фрагмент HTML для модального окна"""
    txt0 = request.form["txt"]
    tomita_dir = os.path.join(BASE_DIR, "tomita")
    input_path = os.path.join(tomita_dir, "input.txt")
    output_path = os.path.join(tomita_dir, "output.txt")
    tomita_parser_path = os.path.join(tomita_dir, "tomitaparser")

    try:
        with codecs.open(input_path, "w", "utf-8") as f:
            f.write(str(txt0))
        
        command = [tomita_parser_path, "config.proto"]
        subprocess.check_output(command, stderr=subprocess.STDOUT, cwd=tomita_dir)
        
        with open(output_path, "r", encoding="utf-8") as f:
            results = f.read()
            
        # Возвращаем просто текст (или можно отрендерить мини-шаблон)
        return f"<h3>Входной текст:</h3><p>{txt0}</p><h3>Извлеченные факты:</h3><pre>{results}</pre>"
    except Exception as e:
        return f"<div class='error'>Ошибка парсера: {str(e)}</div>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)