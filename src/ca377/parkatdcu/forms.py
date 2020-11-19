from django import forms


class SearchForm(forms.Form):
    campus = forms.CharField(label="Campus", max_length=100)

    def clean_data(self):
        data = self.cleaned_data["campus"]
        return data.lower()
