from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('munchmate.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM Recipes').fetchall()
    conn.close()
    return render_template('recipes.html', recipes=rows)

@app.route('/api/recipe/<int:rid>')
def api_recipe(rid):
    conn = get_db_connection()
    r = conn.execute('SELECT * FROM Recipes WHERE id=?', (rid,)).fetchone()
    conn.close()
    if r:
        return jsonify(dict(r))
    return jsonify({'error':'not found'}),404

@app.route('/recommend', methods=['GET','POST'])
def recommend():
    matched = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('ingredients','').lower()
        given = [x.strip() for x in query.split(',') if x.strip()]
        conn = get_db_connection()
        allr = conn.execute('SELECT * FROM Recipes').fetchall()
        conn.close()
        for r in allr:
            ings = r['ingredients'].lower()
            if any(g in ings for g in given):
                matched.append(r)
    return render_template('recommend.html', recipes=matched, query=query)

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/blog/<int:id>')
def blog(id):
    return render_template('blog.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
