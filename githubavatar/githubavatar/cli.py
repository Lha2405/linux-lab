import click
import requests
import sys

from PIL import Image
try:
    from StringIO import StringIO
except: # when using python3.x
    from io import BytesIO, StringIO

@click.command()
@click.option('--as-author', '-c', is_flag=True, help='Computer Science at UBU')
@click.argument('name', default='wichit2s', required=False)
def main(name, as_author):
    """Get Github Avatar"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    api_user_url = 'https://resizing.flixster.com/zt1Al_3bLFv_5OGXwg-camTxzmk=/300x300/v1.bjsxMjYxMjY5O2o7MTc1NjQ7MTIwMDszMDAwOzE1MDA'.format(name)
    json = requests.get(api_user_url).json()
    req = requests.get(json['avatar_url'])
    if sys.version_info >= (3,0):
        img = Image.open(BytesIO(req.content))
        img.show()
    else:
        img = Image.open(StringIO(req.content))
        img.show()
