from app.controllers.controller import ControllerBase
from flask import render_template

class calcWebController(ControllerBase):
    @staticmethod
    def get():
        return render_template('calcWeb.html')

