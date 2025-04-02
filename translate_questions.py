import json

# Charger les questions
with open('questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# Traductions des thèmes
theme_translations = {
    "Nemzeti jelképek és ünnepek": "Symboles nationaux et fêtes",
    "Történelmi események": "Événements historiques",
    "Irodalom és zene": "Littérature et musique",
    "Alkotmányos intézmények": "Institutions constitutionnelles",
    "Állampolgári jogok és kötelességek": "Droits et devoirs des citoyens",
    "Vegyes kérdések": "Questions diverses"
}

# Ajouter les traductions françaises
for q in questions:
    # Skip already translated questions
    if "theme_fr" in q:
        continue
        
    # Theme translation
    q["theme_fr"] = theme_translations.get(q["theme"], q["theme"])
    
    # Question translations (simplified - these would need real translations)
    if q["theme"] == "Nemzeti jelképek és ünnepek":
        if "magyar zászló" in q["question"]:
            q["question_fr"] = "Quelles sont les trois couleurs du drapeau hongrois ?"
            q["options_fr"] = ["Bleu, blanc, vert", "Rouge, blanc, vert", "Jaune, bleu, rouge"]
            q["correct_answer_fr"] = "Rouge, blanc, vert"
            q["explanation_fr"] = "Les couleurs du drapeau hongrois sont rouge, blanc et vert."
        elif "nemzeti himnusz" in q["question"]:
            q["question_fr"] = "Quel est le titre de l'hymne national hongrois ?"
            q["options_fr"] = ["Szózat", "Himnusz", "Magyar Dal"]
            q["correct_answer_fr"] = "Himnusz"
            q["explanation_fr"] = "Le titre de l'hymne national hongrois est simplement 'Himnusz', écrit par Ferenc Kölcsey en 1823, dont la musique a été composée par Ferenc Erkel."
        elif "Szent István" in q["question"]:
            q["question_fr"] = "Quelle fête est liée au roi Saint-Étienne ?"
            q["options_fr"] = ["15 mars", "20 août", "23 octobre"]
            q["correct_answer_fr"] = "20 août"
            q["explanation_fr"] = "Le 20 août est la fête du roi Saint-Étienne, qui est la fête nationale officielle de la Hongrie et commémore la fondation de l'État."
        elif "címer" in q["question"]:
            q["question_fr"] = "Quel est l'un des éléments importants des armoiries hongroises ?"
            q["options_fr"] = ["La couronne", "L'aigle", "Le soleil"]
            q["correct_answer_fr"] = "La couronne"
            q["explanation_fr"] = "La Sainte Couronne se trouve au sommet des armoiries hongroises, qui est un symbole de la souveraineté de la Hongrie."
        elif "1956" in q["question"]:
            q["question_fr"] = "Quelle fête nationale commémore la Révolution de 1956 ?"
            q["options_fr"] = ["15 mars", "20 août", "23 octobre"]
            q["correct_answer_fr"] = "23 octobre"
            q["explanation_fr"] = "Le 23 octobre est le jour commémoratif de la Révolution et Guerre d'Indépendance de 1956, qui est une fête nationale en Hongrie."
    
    elif q["theme"] == "Történelmi események":
        if "államot" in q["question"]:
            q["question_fr"] = "Quand l'État hongrois a-t-il été fondé ?"
            q["options_fr"] = ["896", "1000", "1526"]
            q["correct_answer_fr"] = "1000"
            q["explanation_fr"] = "L'État hongrois a été officiellement fondé en l'an 1000, lorsque le roi Étienne a été couronné, établissant ainsi le Royaume chrétien de Hongrie."
        elif "1848-49" in q["question"]:
            q["question_fr"] = "Quel événement a mis fin à la Révolution et Guerre d'Indépendance de 1848-49 ?"
            q["options_fr"] = ["La bataille de Mohács", "La reddition de Világos", "Le traité de Trianon"]
            q["correct_answer_fr"] = "La reddition de Világos"
            q["explanation_fr"] = "La Révolution et Guerre d'Indépendance de 1848-49 s'est terminée par la reddition de Világos le 13 août 1849, lorsque le général Artúr Görgei a déposé les armes devant les troupes russes."
        elif "trianoni" in q["question"]:
            q["question_fr"] = "Quand le traité de Trianon a-t-il été signé ?"
            q["options_fr"] = ["1918", "1920", "1945"]
            q["correct_answer_fr"] = "1920"
            q["explanation_fr"] = "Le traité de Trianon a été signé le 4 juin 1920, qui a attribué une grande partie du territoire historique de la Hongrie à d'autres pays."
        elif "forradalom" in q["question"] and "1956" in q["question"]:
            q["question_fr"] = "En quelle année la Révolution hongroise de 1956 a-t-elle eu lieu ?"
            q["options_fr"] = ["1945", "1956", "1989"]
            q["correct_answer_fr"] = "1956"
            q["explanation_fr"] = "La Révolution hongroise de 1956 a commencé le 23 octobre 1956 et a duré jusqu'au 10 novembre, quand elle a été écrasée par les troupes soviétiques."
        elif "rendszerváltás" in q["question"]:
            q["question_fr"] = "En quelle année le changement de régime a-t-il eu lieu en Hongrie ?"
            q["options_fr"] = ["1985", "1990", "1995"]
            q["correct_answer_fr"] = "1990"
            q["explanation_fr"] = "Le processus de changement de régime en Hongrie s'est déroulé en 1989-1990, avec les premières élections libres organisées au printemps 1990."

    elif q["theme"] == "Irodalom és zene":
        if "Szózat" in q["question"]:
            q["question_fr"] = "Qui a écrit le poème 'Szózat' ?"
            q["options_fr"] = ["Sándor Petőfi", "Mihály Vörösmarty", "János Arany"]
            q["correct_answer_fr"] = "Mihály Vörösmarty"
            q["explanation_fr"] = "Le poème patriotique 'Szózat' a été écrit par Mihály Vörösmarty en 1836, considéré comme le deuxième hymne national de la Hongrie après le 'Himnusz'."
        elif "Háry János" in q["question"]:
            q["question_fr"] = "Quel compositeur a écrit l'opéra 'Háry János' ?"
            q["options_fr"] = ["Béla Bartók", "Zoltán Kodály", "Franz Liszt"]
            q["correct_answer_fr"] = "Zoltán Kodály"
            q["explanation_fr"] = "L'opéra 'Háry János' a été composé par Zoltán Kodály en 1926, combinant la tradition des contes populaires hongrois avec la musique classique."
        elif "népzene" in q["question"]:
            q["question_fr"] = "Qui était l'un des plus importants collecteurs et chercheurs de musique folklorique hongroise ?"
            q["options_fr"] = ["Béla Bartók", "Ferenc Erkel", "Ernő Dohnányi"]
            q["correct_answer_fr"] = "Béla Bartók"
            q["explanation_fr"] = "Béla Bartók était l'un des plus importants collecteurs et chercheurs de musique folklorique hongroise, ayant collecté et systématisé des milliers de chansons populaires avec des méthodes scientifiques."
        elif "Egri csillagok" in q["question"]:
            q["question_fr"] = "Qui a écrit le roman 'Étoiles d'Eger' (Egri csillagok) ?"
            q["options_fr"] = ["Mór Jókai", "Géza Gárdonyi", "Kálmán Mikszáth"]
            q["correct_answer_fr"] = "Géza Gárdonyi"
            q["explanation_fr"] = "Le roman historique 'Étoiles d'Eger' a été écrit par Géza Gárdonyi en 1899, relatant le siège ottoman du château d'Eger en 1552."
        elif "Talpra magyar" in q["question"]:
            q["question_fr"] = "Quel célèbre poème hongrois commence par 'Talpra magyar, hí a haza!' ?"
            q["options_fr"] = ["Szózat", "Himnusz", "Nemzeti dal"]
            q["correct_answer_fr"] = "Nemzeti dal"
            q["explanation_fr"] = "Le 'Nemzeti dal' (Chant national) est un poème de Sándor Petőfi qui est devenu le symbole de la révolution du 15 mars 1848. Le poème commence par 'Talpra magyar, hí a haza!' (Debout, Hongrois, la patrie vous appelle!)."

    elif q["theme"] == "Alkotmányos intézmények":
        if "államfő" in q["question"]:
            q["question_fr"] = "Qui est le chef d'État hongrois ?"
            q["options_fr"] = ["Le Premier ministre", "Le Président de la République", "Le Président du Parlement"]
            q["correct_answer_fr"] = "Le Président de la République"
            q["explanation_fr"] = "Le chef d'État de la Hongrie est le Président de la République, élu par l'Assemblée nationale pour cinq ans."
        elif "képviselő" in q["question"]:
            q["question_fr"] = "Combien de députés siègent à l'Assemblée nationale hongroise ?"
            q["options_fr"] = ["199", "386", "120"]
            q["correct_answer_fr"] = "199"
            q["explanation_fr"] = "Depuis la réforme électorale de 2011, l'Assemblée nationale hongroise compte 199 députés (contre 386 auparavant)."
        elif "népképviseleti szerve" in q["question"]:
            q["question_fr"] = "Quel est l'organe principal de représentation populaire en Hongrie ?"
            q["options_fr"] = ["Le gouvernement", "L'Assemblée nationale", "Le bureau du Président de la République"]
            q["correct_answer_fr"] = "L'Assemblée nationale"
            q["explanation_fr"] = "L'organe principal de représentation populaire en Hongrie est l'Assemblée nationale, qui exerce le pouvoir législatif."
        elif "kormány feje" in q["question"]:
            q["question_fr"] = "Qui est le chef du gouvernement hongrois ?"
            q["options_fr"] = ["Le Président de la République", "Le Premier ministre", "Le Président de l'Assemblée nationale"]
            q["correct_answer_fr"] = "Le Premier ministre"
            q["explanation_fr"] = "Le chef du gouvernement hongrois est le Premier ministre, qui dirige le pouvoir exécutif et le gouvernement."
        elif "bíróság" in q["question"]:
            q["question_fr"] = "Quelle est la plus haute instance judiciaire de Hongrie ?"
            q["options_fr"] = ["La Cour constitutionnelle", "La Curia", "La Cour suprême"]
            q["correct_answer_fr"] = "La Curia"
            q["explanation_fr"] = "La plus haute instance judiciaire de Hongrie est la Curia, qui est au sommet du système judiciaire ordinaire. La Cour constitutionnelle est une institution constitutionnelle distincte."

    elif q["theme"] == "Állampolgári jogok és kötelességek":
        if "szavazhatnak" in q["question"]:
            q["question_fr"] = "À partir de quel âge les citoyens hongrois peuvent-ils voter ?"
            q["options_fr"] = ["16", "18", "21"]
            q["correct_answer_fr"] = "18"
            q["explanation_fr"] = "Les citoyens hongrois peuvent voter à partir de 18 ans aux élections parlementaires et municipales, ainsi qu'aux référendums."
        elif "NEM tartozik" in q["question"]:
            q["question_fr"] = "Lequel de ces éléments N'EST PAS un devoir fondamental des citoyens ?"
            q["options_fr"] = ["Obligation de défense nationale", "Paiement des impôts", "Adhésion à un parti politique"]
            q["correct_answer_fr"] = "Adhésion à un parti politique"
            q["explanation_fr"] = "L'adhésion à un parti politique n'est pas un devoir fondamental des citoyens, c'est entièrement volontaire. Les devoirs fondamentaux comprennent l'obligation de défense nationale, le paiement des impôts et l'obligation scolaire."
        elif "állampolgárság megszerzésének" in q["question"]:
            q["question_fr"] = "Quelle est l'une des façons d'acquérir la citoyenneté hongroise ?"
            q["options_fr"] = ["Naissance", "Travail", "Visa touristique"]
            q["correct_answer_fr"] = "Naissance"
            q["explanation_fr"] = "L'une des façons fondamentales d'acquérir la citoyenneté hongroise est la naissance : l'enfant d'un citoyen hongrois obtient automatiquement la citoyenneté hongroise."
        elif "tankötelezettség" in q["question"]:
            q["question_fr"] = "Jusqu'à quel âge dure l'obligation scolaire en Hongrie ?"
            q["options_fr"] = ["14", "16", "18"]
            q["correct_answer_fr"] = "16"
            q["explanation_fr"] = "En Hongrie, l'obligation scolaire dure jusqu'à l'âge de 16 ans (auparavant, c'était 18 ans)."
        elif "véleménynyilvánítást" in q["question"]:
            q["question_fr"] = "Quel droit fondamental garantit la libre expression des opinions ?"
            q["options_fr"] = ["Droit de vote", "Liberté d'expression", "Liberté de mouvement"]
            q["correct_answer_fr"] = "Liberté d'expression"
            q["explanation_fr"] = "La liberté d'expression est le droit démocratique fondamental qui garantit que les citoyens peuvent exprimer librement leurs opinions."

    elif q["theme"] == "Vegyes kérdések":
        if "folyó" in q["question"]:
            q["question_fr"] = "Quelle rivière traverse Budapest ?"
            q["options_fr"] = ["Tisza", "Danube", "Rába"]
            q["correct_answer_fr"] = "Danube"
            q["explanation_fr"] = "Le Danube traverse Budapest, c'est le plus long fleuve de Hongrie et il divise la capitale en parties Buda et Pest."
        elif "hivatalos nyelve" in q["question"]:
            q["question_fr"] = "Quelle est la langue officielle de la Hongrie ?"
            q["options_fr"] = ["Hongrois", "Anglais", "Allemand"]
            q["correct_answer_fr"] = "Hongrois"
            q["explanation_fr"] = "La langue officielle de la Hongrie est le hongrois, qui appartient à la famille des langues finno-ougriennes."
        elif "legnagyobb tó" in q["question"]:
            q["question_fr"] = "Quel est le plus grand lac de Hongrie ?"
            q["options_fr"] = ["Lac Velence", "Lac Balaton", "Lac Fertő"]
            q["correct_answer_fr"] = "Lac Balaton"
            q["explanation_fr"] = "Le lac Balaton est le plus grand lac de Hongrie et d'Europe centrale, souvent appelé la 'mer hongroise'."
        elif "fizetőeszköze" in q["question"]:
            q["question_fr"] = "Quelle est la monnaie de la Hongrie ?"
            q["options_fr"] = ["Euro", "Forint", "Couronne"]
            q["correct_answer_fr"] = "Forint"
            q["explanation_fr"] = "La monnaie officielle de la Hongrie est le forint (Ft ou HUF), qui est la monnaie du pays depuis 1946."
        elif "ételt" in q["question"]:
            q["question_fr"] = "Quel plat hongrois est considéré comme le plat national ?"
            q["options_fr"] = ["Goulash", "Chou à la székely", "Chou farci"]
            q["correct_answer_fr"] = "Goulash"
            q["explanation_fr"] = "Le goulash est le plat hongrois le plus connu internationalement, souvent considéré comme un symbole de la cuisine hongroise."

# Sauvegarder les questions avec traductions
with open('questions.json', 'w', encoding='utf-8') as file:
    json.dump(questions, file, ensure_ascii=False, indent=2)

print("Traduction terminée !")