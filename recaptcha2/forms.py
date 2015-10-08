# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import wtforms
from wtfrecaptcha.fields import RecaptchaField

from mediagoblin.tools.translate import lazy_pass_to_ugettext as _
from mediagoblin.auth.tools import normalize_user_or_email_field
from mediagoblin.tools import pluginapi

class RegistrationForm(wtforms.Form):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if 'site_key' in kwargs:
            self.captcha.public_key = kwargs.pop('site_key')
        else:
            raise ValueError('Recaptcha site key is required.')
        if 'secret_key' in kwargs:
            self.captcha.private_key = kwargs.pop('secret_key')
        else:
            raise ValueError('Recaptcha secret key is required.')

    username = wtforms.StringField(
        _('Username'),
        [wtforms.validators.InputRequired(),
         normalize_user_or_email_field(allow_email=False)])
    password = wtforms.PasswordField(
        _('Password'),
        [wtforms.validators.InputRequired(),
         wtforms.validators.Length(min=5, max=1024)])
    email = wtforms.StringField(
        _('Email address'),
        [wtforms.validators.InputRequired(),
         normalize_user_or_email_field(allow_user=False)])

    captcha = RecaptchaField(
	public_key='unset',
	private_key='unset',
       	secure=True)
