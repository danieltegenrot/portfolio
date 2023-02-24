from django.shortcuts import render

# Create your views here.
def page(request, page):

    header = ""
    content = ""
    about_text_button = True
    about_code_button = True
    about_visuals_button = True

    if page == "portfolio":
        header = "Portfolio"
        content = f"<p>Hej!<br/><br/> Jag är en av de stjärnor som ser till att webben blir en snyggare och roligare plats att vara på.<br><br> Genom att kombinera <a href='/portfolio/text' class='about-text-link'>innehållsrik text</a>, <a href='/portfolio/kod' class='about-code-link'>lättförstådd kod</a> och <a href='/portfolio/grafik' class='about-visuals-link'>målande grafik</a> skapar jag webb-sajter som är för alla.<br><br> Detta innebär såklart 100% på Chrome Lighthouse, gamification-element för att liva upp stämningen och ett gott öga för hur text och bild smälter samman.</p>"
    elif page == "text":
        header = "Innehållsrik text"
        content = f"<p>Innehållsrik text är inte text med många ord, utan ord med mycket mening. Att säga mycket på liten yta är ofta väsentligt för flödet på en webb-sajt att kännas naturligt och engagerande.<br/><br/> Jag har två år på skrivarskola bakom mig och hjälper gärna till med texter och rubriksättning. <br/><br/> Jag hjälpte till med copyn åt <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-text-link'>halsomedcinsktcenter.se</a> där en stor del av jobbet var att sammanfatta tjänsten tydligt efter de designbeslut vi satte ut. <br/><br/> Likaså tog jag mycket ansvar över <a target='_blank' href='https://bokningssystem.boka.se' class='about-text-link'>bokningssystem.boka.se</a> och satte texter samt såg till att det stora utbudet av innehåll kändes sammanhängande och lättbegripligt.</p>"
        about_text_button = False
    elif page == "kod":
        header = "Lättförstådd kod"
        content = f"<p>Bra kod, tror jag, bör flöda ungefär som texten i en bok. Den ska vara lätt att läsa. Inte göra jobbet med så få tecken som möjligt.<br/><br/> Jag försöker alltid se till att kod som jag lämnar över ska vara lika begriplig för någon annan som för mig. Jag är fluent i HTML, CSS/Sass, Bootstrap, Javacsript, React m. m.<br/><br/> Jag har en del erfarenhet av att få CMS-verktyg att funka bra med resten av koden men jag håller mig gärna på frontend-sidan av webben.<br/><br/> Jag hade ansvar för frontend på <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-code-link'>halsomedicinsktcenter.se</a> när sidan byggdes om och jag var även med och byggde om framsidan åt <a target='_blank' href='https://boka.se' class='about-code-link'>boka.se</a> från grunden.<br/><br/> Den här sajten är byggd med Django och Python.</p>"
        about_code_button = False
    elif page == "grafik":
        header = "Målande grafik"
        content = f"<p>En bild säger ju mer än tusen ord så... <br/><br/>Psst! Kika gärna in på <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-visuals-link'>halsomedicinsktcenter.se</a> som jag designat helt från grunden.</p>"
        about_visuals_button = False

    return render(request, "daniel/index.html", {
        "page": page,
        "header": header,
        "content": content,
        "about_text_button": about_text_button,
        "about_code_button": about_code_button,
        "about_visuals_button": about_visuals_button
    })


