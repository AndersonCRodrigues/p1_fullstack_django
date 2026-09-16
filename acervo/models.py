from django.db import models


class Livro(models.Model):
    class Tipo(models.TextChoices):
        DIGITAL = "D", "Digital"
        FISICO = "F", "Fisico"

    class Categoria(models.TextChoices):
        GENERALIDADES = (
            "000",
            "000 - Generalidades e Informação: Obras gerais, enciclopédias, jornais e"
            " biblioteconomia.",
        )
        FILOSOFIA_PSICOLOGIA = (
            "100",
            (
                "100 - Filosofia e Psicologia: Ética, lógica e investigações sobre a"
                " mente humana."
            ),
        )
        RELIGIAO_TEOLOGIA = (
            "200",
            (
                "200 - Religião e Teologia: Mitologia, teologia e estudos sobre"
                " crenças e religiões."
            ),
        )
        CIENCIAS_SOCIAIS = (
            "300",
            (
                "300 - Ciências Sociais e Direito: Política, economia, sociologia,"
                " educação e leis."
            ),
        )
        LINGUISTICA = (
            "400",
            (
                "400 - Linguística e Idiomas: Gramáticas, dicionários e estudos de"
                " línguas."
            ),
        )
        CIENCIAS_PURAS = (
            "500",
            (
                "500 - Ciências Puras (Exatas e Naturais): Matemática, física,"
                " química, biologia e astronomia."
            ),
        )
        CIENCIAS_APLICADAS = (
            "600",
            (
                "600 - Ciências Aplicadas (Tecnologia): Medicina, engenharia,"
                " agricultura e administração."
            ),
        )
        ARTES = (
            "700",
            (
                "700 - Artes e Recreação: Pintura, música, arquitetura, esportes e"
                " lazer."
            ),
        )
        LITERATURA = (
            "800",
            (
                "800 - Literatura: Poesia, romances, contos, crônicas e crítica"
                " literária."
            ),
        )
        HISTORIA_GEOGRAFIA = (
            "900",
            (
                "900 - História e Geografia: Biografias, viagens e acontecimentos"
                " históricos"
            ),
        )

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo = models.CharField(
        max_length=1, 
        choices=Tipo.choices, 
        default=Tipo.DIGITAL,
    )
    categoria = models.CharField(
      max_length=3,
      choices=Categoria.choices,
      default=Categoria.GENERALIDADES,
    )

    def __str__(self):
        return self.titulo
