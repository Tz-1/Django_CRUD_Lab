from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio', ciudad='Ciudad', pais='Pais')
    
    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad')
        self.assertEqual(self.laboratorio.pais, 'Pais')

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorio/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("mostrar-lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mostrar.html")
        self.assertContains(response, "Información de Laboratorios")