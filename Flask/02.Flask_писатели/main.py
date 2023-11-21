
books_year = {
    'Hemingway': {
        1925: ['In Our Time'],
        1926: ['The Sun Also Rises', 'Men Without Women'],
        1940: ['For Whom the Bell Tolls']
    },
    'Shakespeare': {
        1997: ['Harry Potter and the Philosophers Stone'],
        1998: ['Harry Potter and the Chamber of Secrets']
    }
}

write='Hemingway'
year=1926
if write in books_year and year in books_year[write]:
     books = books_year[write][year]
     print(books)