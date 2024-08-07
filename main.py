#import sys
from API import create_app

#sys.path.append(API)


app = create_app()

if __name__ == '__main__':
    app.run(debug = True)