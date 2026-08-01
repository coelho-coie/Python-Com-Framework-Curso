"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_wsgi_application()


# Força a execução das migrações caso esteja no Vercel
#if os.environ.get('VERCEL'):  #Funcionou no vercel
#    try:
#        from django.core.management import call_command
#        call_command('migrate', interactive=False)
#    except Exception as e:
#        print(f"Erro ao rodar migrações no Vercel: {e}")
