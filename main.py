from bottle import HTTPError, route, run, request
from config import SQLite


db = SQLite('albums.sqlite3')

@route("/albums/<artist>")
def albums(artist):
    albums_list = db.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album[4] for album in albums_list]
        result = f"Кол-во альбомов группы {artist} -- {len(albums_list)}<br>"
        result += "Список альбомов {}<br>".format(artist)
        result += "<br>".join(album_names)
    return result

@route("/albums", method="POST")
def user():
    for ids in db.get_ids():
        new = ids[0] + 1
    user_data = {
        "id": new,
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    if not db.check_name(user_data['album']):
        try:
            user_data['year'] = int(user_data['year'])
        except:
            return "Некорректный год"
        db.add(user_data)
        return "Данные успешно сохранены"
    else:
        message = "Альбом {} уже есть в базе".format(user_data['album'])
        result = HTTPError(409, message)
        return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)

# В консоль:
# http -f POST localhost:8080/albums year=2000 artist="New Artist" genre="Rock" album="Super"
