

import emoji


emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}


print("Emojis disponíveis:")
for texto, icone in emojis_disponiveis.items():
    print(f"{icone} - {texto}")


frase_codificada = input("Digite uma frase e ela será emojizada:\n")


frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)


print("Frase emojizada:")
print(frase_emojizada)
