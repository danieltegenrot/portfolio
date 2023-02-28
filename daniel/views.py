from django.shortcuts import render

# Create your views here.
def page(request, page):

    header = ""
    welcome_text = ""
    first_text_box = ""
    second_text_box = ""
    third_text_box = ""
    about_text_button = True
    about_code_button = True
    about_visuals_button = True
    no_text_box = None

    if page == "portfolio":
        header = "Portfolio"
        welcome_text = f"<p class='big-text'>Hej!<br/><br/> Jag är en av de stjärnor som ser till att webben blir en snyggare och roligare plats att vara på.</p>"
        first_text_box = f"<p class='text-box'>Front end och UX är mina spetsområden. Jag jobbar lika bra i Figma som i exempelvis React och har erfarenhet av CMS-system såsom Wordpress.</p>"
        second_text_box = f"<p class='text-box'>Genom att kombinera <a href='/portfolio/text' class='about-text-link'>innehållsrik text</a>, <a href='/portfolio/kod' class='about-code-link'>lättförstådd kod</a> och <a href='/portfolio/grafik' class='about-visuals-link'>målande grafik</a> skapar jag engagerande och intressanta webb-sajter som är för alla.</p>"
        third_text_box = f"<p class='text-box'>De senaste två projekten jag jobbade på var <a target='_blank' href='https://halsomedicinsktcenter.se' class='normal-text-link'>Hälsomedicinskt Center</a> som driver vårdcentraler runtom i Skåne, samt <a target='_blank' href='https://bokningssystem.boka.se/' class='normal-text-link'>Boka</a> som är en av sveriges största bokningssajter.</p>"
    elif page == "text":
        header = "Innehållsrik text"
        welcome_text = f"<p class='big-text'>Innehållsrik text är inte text med många ord, utan ord med mycket mening.</p>"
        first_text_box = f"<p class='text-box'>Att säga mycket på liten yta är ofta väsentligt för flödet på en webb-sajt att kännas naturligt och engagerande. Jag har två år på skrivarskola bakom mig och hjälper gärna till med texter och rubriksättning.</p>"
        second_text_box = f"<p class='text-box'>Jag hjälpte till med copyn åt <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-text-link'>halsomedcinsktcenter.se</a> där en stor del av jobbet var att sammanfatta tjänsten tydligt efter de designbeslut vi satte ut.</p>"
        third_text_box = f"<p class='text-box'>Likaså tog jag mycket ansvar över <a target='_blank' href='https://bokningssystem.boka.se' class='about-text-link'>bokningssystem.boka.se</a> och satte texter samt såg till att det stora utbudet av innehåll kändes sammanhängande och lättbegripligt.</p>"
        about_text_button = False
    elif page == "kod":
        header = "Lättförstådd kod"
        welcome_text = f"<p class='big-text'>Bra kod bör flöda som texten i en bok. Den ska vara lätt att läsa. Inte göra jobbet med så få tecken som möjligt.</p>" 
        first_text_box = f"<p class='text-box'>Jag har suttit mycket med HTML, CSS/Sass, Bootstrap, Javacsript, React m. fl. Jag har en del erfarenhet av att sätta upp CMS-databaser men håller mig gärna på frontend-sidan av webben.</p>" 
        second_text_box = f"<p class='text-box'>Jag hade ansvar för frontend på <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-code-link'>halsomedicinsktcenter.se</a> när sidan byggdes om och jag var även med och byggde om framsidan åt <a target='_blank' href='https://boka.se' class='about-code-link'>boka.se</a> från grunden.</p>"
        third_text_box = f"<p class='text-box'>Den här sajten är byggd med Django och Python. <a target='_blank' href='https://github.com/danieltegenrot/portfolio' class='about-code-link'>GitHub</a></p>"
        about_code_button = False
    elif page == "grafik":
        header = "Målande grafik"
        welcome_text = f"<p class='big-text'>En bild säger ju mer än tusen ord så...</p>"
        no_text_box = f"<p class='space-underneath'>Psst! Kika gärna in på <a target='_blank' href='https://halsomedicinsktcenter.se' class='about-visuals-link'>halsomedicinsktcenter.se</a> som jag designat helt från grunden.</p>"
        about_visuals_button = False

    return render(request, "daniel/index.html", {
        "page": page,
        "header": header,
        "welcome_text": welcome_text,
        "first_text_box": first_text_box,
        "second_text_box": second_text_box,
        "third_text_box": third_text_box,
        "no_text_box": no_text_box,
        "about_text_button": about_text_button,
        "about_code_button": about_code_button,
        "about_visuals_button": about_visuals_button
    })


