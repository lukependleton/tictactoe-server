import flask
import tictactoe

@tictactoe.app.route('/api/rooms/getRooms', methods=["GET"])
def getRooms():
    return "None so far, but we'll get some implemented soon"

