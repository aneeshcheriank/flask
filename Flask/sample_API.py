from flask import Flask, jsonify, request

app = Flask(__name__)

books_list = [
    {
        'id': 0,
        'author': 'Chinua Avhrbr',
        'language': 'English',
        'title': 'Things fall appart'
    },
    {
        'id': 1,
        'author': 'Hans Christian Andersen',
        'language': 'Dannish',
        'title': 'Fairy tales'
    },
    {
        'id': 2,
        'author': 'Samuel Beckett',
        'language': 'French, English',
        'title': 'Molloy, Malone Dies, The Unnamanle, the trilogy'
    },
    {
        'id': 3,
        'author': 'Giovanni Boccaccio',
        'language': 'Italian',
        'title': 'The Decameron'
    },
    {
        'id': 4,
        'author': 'Jorge Luis Borges',
        'language': 'Spanish',
        'title': 'Ficctiones'
    },
    {
        'id': 5,
        'author': 'Emily Bront',
        'language': 'English',
        'title': 'Wuthering Heights'
    }
]

@app.route('/books', methods=['GET', 'POST'])
def books():
    
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404
            
    if request.method == 'POST':
        author = request.form['author']
        lang = request.form['language']
        title = request.form['title']
        iD = books_list[-1]['id']+1
        
        books_list.append({
            'id': iD,
            'author': author,
            'language': lang,
            'title': title
        })
        
        return jsonify(books_list), 201
    
@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    
    for book in books_list:
        if book['id'] == id:
            break
    
    if request.method == 'GET':
        return jsonify(book)
            
    elif request.method == 'PUT':
        author = request.form['author']
        lang = request.form['language']
        title = request.form['title']
        
        book['author'] = author
        book['language'] = lang
        book['title'] = title
        
        return jsonify(books_list)
    
    elif request.method == 'DELETE':
        books_list.remove(book)
        
        ## need to update the ids:
        for i in range(id, len(books_list)):
            books_list[i]['id'] = i
            
        return jsonify(books_list)        



if __name__ == '__main__':
    app.run(debug=True)
    