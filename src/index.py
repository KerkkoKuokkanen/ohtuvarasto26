from varasto import Varasto


def tulosta_perustiedot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta


def testaa_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_setterit(mehua):
    print("Mehu setterit:")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def testaa_virhetilanteet1(olutta):
    print("Virhetilanteita:")
    print(f"Varasto(-100.0): {Varasto(-100.0)}")
    print(f"Varasto(100.0, -50.7): {Varasto(100.0, -50.7)}")

    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto liian lisäyksen jälkeen: {olutta}")

def testaa_virhetilanteet2(mehua, olutta):
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto negatiivisen lisäyksen jälkeen: {mehua}")

    saatiin_olut = olutta.ota_varastosta(1000.0)
    print(f"Olutta saatiin: {saatiin_olut}, varasto: {olutta}")

    saatiin_mehu = mehua.ota_varastosta(-32.9)
    print(f"Mehua saatiin: {saatiin_mehu}, varasto: {mehua}")


def main():
    mehua, olutta = tulosta_perustiedot()
    testaa_getterit(olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet1(olutta)
    testaa_virhetilanteet2(mehua, olutta)


if __name__ == "__main__":
    main()
