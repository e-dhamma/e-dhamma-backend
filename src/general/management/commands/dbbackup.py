import os
import datetime
from shutil import copyfile

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from utils.opsys import change_dir


class Command(BaseCommand):
    help = f"Add database backup to '{settings.BACKUP_DIR}' directory"

    def handle(self, *args, **options):
        backup = add_db_backup()
        self.stdout.write(self.style.SUCCESS(f"Backup '{backup}' was created successfully"))


def add_db_backup():
    # Check whether directory for db backups exists
    if not os.path.exists(settings.BACKUP_DIR):
        os.makedirs(settings.BACKUP_DIR)

    # Make a backup
    with change_dir(settings.BACKUP_DIR):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = f'db-backup-at-{timestamp}.sqlite3'
        copyfile(os.path.join(settings.BASE_DIR, 'db.sqlite3'), os.path.join(settings.BACKUP_DIR, filename))
    return filename
