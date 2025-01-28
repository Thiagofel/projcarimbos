from django import forms
from datetime import datetime

class ClienteForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "id": "nome", 
                "required": True})
    )
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "required": True,
                "id": "data_nascimento",
                "min": "1900-01-01",  # Limite inferior
                "max": datetime.now().strftime("%Y-%m-%d"),  # Data máxima como hoje
                "placeholder": "DD/MM/YYYY."
            }
        ),
        input_formats=["%Y-%m-%d", "%d/%m/%Y"],  # Define o formato esperado
        error_messages={
            "invalid": "Data de nascimento inválida. Use o formato DD-MM-YYYY."
        }
    )

    def clean_data_nascimento(self):
        data = self.cleaned_data.get("data_nascimento")

        # Garante que a data é válida e dentro de um intervalo aceitável
        if data.year < 1900 or data > datetime.now().date():
            raise forms.ValidationError("Por favor, insira uma data de nascimento válida entre 1900 e hoje.")

        return data
