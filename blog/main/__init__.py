#!/usr/bin/env python

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

# EOF