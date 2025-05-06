# AIthos - Creative AI Platform
# Copyright (C) 2025 DomAIthos
# Licensed under the GNU GPL v3
# See LICENSE file or https://www.gnu.org/licenses/gpl-3.0.html

import openai

def genera_contenuto(prompt, modello="gpt-3.5-turbo"):
    risposta = openai.ChatCompletion.create(
        model=modello,
        messages=[{"role": "user", "content": prompt}]
    )
    return risposta.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Benvenuto su AIthos!")
    prompt = input("Scrivi l'idea per il tuo libro: ")
    output = genera_contenuto(f"Scrivi l'introduzione per un libro su: {prompt}")
    print("\nContenuto generato:\n")
    print(output)
