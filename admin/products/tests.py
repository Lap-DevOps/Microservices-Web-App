from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.db import connections

from django.test import TestCase
from django.db import connections

class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        # Проверка соединения с базой данных
        connection = connections['default']
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

            # Проверяем, что результат не является None
            result = cursor.fetchone()
            self.assertIsNotNone(result, "Expected non-None result")

            # Если результат не None, проверяем значение
            if result is not None:
                self.assertEqual(result[0], 1, "Unexpected value in the result")
