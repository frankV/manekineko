
# -*- coding: utf-8 -*-

import os

from flask import Blueprint, render_template, send_from_directory, abort, redirect, url_for, request, flash
from flask import current_app as app
from flask.ext.login import login_required, current_user
from .forms import CreateMessageForm
from .models import Message, StaredMessages


message = Blueprint('message', __name__, url_prefix='/message')


@message.route('/add_message', methods=['POST'])
@login_required
def add_message():
	user = current_user
	form = CreateMessageForm()
	if form.validate_on_submit():
		form.add_message(user)
		flash("Your message has been added",'success')
	msg = Message()
	return render_template('user/index.html', form=form, user=user,messages = msg.get_all_messages())

@message.route('/add_starred_message/<int:message_id>', methods=['GET'])
def add_star_message(message_id):
	user = current_user
	star_message = StaredMessages()
	star_message.add(
		user_id = current_user.id,
		message_id = message_id
		)
	form = CreateMessageForm()
	msg = Message()
	return render_template('user/index.html', form=form, user=user,messages = msg.get_all_messages())

@message.route('/remove_starred_message/<int:message_id>', methods=['GET'])
def remove_star_message(message_id):
	user = current_user
	star_message = StaredMessages()
	star_message.delete_by_id(message_id)
	form = CreateMessageForm()
	msg = Message()
	return render_template('user/index.html', form=form, user=user,messages = msg.get_all_messages())

	




