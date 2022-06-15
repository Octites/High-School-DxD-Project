from colorama import Fore, Back, Style
a = input(Fore.MAGENTA + 'Have you watched High School Dxd? Respond with Y or N: ')
if a == 'N':
    print('Watch the Anime here for free HD https://animixplay.to/v1/high-school-dxd')
elif a == "Y":
    char = input(Fore.RED + 'Choose a Waifu: Rias, Akeno, Kuroka, Koneko, Xenovia, Asia: ')
    if char == "Rias":
        print("""Rias Gremory is the main female protagonist of High School DxD. She is the Gremory Clan's heiress after her oldest brother, Sirzechs, took the position of Lucifer. Rias is the sole daughter and youngest child of Zeoticus and Venelana Gremory, the aunt of Millicas Gremory, and the maternal cousin of Sairaorg and Magdaran Bael.
She became known as the Crimson-Haired Ruin Princess, because of the color of her hair and Power of Destruction. Now, Rias is a first-year College Student at Kuoh Academy, the former President of the Occult Research Club, and the school's Number-One Beauty, as well as one of Kuoh Academy's Two Great Ladies alongside Akeno Himejima. She is also one of Issei's fiancées.""")
    if char == "Akeno":
        print("""Akeno Himejima is a first-year college student at Kuoh Academy and one of the many female protagonists of High School DxD. She is the daughter of Baraqiel, a Fallen Angel Cadre, who is the current Vice Governor General of Grigori and Shuri Himejima, a member of the Himejima Clan. She is Rias Gremory's Queen as well as her best friend. Akeno is one of Kuoh Academy's Two Great Ladies alongside Rias. She is also one of Issei's fiancées.""")
    if char == "Kuroka":
        print("""Kuroka (later on Kuroka Toujou) is a Nekoshou, a rare variant of Nekomata, and a member of the Vali Team previously affiliated with the Khaos Brigade, now a part of Team DxD. She is the older sister of Koneko Toujou and a former SS-Class Stray Devil, one of the most wanted criminals in the Underworld for killing her master, which was later revealed to be in order to protect her sister.
She is also one of Issei's fiancees. After the defeat of the Alliance of Hell, she became Xenovia Quarta's Bishop.""")
    if char == "Koneko":
        print("""Koneko Toujou, originally named Shirone is one of the female protagonists of High School DxD. At first, a first-year student at Kuoh Academy, prior to becoming a second-year, and a member of the Occult Research Club. She is a Nekoshou, a rare species of Nekomata, and the younger sister of Kuroka, as well as Rias Gremory's first Rook.
Having become one of Issei's fiancées, then coming to terms with herself, her past, and making amends with Kuroka, Koneko started going by Shirone Toujou.""")
    if char == "Xenovia":
        print("""Xenovia Quarta is one of the many female protagonists of High School DxD. She is a third-year high school student at Kuoh Academy in Class 3-B and is a natural-born Holy Sword user who wields the Durandal. After learning the truth of God's death in the war, she was excommunicated from the Church and decided to join the Occult Research Club as Rias' second Knight, alongside Yuuto. After Issei's promotion, she now serves under him as his first Knight and is also one of his fiancées.""")
    if char == "Asia":
        print("""Asia Argento is one of the many female protagonists of High School DxD. She is a third-year high school student at Kuoh Academy in Class 3-B and is a girl with a very gentle heart who possesses a rare Sacred Gear, Twilight Healing, in her body that is capable of healing the wounds of Humans, Angels, Fallen Angels, and Devils alike. She was formerly one of Rias Gremory's Bishops but now serves as Issei Hyoudou's first Bishop and one of his fiancées.""")
    elif char != "Rias" or "Akeno" or "Kuroka" or "Xenovia" or "Asia":
        print('Please enter the name of a character.')
else:
    print(("Please enter Y or N. (Yes or No)"))