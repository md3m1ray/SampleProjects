import random


def zar_at():
    return random.randint(1, 6)


score = 0
denemesayisi = 0


def main(score, denemesayisi):
    input("Zar atmak için Enter tuşuna basın...")

    denemesayisi += 1
    zar1 = zar_at()
    zar2 = zar_at()

    print(f"\nZar 1: {zar1}")
    print(f"Zar 2: {zar2}")

    if zar1 == zar2:
        print("İki zar da aynı! Tebrikler!")
        score += 1
    else:
        print("İki zar farklı. Daha fazla şansını denemelisin!")

    print(f"Score: {score}\n")

    if score == 3 :
        print(f"{denemesayisi} defa zar atarak 3 puan hedefine ulaştınız tebrikler")
    elif denemesayisi == 15 :
        print("15 defa zar attınız ancak hedefe ulaşamadınız. Üzgünüz!")
    else:
        main(score, denemesayisi)


if __name__ == "__main__":
    main(score, denemesayisi)
