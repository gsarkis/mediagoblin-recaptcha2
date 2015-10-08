.. _recaptcha2-chapter:

===================
 recaptcha2 plugin
===================

The recaptcha2 plugin adds a Google reCAPTCHA field to the user sign up
form to reduce spam. Future work will focus on switching to reCAPTCHA 2.

This plugin can be enabled alongside :ref:`basic_auth-chapter`.

Set up the recaptcha2 plugin
============================

1. Install wtforms-recaptcha::

    pip install wtforms-recaptcha

2. Add the following to your MediaGoblin .ini file in the ``[plugins]`` section -before- ``[[mediagoblin.plugins.basic_auth]]``::

    [[mediagoblin.plugins.recaptcha2]]
    RECAPTCHA_SITE_KEY = 'your public reCAPTCHA site key from google'
    RECAPTCHA_SECRET_KEY = 'your secret reCAPTCHA key from google'
