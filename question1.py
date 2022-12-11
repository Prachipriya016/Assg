{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "# Python program to check if\n# given mobile number is valid\nimport re\n\ndef isValid(s):\n\t\n\t# 1) Begins with 0 or 91\n\t# 2) Then contains 6,7 or 8 or 9.\n\t# 3) Then contains 9 digits\n\tPattern = re.compile(\"(\"+\"|1)?[212]{3}?[456]{3}?[7890]{4}?\")\n\treturn Pattern.match(s)\n\n# Driver Code\ns = \"12124567890\"\nif (isValid(s)):\n\tprint (\"Valid Number\")\t\nelse :\n\tprint (\"Invalid Number\")\n\n\n\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [
        {
          "name": "stdout",
          "text": "Valid Number\n",
          "output_type": "stream"
        }
      ],
      "id": "f782f5e8"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "f38d37e3"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "5dfc0ebb"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "dce11678"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "af341a9f"
    }
  ]
}