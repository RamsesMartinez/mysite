from django.db import models


class Question(models.Model):
    """Modelo para las preguntas."""
    question_text = models.CharField('titulo', max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"


class ChoiceTag(models.Model):
    """Modelo para indicar tags a las opciones"""
    tag = models.CharField(verbose_name="Tag", max_length=60)

    def __str__(self):
        return f"{self.id} - {self.tag}"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Choice(models.Model):
    """Modelo para las opciones."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.ForeignKey(
        ChoiceTag,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    choice_text = models.CharField("texto", max_length=200)
    votes = models.IntegerField("votos", default=0)

    def __str__(self):
        return f"{self.question} - {self.choice_text} - {self.votes}"

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
