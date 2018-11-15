import subprocess
import os
import re
from django.test import TestCase
from django.conf import settings
from utils.opsys import change_dir

OUTPUT_REGEX = re.compile(r"Backup 'db-backup-at-(\d{4}-\d{2}-\d{2})-\d{6}.sqlite3' was created successfully")


class ManagePyCommandsTest(TestCase):

    def test_dbbackup_command(self):
        num_of_db_backups = os.listdir(settings.BACKUP_DIR)
        p = subprocess.run('python ./manage.py dbbackup',
                           stdout=subprocess.PIPE, shell=True)
        self.assertTrue(OUTPUT_REGEX.match(p.stdout.decode().strip()))
        new_num_of_db_backups = os.listdir(settings.BACKUP_DIR)
        self.assertEqual(len(num_of_db_backups) + 1, len(new_num_of_db_backups))
