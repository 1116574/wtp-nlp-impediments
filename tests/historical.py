# body = "<p><strong>Z przyczyn technicznych wyst&#x119;puj&#x105; utrudnienia w kursowaniu metra linii M1. Metro kursuje w p&#x119;tli Metro Kabaty &#x2013; Metro S&#x142;odowiec &#x2013; Metro Kabaty.</strong></p><p><strong>Trwa uruchamianie komunikacji zast&#x119;pczej za metro.</strong></p><p><strong>Za utrudnienia przepraszamy.</strong></p>"
# body = html.unescape(body)

with open('history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

# body = html.unescape(history[20]['body'])  # 17  19 wejscie lol
body = html.unescape(history[66]['body'])
# body = '<p><strong><u>Trwa przywracanie podstawowej organizacji ruchu.</u></strong></p><p> Z powodu zdarzenia na stacji metra<strong> Centrum</strong> wyst&#x119;puj&#x105; utrudnienia w kursowaniu linii metra <strong>M1</strong>. Ruch odbywa si&#x119; w p&#x119;tlach: <strong>Kabaty &#x2013; Politechnika</strong> oraz <strong>Dw.Gda&#x144;ski &#x2013; M&#x142;ociny</strong>. </p><p> Na odcinku <strong>Metro Politechnika</strong> <strong>&#x2013; Dw. Gda&#x144;ski</strong> prosimy r&#xF3;wnie&#x17C; o korzystanie z tramwajowej linii <strong>4,15,18,35. </strong></p><p>Autobusy linii <strong>520</strong> kursuj&#x105; na wyd&#x142;u&#x17C;onej trasie <strong>Marysin&#x2026;..pl. Bankowy, Andersa &#x2013; pl. Wilsona.</strong></p><p> <strong>Przepraszamy za utrudnienia.</strong> </p>'
# 35 doesnt even have loop skull emoji
soup = BeautifulSoup(body, 'html.parser')
processed_html = [s for s in soup.strings]

text = ' '.join(processed_html)
text = "W związku z budową stacji metra C19 ZACISZE, C20 KONDRATOWICZA oraz C21 BRÓDNO i koniecznością czasowego wyłączenia ruchu na stacjach C16 SZWEDZKA, C17 TARGÓWEK MIESZKANIOWY i C18 TROCKA, od dnia 14.08.2022 r. od początku kursowania do nocy 21/22.08.2022 r. do końca kursowania trasa linii metra M2 zostanie skrócona:\n\nM2\n\nBEMOWO – … – DWORZEC WILEŃSKI\n\nJednocześnie uruchomiona zostanie zastępcza linia autobusowa ZM2 kursująca na trasie:\n\nMETRO TROCKA – Trocka – Unicka (d. Pratulińska) – Handlowa – Ossowskiego – Barkocińska – Myszkowska – Gorzykowska – Radzymińska – al. Solidarności – Targowa – DW. WILEŃSKI (powrót: Targowa – zawrotka przy ulicy Ząbkowskiej – Targowa – al. Solidarności)\n\nDodatkowo w dniach od dnia 14.08.2022 r. do dnia 21.08.2022 r. wprowadza się następujące zmiany tras linii 140, 199, 245, 340, 527 i 738:\n\n140\n\nMarki: CZARNA STRUGA – Legionowa – al. Piłsudskiego – Ząbki: Radzymińska – Warszawa: Radzymińska – al. Solidarności – Targowa – DW. WILEŃSKI\n\n199\n\nREMBERTÓW-STRZELNICA – … – Bystra – Radzymińska – al. Solidarności – Targowa – DW. WILEŃSKI\n\n245\n\nZąbki: MACZKA – … – Warszawa: Łodygowa – Radzymińska – al. Solidarności – Targowa – DW. WILEŃSKI\n\n269\n\nzawieszenie kursowania\n\n527\n\nGRODZISK – … – św. Wincentego – Borzymowska – Trocka – Radzymińska – al. Solidarności – Targowa – Kijowska – DW. WSCHODNI /KIJOWSKA/\n\n738\n\nRadzymin: OS. VICTORIA – … – Ząbki: Radzymińska – Warszawa: Radzymińska – al. Solidarności – Targowa – DW. WILEŃSKI\n\nNa trasach linii 140, 245 i 738 pomiędzy przystankami w zespołach BIEŻUŃSKA a DW. WILEŃSKI obowiązują jedynie przystanki w zespole SZWEDZKA. Na trasie linii 527pomiędzy przystankami w zespołach METRO TROCKA a DW. WILEŃSKI również obowiązują jedynie przystanki w zespole SZWEDZKA.\n\nNa krańcu DW. WSCHODNI /KIJOWSKA/ dla linii 412obowiązywać będzie przystanek 09 zamiast 04.\n\nZawiesza się funkcjonowanie przystanków:\n\n- METRO TROCKA 07, 08, 09, 13\n- BRÓDNO-PODGRODZIE 03\n\nPrzywrócone zostanie funkcjonowanie przystanku DW. WSCHODNI /KIJOWSKA/ 09.\n\nPrzepraszamy za utrudnienia."

# text = 'Linia metra MA12 kursuje w pętli Młocin-Centrum, wyłączone stacje: STP KABATY, Młociny, Plac Wilsona, Politechnika'

console = Console()
console.print(text)