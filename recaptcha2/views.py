@allow_registration
@auth_enabled
def register(request):
#    if request.method == 'GET':
#        return redirect(
#            request,
#            'mediagoblin.plugins.recaptcha.register')

    register_form = auth_forms.RegistrationForm(request.form)
    config = pluginapi.get_config('mediagoblin.plugins.recaptcha')

    recaptcha_protocol = ''
    if config['RECAPTCHA_USE_SSL']:
        recaptcha_protocol = 'https'
    else:
        recaptcha_protocol = 'http'
    _log.debug("Connecting to reCAPTCHA service via %r", recaptcha_protocol)

    if register_form.validate():
        recaptcha_challenge = request.form['recaptcha_challenge_field']
        recaptcha_response = request.form['recaptcha_response_field']
        _log.debug("response field is: %r", recaptcha_response)
        _log.debug("challenge field is: %r", recaptcha_challenge)
        response = captcha.submit(
            recaptcha_challenge,
            recaptcha_response,
            config.get('RECAPTCHA_PRIVATE_KEY'),
            request.remote_addr,
            )

        goblin = response.is_valid
        if response.error_code:
            _log.debug("reCAPTCHA error: %r", response.error_code)

        if goblin:
            user = register_user(request, register_form)

            if user:
                # redirect the user to their homepage... there will be a
                # message waiting for them to verify their email
                return redirect(
                    request, 'mediagoblin.user_pages.user_home',
                    user=user.username)

        else:
            messages.add_message(
                request,
                messages.WARNING,
                _('Sorry, captcha was incorrect. Please try again.'))

    return render_to_response(
        request,
        'mediagoblin/plugins/recaptcha/register.html',
        {'register_form': register_form,
         'post_url': request.urlgen('mediagoblin.plugins.recaptcha.register'),
         'recaptcha_public_key': config.get('RECAPTCHA_PUBLIC_KEY'),
         'recaptcha_protocol' : recaptcha_protocol})

