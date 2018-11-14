DEPLOY_COMMANDS = [
    # ('add db backup', 'python manage.py dbbackup'),
    ('pull changes', '../scripts/fail-if-git-status-dirty.sh && git pull'),
    ('update dependencies', 'pip install --requirement=requirements.txt'),
    ('migrate database', 'python manage.py migrate'),
    # ('send validation report to admins', 'python manage.py validationreport --sendmail'),
    # ('update dashboard', 'cd dashboard/vue-frontend-src && npm ci && npm run build'),
    ('update static files', 'python manage.py collectstatic --noinput'),
    ('restart app', 'touch wholesaler/wsgi.py'),
]

