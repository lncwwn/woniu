#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.web
import hashlib
import modules.db
import datetime

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        nick = self.get_body_argument('nick')
        password = self.get_body_argument('password')
        if not nick or not password:
            self.write({'success': False})
            self.finish()
            return
        member = modules.db.db.get('select id, nick, password from member where nick = %s', nick)

        if member:
            md5 = hashlib.md5()
            md5.update(password)
            password_md5 = md5.hexdigest()
            if member.password == password_md5:
                self.write({'success': True, 'data': member})
                self.finish()
                return
        self.write({'success': False})
        self.finish()

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signup.html');

    def post(self):
        nick = self.get_body_argument('nick')
        password = self.get_body_argument('password')
        password_confirm = self.get_body_argument('password_confirm')
        if nick and password and password_confirm:
            if password == password_confirm:
                md5 = hashlib.md5()
                md5.update(password)
                password_md5 = md5.hexdigest()
                now = datetime.datetime.now()
                insert_sql = 'insert into member (nick, password, created) values (%s, %s, %s)'
                try:
                    member_id = modules.db.db.insert(insert_sql, nick, password_md5, now)
                    self.write({'success': True})
                    self.finish()
                    return
                except:
                    pass
                    # TODO add log

        self.write({'success': False})
        self.finish()
