     from flask import Flask, request, abort, render_template

webapp = Flask("mywebapp")
  
@webapp.route('/')
def index():
  return 'Hello anonymous user!'

if __name__ == '__main__':
  webapp.debug = True
  webapp.run()
