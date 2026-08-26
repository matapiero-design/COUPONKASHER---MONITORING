# Nettoyage des emails — run 2026-08-26 (mode : reel)

## Ce qui a ete traite

| Regle | Etage | Volume dans la boite | Threads releves |
|---|---|---|---|
| Divrei Torah et listes de Tehilim | archive | > 50 | 50 |
| Marketing voyage (compagnies, OTA, hôtels) | archive | 50 | 49 |
| Marketing grand public (télécom, retail, petites annonces) | archive | 50 | 48 |
| Marketing voyage (compagnies, OTA, hôtels) | corbeille | 50 | 47 |
| Marketing grand public (télécom, retail, petites annonces) | corbeille | 5 | 3 |
| Veille concurrence — offres casher | archive | 1 | 1 |
| **Total** | | | **198** |

> Les volumes marques `>` sont plafonnes par l'API Gmail, qui cesse de compter au-dela de 200 threads. Le vrai volume est superieur, parfois de beaucoup.

## Par expediteur

| Expediteur | Threads |
|---|---|
| ? | 149 |
| kayak@msg.kayak.com | 21 |
| marketing@ma.elal-mail.com | 9 |
| michael@mail.ottotheagent.com | 5 |
| matmid@ma.elal-airlines.com | 4 |
| contact@newsletter.lacompagnie.com | 3 |
| info@alps2alps.com | 2 |
| elal@ma.elalmatmid.com | 2 |
| travel@kiwi.com | 1 |
| info@kiwi.com | 1 |
| noreply@info.nhow-hotels.com | 1 |

## Ecartes par les protections

Ces threads matchaient une regle mais ont ete retenus. **Ils restent en place.**

| Expediteur | Sujet | Motif |
|---|---|---|
| elal@ma.elalmatmid.com | מוריס, עדיין אין לך FLY CARD? מצטרפים עכשיו ומקבלים כרטיס טיסה מתנה! פ | mot-cle sujet : כרטיס טיסה |
| bezeq_mail@bezeq.co.il | חשבונית בזק — ecartes par protection mot-cle sujet | mot-cle sujet : חשבונית |
| bezeq_mail@bezeq.co.il | חשבונית בזק — ecartes par protection mot-cle sujet | mot-cle sujet : חשבונית |
| bezeq_mail@bezeq.co.il | חשבונית בזק — ecartes par protection mot-cle sujet | mot-cle sujet : חשבונית |
| bezeq_mail@bezeq.co.il | חשבונית בזק — ecartes par protection mot-cle sujet | mot-cle sujet : חשבונית |

---

_Genere par `pipeline/email_cleanup.py` le 2026-08-26 14:12 UTC._
