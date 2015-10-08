# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2015 Gabi Sarkis
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

import os
import logging

from mediagoblin.tools import pluginapi

from . import forms as recaptcha2_forms

_log = logging.getLogger(__name__)

PLUGIN_DIR = os.path.dirname(__file__)

def setup_plugin():
    _log.info('Setting up recaptcha2...')
    config = pluginapi.get_config('mediagoblin.plugins.recaptcha2')

    _log.info('Done setting up recaptcha2...')

def get_registration_form(request):
    config = pluginapi.get_config('mediagoblin.plugins.recaptcha2')
    return recaptcha2_forms.RegistrationForm(request.form,
                                             site_key=config.get('RECAPTCHA_SITE_KEY'),
                                             secret_key=config.get('RECAPTCHA_SECRET_KEY'),
                                             captcha={
                                                'ip_address': request.remote_addr,
                                             })

hooks = {
    'setup': setup_plugin,
    'auth_get_registration_form': get_registration_form,
}
