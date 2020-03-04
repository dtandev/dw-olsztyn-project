def candidates():
    candidatesDictionary = {
        #Initials : [First_name, Last_name, Club, Last_seen, 'TV_station', Total_time, Last_screenshot]
        'AD': ['Andrzej', 'Duda', 'Bezpartyjny', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Prezydent_Rzeczypospolitej_Polskiej_Andrzej_Duda.jpg/240px-Prezydent_Rzeczypospolitej_Polskiej_Andrzej_Duda.jpg'],
        'MKB' : ['Małgorzata', 'Kidawa-Błońska', 'Platforma Obywatelska', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Kidawa-B%C5%82o%C5%84ska_%28cropped%29.jpg/240px-Kidawa-B%C5%82o%C5%84ska_%28cropped%29.jpg'],
        'SH' : ['Szymon', 'Hołownia', 'Bezpartyjny', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/02019_%283%29_Szymon_Ho%C5%82ownia.jpg/166px-02019_%283%29_Szymon_Ho%C5%82ownia.jpg'],
        'RB' : ['Robert', 'Biedroń', 'Wiosna / Nowa Lewica','b/d', 'b/d', 'b/d',  'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Robert_wiki.png/240px-Robert_wiki.png'],
        'WKK' : ['Władysław', 'Kosiniak-Kamysz', 'Polskie Stronnictwo Ludowe', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/W%C5%82adys%C5%82aw_Kosiniak-Kamysz_Sejm_2016.JPG/163px-W%C5%82adys%C5%82aw_Kosiniak-Kamysz_Sejm_2016.JPG'],
        'KB' : ['Krzysztof', 'Bosak', 'Konfederacja / Ruch Narodowy', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/JKRUK_20190927_KRZYSZTOF_BOSAK_KIELCE_IMGP2283.jpg/209px-JKRUK_20190927_KRZYSZTOF_BOSAK_KIELCE_IMGP2283.jpg'],
        'PLM' : ['Piotr', ' Liroy-Marzec', 'Skuteczni', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Piotr_Liroy-Marzec_Sejm_2016a.jpg/168px-Piotr_Liroy-Marzec_Sejm_2016a.jpg'],
        'LS' : ['Leszek', 'Samborski', 'Odpowiedzialność', 'b/d', 'b/d', 'b/d', 'https://portalniezalezny.pl/wp-content/uploads/2016/05/leszek_samobrski.jpg'],
        'PB' : ['Piotr', 'Bakun', 'Bezpartyjny', 'b/d', 'b/d', 'b/d', 'https://scontent.fwaw5-1.fna.fbcdn.net/v/t1.0-9/43248180_340778723157575_4132832989245603840_n.png?_nc_cat=100&_nc_oc=AQmnsAjKoKb3pMRLc0q626fo64-Nr_dxI9DQl4QVONXckCPINnh77CJHUY_T5fJElL8&_nc_ht=scontent.fwaw5-1.fna&oh=5c22ef03e08609abaee81b7739d6c552&oe=5F02CDF5'],
        'SZ' : ['Stanisław', 'Żółtek', 'Kongres Nowej Prawicy / PolEXIT', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Stanis%C5%82aw_%C5%BB%C3%B3%C5%82tek.JPG/180px-Stanis%C5%82aw_%C5%BB%C3%B3%C5%82tek.JPG'],
        'WP' : ['Wojciech', 'Podjacki', 'Liga Obrony Suwerenności', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Wojciech_Podjacki.JPG/800px-Wojciech_Podjacki.JPG'],
        #'MP' : ['Mirosław', ' Piotrowski', 'Ruch Prawdziwa Europa - Europa Christi', 'b/d', 'b/d', 'b/d', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Miros%C5%82aw_Piotrowski_%28Martin_Rulsch%29_1.jpg/152px-Miros%C5%82aw_Piotrowski_%28Martin_Rulsch%29_1.jpg'],
        #'AV' : ['Andrzej', ' Voigt', 'Bezpartyjny', 'b/d', 'b/d', 'b/d', '']
        }
    return candidatesDictionary

def candidates_color_mapping(candidates):
    colors = px.colors.qualitative.Light24
    candidatesNames = ['{} {}'.format(candidates[candidate][0], candidates[candidate][1]) for candidate in candidates]
    candidates_color_map = dict(zip(candidatesNames, colors))
    return candidates_color_map