from django.forms import ModelForm
from .models import Question


class QuestionModelForm(ModelForm):
    """docstring for QuestionModelForm."""
    class Meta():
        model = Question
        # fields = ['question_text','pub_date']
        # include =
        exclude = ['id']
