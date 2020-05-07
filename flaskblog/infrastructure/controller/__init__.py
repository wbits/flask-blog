from flask import render_template, url_for, flash, redirect, request
from flaskblog.application import user_service
from flaskblog.infrastructure.form import registration_form, login_form
from flaskblog.infrastructure.controller.user_controller import UserController
from flaskblog.infrastructure.controller.controller_service import ControllerService
from flaskblog.infrastructure import session


def user_controller():
    return UserController(controller_service(), user_service(), registration_form(), login_form())


def controller_service():
    return ControllerService(redirect, url_for, flash, render_template, request, session())
