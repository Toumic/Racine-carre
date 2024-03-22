#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Nombre au carré << nombre12carre3.py >>


from decimal import *
import inspect

line_no = lambda: inspect.currentframe().f_back.f_lineno


def equagene(nbr):
    global mm, mo, mi

    def resume():
        print("""Le nombre_carre utilise le module decimal...
        La racine carrée réelle a forme générique
        Pour les opérations et les comparaisons
        Le traité se porte sur le nombre (ex:13.25)
        Les nombres négatifs en string dans le code
        Au vu du capable complexe de nombre_carre...
        Précision décimale aidant le nombre calculé
            La racine carrée réelle de : 3**2
            ou bien de : (42-32)**-2
        Prémice de nouvelles formes opératoires
        Autorités en terme général tant que logiques""")

    def espec6(ome):
        """ Séparation décimale pour typage *(_%6_)*
        # *(_TableTypeGénéral = [0,1,2,3,4,5]_)*
        # Type 6 est Supérieur à *(_TTG_)*"""

        # Recherche du point décimal
        if '.' in ome:
            nentie = 0  # Poids.Entier.fort
            for me in ome:
                nentie += 1
                if me == '.':
                    break
        else:
            # Nombre.Entier
            nentie = len(str(int(ome)))  # Poids.Entier.faible

        nmasse = len(ome)  # Masse.Nombre
        nmedif = nmasse - nentie  # Mesure.Decimale
        ndecim = ome[nentie:]  # Masse.Decimale
        # Mesure.Decimale
        if nmedif != 0:
            fnd = 0
            for nd in ndecim:
                fnd += int(nd)  # Addition ndecim(nd)
                if fnd != 0:  # Somme positive
                    decim6[0] = int(ndecim) % 6
                    # Condition nombre négatif
                    if ome[0] == '-':
                        decim6[0] = int(str('-' + str(decim6[0])))
                    break

    def opera(nop):
        """Fonction opératoire"""

        def addition(i, j):
            return i + j

        def soustraction(i, j):
            return i - j

        def multiplie(i, j):
            return i * j

        def expose(i, j):
            return i ** j

        def division(i, j):
            return i / j

        def diventier(i, j):
            return i // j

        def modulo(i, j):
            return i % j

        signe = {'+': addition, '-': soustraction, '*': multiplie,
                 '**': expose, '/': division, '//': diventier,
                 '%': modulo}
        getcontext().prec = len(nop) * 50
        nbr1 = Decimal(nop[0])
        operation = signe[nop[1]]
        nbr2 = Decimal(nop[2])
        opombre[0] = str(operation(nbr1, nbr2))
        if 'E' in opombre[0] or 'e' in opombre[0]:
            op_e = []
            op_o = len(opombre[0])
            for ie in range(op_o - 1, 0, -1):
                if opombre[0][ie] in ("E", '+', '-'):
                    break
                else:
                    op_e.append(opombre[0][ie])
            op_r = list(reversed(op_e))
            op_j = (''.join(str(o0a) for o0a in op_r))
            getcontext().prec = int(op_j) + op_o
            opombre[0] = str(operation(nbr1, nbr2))

    def nombre_carre(nbrequa):
        """ Cette fonction produit la racine carrée du nombre, et
        elle commence par définir la partie entière de la racine².
        Qui en général a une virgule  flottante ( point  décimal )
        La polarité du nombre signé, forme une transition (+-)
            Analyse de la surface(Typique = Nombre % 6)
                1 = 7 % 6       :7%6: Pôle positif naturel
                -1 = -7 % -6    :-7%-6: Pôle négatif naturel
                5 = -7 % 6      :-7%6: Transit positif naturel
                -5 = 7 % -6     :7%-6: Transit négatif naturel
        """

        nbrequa = Decimal(nbrequa)
        if nbrequa <= -0:
            nbrequa = Decimal(str(nbrequa)[1:])
            rondeur[1] = 1

        # Précision.Allusion.Illusion.
        premax = 100000000
        """ Modulation unaire"""
        if len(str(nbrequa)) < 10:
            precision = (len(str(nbrequa)) + 1) * 10
            precisive = '(*10)'
        elif 10 <= len(str(nbrequa)) < 50:
            precision = int(len(str(nbrequa)) ** 2)
            precisive = '(**2)'
        elif 50 <= len(str(nbrequa)) < 100:
            precision = int(len(str(nbrequa)) ** 1.75)
            precisive = '(**1.75)'
        elif 100 <= (int(len(str(nbrequa)))) < premax:
            precision = int(len(str(nbrequa)) ** 1.25)
            precisive = '(**1.25)'
        else:
            return
        getcontext().prec = precision
        # Maximum(machine locale) = 100000000

        # Racine² décimale entière
        wh = int(nbrequa ** Decimal(.5))
        wh0 = (nbrequa ** Decimal(.5))
        nbu = nbrequa

        # Secteur décimal
        decitab = []
        if rondeur[1] == 1:
            entiere[0] = str('-' + str(wh))
        else:
            entiere[0] = str(wh)
        print('entiere =', entiere[0])

        www = nbrdec = nc = top = 0
        while image[0] ** 2 <= nbrequa and top == 0:
            for img in range(1, 10):
                if decitab:
                    image[0] = Decimal(entiere[0] + '.' + recital[0] + str(img))
                else:
                    if not nc:
                        nbrdec += 1  # Unité décimale
                        nc = 1
                    image[0] = Decimal(entiere[0] + '.' + str(img))

                if image[0] ** 2 > nbrequa:
                    decitab.append(img - 1)
                    nbrdec += 1  # Nombre de décimales
                    recital[0] = (''.join(str(d) for d in decitab))
                    image[0] = Decimal(entiere[0] + '.' + recital[0])
                    if image[0] ** 2 == nbrequa:
                        rondeur[0] = 'Juste racine² | nbr |'
                        top = 1
                        break
                    break
                elif img == 9:
                    if image[0] ** 2 == nbrequa:
                        rondeur[0] = 'Juste racine² | i9 |'
                        top = 1
                        break
                    decitab.append(img)
                    nbrdec += 1  # Nombre de décimales
                    recital[0] = (''.join(str(d) for d in decitab))
                    image[0] = Decimal(entiere[0] + '.' + recital[0])
                elif image[0] ** 2 == nbrequa:
                    rondeur[0] = 'Juste racine² | elif |'
                    top = 1
                    recital[0] = str(image[0])[len(entiere[0]) + 1:]
                    break

            # print(www, '°°° **2 =', image[0] ** 2)
            www += 1
        else:
            if len(str(rondeur[0])) < 1:
                rondeur[2] = 'Variant racine² | not |'
            nb0 = str(int(nbrequa) % 6)
            if rondeur[1] == 1:
                nbrequa = Decimal('-' + str(nbrequa))
                wh0 = Decimal('-' + str(wh0))
                nb0 = '-' + nb0
            sq0 = wh0
            if decim6[0] < 6:
                print('Rnombre =', nbrequa, ';typo =',
                      [nb0, '.', str(decim6[0])])
            else:
                print('Rnombre =', nbrequa, ';typo =', [nb0])
            if sq0 ** 2 == nbu:
                print('_Rreelle_juste =', sq0)
            else:
                print('_Rracine =', sq0)
            print('*... (', nbrdec, ') Precision', precision, precisive)

    # Nombre a forme décimale __________________________________
    """ Une décimale au format texte a un meilleur suivi """
    # :nombre = '22135323.12554':
    #  imageoo2 = 22135323.125540000000000000000000000000000000...
    # ...00000000000000000000000000000000000000000000000000000000
    # :nombre = 22135323.12554:
    #  imageoo2 = 22135323.125539999455213546752929687500000000...
    # ...00000000000000000000000000000000000000000000000000000000
    """."""  # __________________________________________________

    # Dispatchage des précisions
    nombre = nbr  # Réception nombre
    nombre = '(' + nombre + ')'  # Parent globe

    # Mathématique sur nombres
    opsigne = ['+', '-', '%', '*', '/', '**', '//']  # Signes math
    opforme = ['(', ')', '=']  # Formes math
    opobjet = ''.join(str(o) for o in range(10)) + '.'
    oparfer = []  # Parenthèses fermantes
    oparouv = []  # Parenthèses ouvrantes
    opaprio = []  # Priorités parenthèses
    optrucs = []  # Collecte signes
    opblanc = []  # Collecte blancs
    opautre = []  # Collecte autres
    opchiff = []  # Collecte chiffres
    opimage = []  # Points réalisés
    opserie = {}  # Collecte nombres à calculer
    opombre = {0: ''}  # Nombre calculé

    print(line_no(), 'nombre =', nombre, '  # = 45')

    # Décomposition du nombre
    n0n = 0
    for no in nombre:
        if no in opforme:
            if no == '(':
                oparouv.append(n0n)  # Contrôle parenthèses
            else:
                oparfer.append(n0n)
            opimage.append(no)
        elif no in opsigne:
            optrucs.append(n0n)
            opimage.append(no)
        elif no in opobjet:
            opchiff.append(n0n)
            opimage.append(n0n)
        elif no == ' ':
            opblanc.append(n0n)
            opimage.append(no)
        else:
            opautre.append(n0n)
            opimage.append(no)
        n0n += 1
    print()
    print('oparouv', oparouv, 'oparfer', oparfer)
    print('optrucs', optrucs, 'opblanc', opblanc)
    print('opimage', opimage, '\nopchiff', opchiff,
          'opautre', opautre)
    print('______________________________', )

    # Positions des parenthèses ?(())?
    optotal = len(nombre)  # Blancs inclus
    oparent = len(oparouv)  # Quantité stage
    opstage = [[]] * oparent
    rentage = []  # Priorité cycle
    o1 = o3 = 0
    for ouv in range(oparent):
        o1 -= 1
        parouv = oparouv[o1]
        aro = o2 = parouv
        #print('ouv', parouv)
        while o2 < optotal:
            aro += 1
            if aro in oparfer:
                #print('aro', aro)
                for ops in opstage:
                    if aro in ops:
                        break
                else:
                    o3 -= 1
                    opstage[o3] = [parouv, aro]
                    # print('opstage', opstage[o3])
                    break
            o2 += 1

    # Traitement des signes ?(**,//)?
    signes = []
    s0s = ''
    o0 = 0
    if optrucs:
        while 1:
            if o0 < len(optrucs) - 1 \
                    and optrucs[o0 + 1] - optrucs[o0] == 1:
                s0s += nombre[optrucs[o0]]
                s0s += nombre[optrucs[o0 + 1]]
                if s0s in opsigne:
                    s1s = optrucs[o0], s0s
                    signes.append(s1s)
                    s0s = ''
                    o0 += 1
                else:
                    s1s = optrucs[o0], s0s[:-1]
                    signes.append(s1s)
                    s0s = ''
            else:
                s0s += nombre[optrucs[o0]]
                s1s = optrucs[o0], s0s
                signes.append(s1s)
                s0s = ''
            if o0 == len(optrucs) - 1:
                print('signes =', signes)
                break
            o0 += 1

    # Composition des plages opérationnelles
    if opstage:
        opnuage = {}  # Espace opérationnel
        opcompe = []  # Plagiat des plages

        print()
        # Inclusion des parenthèses
        priospa = {}
        priopro = []  # Borne parenthèse
        oeoe = 0  # Rang opstage[oeoe]=[min,max]
        for opeve in opstage:
            # Groupe change
            if min(opstage[oeoe]) > max(opstage[oeoe-1]):
                opoe = oeoe, opstage[oeoe]
                priopro.append(opoe)  # Premier stage
                # print('.in>ax',max(opstage[oeoe-1]), min(opstage[oeoe]))
            oeoe += 1
            #print('opeve', opeve)
        print('priopro',priopro)        
        # Définition borne
        priofin = []
        for prioeoe in priopro:
            #print('prioeoe',prioeoe[1][0])
            for priogag in opstage:
                #print('priogag',priogag)
                if prioeoe[1][0] < priogag[0] \
                   and prioeoe[1][1] > priogag[1]:
                    # rentage.append(priogag[0])
                    # rentage.append(prioeoe[1][0])
                    priofin.append(priogag)
                    priofin.append(prioeoe[1])
                    print('priogag',priogag)
                    print('prioeoe',prioeoe)
            #print('prioeoe',prioeoe)



            
        
        """# Séquence des mesures
        # priofin = []
        for oprev in sorted(priospa.values()):
            priofin.append(oprev)"""
        print('priofin',priofin)






        print()
        # Groupes parenthèses
        print('opstage', opstage)
        
        
        print()
        #print('priofin', priofin)
        # Production des plages
        for oprev in priofin:
            optreve = []
            print('oprev', oprev)
            
            for rev in range(yop[0], yop[1]):
                if rev not in opcompe:
                    opcompe.append(rev)
                    optreve.append(rev)
            # else: rev a sa plage
            opnuage[yop] = optreve
            # rentage.append(oprev[0])
            print(line_no(), 'plagiopnuage', yop, opnuage[yop])
        print('Plages opnuage', opnuage)
        # Priorité des opérations :opaprio:
        # priospa = {}  # Niveaux d'entre parenthèses
        # priofin = {}  # Local Masse Type
        priobis = {}  # Local couple
        priouno = {}  # Local unique
        priosig = []  # Signe unique
                    
        # print('368 .priofin', priofin)
        for p0r, p1r in opnuage.items():
            pass
            # print()
                        
                        






        

        # Image génération
        for eve, ver in opnuage.items():
            opono = []
            ono = ''
            o0o = 0
            e0n = [0]
            # print()
            # print(eve,ver)
            # (eve,ver)
            for opv in ver:
                # print('*opv',opv)
                if opimage[opv] in opchiff:
                    if ono:
                        if e0n[0]:
                            opv2 = e0n[0] - 1
                        else:
                            opv2 = opv - 2
                        # print('_opchiff.if.ono',ono,'OPV2',opv2,'EON',e0n)
                        for v2 in range(opv2, 0, -1):
                            if v2 in oparfer:
                                opono.append(ono)
                                # print(' __opchiff.oparfer.ono',ono,'v2',v2)
                                ono = ''
                                break
                            elif v2 in opchiff and ono in opsigne:
                                opono.append(ono)
                                ono = ''
                                # print(' __opchiff.opchiff.ono',ono,'v2',v2)
                                break
                            elif v2 in optrucs:
                                # pass
                                # print(' __opchiff.optrucs.ono',ono,'v2',v2)
                                break
                    ono += nombre[opimage[opv]]
                    # print('_opchiff.for.ono',ono,'opono', opono)
                elif opv in optrucs:
                    if ono:
                        opono.append(ono)
                        # print('...truc.ono.opono', opono,'opv',opv)
                        ono = ''
                    for truc in signes:
                        if opv in truc:
                            # print('...Sopv',opv,'truc',truc)
                            for vp in range(truc[0]):
                                if opv in opblanc:
                                    pass
                                elif opv in optrucs:
                                    ono += truc[1]
                                    # print(opv,'...truc.elif.opono', opono,ono)
                                    o0o += 1
                                    e0n[0] = opv
                                    break
                            else:
                                opono.append(truc[1])
                                # print('...truc.else.opono', opono)
                                ono = ''
                        else:
                            pass
                            # print('...truc.else.opono', opono,'opv',opv)
                    if not o0o:
                        ono = ''
                # FIN elif opv in optrucs:
            if ono:
                opono.append(ono)
                # print('Image.opono', opono,'opv',opv)

            if opono:
                # print('_____opono',opono,'len(opono)',len(opono))
                # p0p[0] = 1
                if len(opono) < 3:
                    if len(opono) == 1:
                        oopoo = opono[0]
                        opono = []
                        # print('ver[0]',ver[0])
                        for oo in range(3):
                            if oo == 1:
                                opono.append(oopoo)
                            else:
                                opono.append('')
                        opono = ver[0], 'mnon', opono
                        # print('mnon_____opono',opono)
                    elif opono[0] in opsigne:
                        opono = ver[0], 'gnon', opono
                        # print('gnon_____opono',opono[0])
                    else:
                        opono = ver[0], 'dnon', opono
                        # print('dnon_____opono',opono[0])
                elif len(opono) == 3 and opono[1] != 'mnon':
                    # p0p[0] += 1
                    opono = ver[0], 'oui', opono
                    opombre[ver[0]] = opono[-1]
                    # opombre[1] = opono[-1]
                    """print(' ELSEopono', opono[1], 'p0p',p0p,' ',ver[0],
                          '\n opombre',opombre)"""
                """if p0p[0] > 0:
                    print('IFp0p', opono, 'p0p',p0p,'opombre',opombre)"""
                opserie[opono[0]] = opono[1:]
                # print('FIN_ _ _opono',opono[1:],'.',opono)
            """else:
                print('ZZZZZZZZZZZZZZZZZZZ')
                opono = []"""
        # print()
        # print('_ | _ opserie',opserie)

        if opserie:
            # print()
            # print('m _   opserie',opserie)
            # op0po = 0
            # print('m _ op0po',op0po,'opombre',opombre)
            print()
            print('rentage',rentage)
            for oo in rentage:
                # print()
                # print('rentage',rentage)
                print(line_no(), 'M _ rentage', oo, '  opserie', opserie[oo][1])
                if opserie[oo][0][1:] == 'non':
                    if opombre[0]:
                        if opserie[oo][0][:-3] == 'm':
                            print('MO', opserie[oo][1], 'oo', oo)
                            for mm in signes:
                                if mm[1] in opserie[oo][1]:
                                    print('mm[1]',mm[1],mm[0])
                                    break
                            print('mm[0]',mm[0])
                            for mo in range(mm[0], oo, -1):
                                print('MO', mo)
                                if mo in rentage:
                                    print('MO', mo)
                                    break
                                else: print('MO', mo)
                            # print('max(rentage)',max(rentage),rentage)
                            print('mo,oo',mo,oo)
                            if mo: print(531, 'not mo')
                            for mi in range(mo + 1, max(rentage) + 1):
                                if mi in rentage:
                                    print('MI', mi)
                                    break

                            # print('opnuage',opnuage)
                            # print('opombre', opombre,'OmoO', mo)
                            # print('opombre', opombre,'OmiO', mi)
                            opgrade = [opombre[mo], opserie[oo][1][1],
                                       opombre[mi]]
                            print('opgrade', opgrade)
                            opera(opgrade)
                        elif opserie[oo][0][:-3] == 'g':
                            opgrade = [opombre[0]]
                            for opgr in opserie[oo][-1]:
                                opgrade.append(opgr)
                            print('opgrade', opgrade)
                            opera(opgrade)
                        else:
                            opgrade = []
                            for opgr in opserie[oo][-1]:
                                opgrade.append(opgr)
                            opgrade.append(opombre[0])
                            print('opgrade', opgrade)
                            opera(opgrade)
                else:
                    # print('opserie', opserie[oo][1])
                    opera(opserie[oo][1])
                    opombre[oo] = opombre[0]

    if opombre[0] != '':
        nombre = opombre[0]

    # Séparation décimale pour typage(%6)
    decim6 = [6]
    espec6(nombre)

    image = {0: 0}  # Dico.Nombre réel
    rondeur = {0: '', 1: 0}  # Dico.Comment
    entiere = {0: ''}  # Dico.Racine.Entier
    recital = [0]  # Table.Décimale

    nombre_carre(nombre)  # Appel principal

    if recital[0] != 0:
        recital[0] = str(image[0])[len(entiere[0]) + 1:]
    print('Rrecital =', recital[0], '\n...*')
    oo2 = image[0] ** 2
    if rondeur[1] == 1:
        oo2 = Decimal('-' + str(oo2))
    print('Iimageoo1 =', image[0], '\n..**',
          '\nIimageoo2 =', oo2)
    print('.***')
    if image[0]:
        if rondeur[0]:
            print('Rondeur 0:', rondeur[0])
        elif rondeur[2]:
            print('Rondeur 2:', rondeur[2], '\nReste =',
                  Decimal(nombre) - ((image[0]) ** 2))
        else:
            rondeur[0] = 'Valeur intervalle'
            print('Rondeur 0:', rondeur[0], '\nReste =',
                  Decimal(nombre) - ((image[0]) ** 2))
    else:
        if float(nombre) == 0:
            print('Rrondeur : Juste réro limite | zéro |')
        else:
            print('Rrondeur : Juste hors limite | premax |')

    resume()


if __name__ == '__main__':
    # Jeux des parnthèses
    # parent = '16*(12**((5 ** -2)*8))'  # n+(n+((n+n)+n))
    # parent = '562+((124-4)// (228+-2))'  # n+((n+n)+(n+n))
    parent = '1+((((2+3)+(4+(5+6)))+7)+(8+9))'  # n+((((n+n)+(n+(n+n)))+n)+(n+n))

    equation = parent
    equagene(equation)

    #       Jeux des parenthèses
    #       n+( ( ( (n+n)+(n+(n+n)) )+n)+(n+n) )
    #               |===|    |===|| |  | |===| |
    #                     |=======| |  |       |
    #             |=================|  |       |
    #           |======================|       |
    #         |================================|
#
