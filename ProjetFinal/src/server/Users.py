#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Users:

    def __init__(self, client, id):
        self.client = client
        self.id = id
        self.pseudo = ""
    def setPseudo(self, value):
        self.pseudo = value
