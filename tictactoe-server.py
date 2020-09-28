import argparse
import tictactoe

# TODO: make this a cli tool

def startServer(args):
    #print(f"arguments: {args}")
    print(f"listing urls so far hopefully: {tictactoe.app.url_map}")
    #print("Starting the tictactoe server")
    #tictactoe.app.run()

def stopServer(args):
    pass

# Set up the argument parser
parser = argparse.ArgumentParser(prog="tictactoe", description="The only tictactoe command line arg parser")
#parser.add_argument("startServer")#, func=startServer)

funcMap = {
    "startServer": startServer,
    "stopServer": stopServer
}
parser.add_argument("command", choices=funcMap.keys())

# Parse the given arguments
args = parser.parse_args()
func = funcMap[args.command]
func(args)
#args.func(args)


