"""
This file contains GenerateImagesForm for creating form
for prompts input
"""
from django import forms


class GenerateImagesForm(forms.Form):
    """
    GenerateImagesForm with field 'prompts' to take input
    from the user
    """
    prompts = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter each prompt on a new line."
    )

    def clean_prompts(self):
        """
        To split the string and remove any whitespaces
        """
        data = self.cleaned_data['prompts']
        return [prompt.strip() for prompt in data.splitlines() if prompt.strip()]

